import requests

sites = None

with open('./opendns-top-domains.txt') as f:
	sites = f.readlines()

for site in sites:
	try:
		requests.get("http://%s" % site.strip('\n'))
	except:
		print site.strip('\n')

