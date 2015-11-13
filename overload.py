import requests

sites = None

with open('./opendns-top-domains.txt') as f:
	sites = f.readlines()

while True:
	for site in sites:
		try:
			requests.get("http://%s" % site.strip('\n'))
		except:
			pass

