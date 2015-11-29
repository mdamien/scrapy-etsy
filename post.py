import json

def load(small=False):
	DATA = []
	for i, line in enumerate(open('data.jl')):
	    try:
	        DATA.append(json.loads(line))
	    except:
	        print('fail at line', i)
	    if small and i > 1000:
	        break
	for i in DATA:
	    enhance(i)
	return DATA

def enhance(i):
    i['id'] = i['url'].split('listing/')[1].split('/')[0]
    i['views'] = int(i['fineprints'][1].split()[0])
    #i['favs'] = int(i['fineprints'][1].split()[0])
    if i['rating']:
        i['rating_score'] = float(i['rating'][0])
        i['rating_count'] = int(i['rating'][1])
        del i['rating']

