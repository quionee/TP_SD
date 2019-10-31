import urllib.request
from collections import defaultdict


def fazRequest():
	fp = urllib.request.urlopen("http://localhost:80/identificar")
	mybytes = fp.read()

	mystr = mybytes.decode("utf8")
	fp.close()

	return mystr



vet = defaultdict(int)

for index in range(50): 
	res = fazRequest()
	vet[res.replace('\n', '')] += 1

print (dict(vet))
