import json
from collections import Counter

DATA = []
for i, line in enumerate(open('data.jl')):
    try:
        DATA.append(json.loads(line))
    except:
        print('fail at line', i)


def attrget(item, key):
    keys = key.split('.')
    for key in keys:
        item = item.get(key,'')
    return item

def stats(key, attrget=attrget, limit=10):
    arr = DATA
    def flat(arr):
        for x in arr:
            if type(x) == type([]):
                yield from flat(x)
            else:
                yield x.strip()

    c = Counter(flat([attrget(el,key) for el in arr]))

    count_all = len(arr)
    count_distinct = len(c)
    print()
    print(key,"   -   ",count_all,"values,",count_distinct,"distincts")
    print('----')

    for el,n in c.most_common(limit):
        p = n/count_all*100
        print("{:.1f}% ({}) {}".format(p,n,el))
    print()

stats('shop.title')
stats('price')
stats('availability')
stats('name')
stats('url')
stats('id', lambda i,k: i['url'].split('listing/')[1].split('/')[0])