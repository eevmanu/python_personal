import simplejson as json

f1 = open('./1.json')
d1 = json.load(f1)
f1.close()

f2 = open('./2.json')
d2 = json.load(f2)
f2.close()

result = d1 + d2

fresult = open('./result.json', 'w')
json.dump(result, fresult)
fresult.close()
