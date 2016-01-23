import json

def streamload():
    for line in open('../data.jl'):
        try:
            yield enhance(json.loads(line))
        except Exception as e:
            print(e)
            break

def load(small=False):
    DATA = []
    for i, item in enumerate(streamload()):
        DATA.append(item)
        if i % 100000 == 0:
            print('loaded',i,'items')
        if small and i > 1000:
            break
    return DATA

def enhance(i):
    i['id'] = i['url'].split('listing/')[1].split('/')[0]
    i['views'] = int(i['fineprints'][1].split()[0])
    #i['favs'] = int(i['fineprints'][1].split()[0])
    i['price'] = float(i['price'])
    if i['rating']:
        i['rating_score'] = float(i['rating'][0])
        i['rating_count'] = int(i['rating'][1])
        del i['rating']
    return i