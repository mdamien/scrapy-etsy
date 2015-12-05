from post import streamload

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Boolean, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.postgresql import ARRAY

engine = create_engine('postgresql://postgres@localhost/etsy')

Base = declarative_base()

class Product(Base):
	__tablename__ = 'etsy_products'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	shop = Column(String)
	rating_score = Column(Float)
	rating_count = Column(Integer)
	price = Column(Float)
	price_currency = Column(String)
	available = Column(Boolean)
	views = Column(Integer)
	imgs = ARRAY(String, dimensions=1)
	tags = ARRAY(String, dimensions=1)
	description = Column(Text)

	def __repr__(self):
		return "Product(id='%s', name='%s')" % (self.id, self.name)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

for i, item in enumerate(streamload()):
	product = Product(
		id=item['id'],
		name=item['name'],
		shop=item['shop']['title'],
		rating_score=item.get('rating_score',None),
		rating_count=item.get('rating_count',None),
		price=item['price'],
		price_currency=item['currency'],
		available=item.get('availability','') == 'stock',
		views=item['views'],
		imgs=item['imgs'],
		tags=item['tags'],
		description=item['description'])
	session.merge(product)
	if i % 1000 == 0:
		print(i,'=> commit')
		session.commit()
session.commit()

for product in session.query(Product).filter(Product.name.contains("Balm")):
	print(product.price)