from algoliasearch import algoliasearch

client = algoliasearch.Client("DAT_USERNAME", "DAT_TOKEN")
index = client.init_index('Etsy')

from post import load
DATA = load()
for i in DATA: i['objectID'] = i['id']

print 'saving'

def make_batches(iterable, n=1):
    l = len(iterable)
    for ndx in range(0, l, n):
        yield iterable[ndx:min(ndx + n, l)]

for i, batch in enumerate(make_batches(DATA, n=1000)):
	print 'batch',i
	index.save_objects(batch)
