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

data = [['host']]
IGWriter.writerows(data)

for url in urlList:
	#print url
	#r = requests.get(url)
	#print r.headers
	#print r.content
	data = [[url]]
	IGWriter.writerows(data)
	#time.sleep(1)

IGFile.close()  
