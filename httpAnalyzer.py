import requests
import string
import time
import csv

urlListFile = open('./urlList.txt', 'r')
urlList = urlListFile.read()
urlList = string.split(urlList, '\n')
urlListFile.close()  

IGFile = open('./IGreport.csv', 'wb')
IGWriter = csv.writer(IGFile)

data = [['host', 'server']]
IGWriter.writerows(data)

for url in urlList:
	#print url
	print 'analyze : %s' % url
	r = requests.get(url)
	#print r.headers['Server']
	#print r.content
	data = [[url, r.headers['Server']]]
	IGWriter.writerows(data)
	time.sleep(0.5)

IGFile.close()  
