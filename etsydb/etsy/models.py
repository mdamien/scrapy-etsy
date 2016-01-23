import json

from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core import serializers

class Product(models.Model):
	id = models.IntegerField(primary_key=True, db_index=True)
	name = models.CharField(max_length=255)
	shop = models.CharField(max_length=255)
	rating_score = models.FloatField(null=True)
	rating_count = models.IntegerField(null=True)
	price = models.FloatField()
	price_currency = models.CharField(max_length=10)
	available = models.BooleanField()
	views = models.IntegerField()
	imgs = ArrayField(models.CharField(max_length=255))
	tags = ArrayField(models.CharField(max_length=100))
	description = models.TextField()

	class Meta:
		ordering = ['-id']

	def to_json(self):
		serialized =  serializers.serialize('json', [self, ])
		return json.dumps(json.loads(serialized), indent=4)

	def __str__(self):
		return "Product(%s, %s)" % (self.id, self.name)