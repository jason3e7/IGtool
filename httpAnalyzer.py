import requests
import string
import time

urlListFile = open('./urlList.txt', 'r')
urlList = urlListFile.read()
urlList = string.split(urlList, '\n')

for url in urlList:
	#print url
	r = requests.get(url)
	print r.headers
	#print r.content
	time.sleep(1)
