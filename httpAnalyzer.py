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

data = [['host', 'statusCode', 'server', 'set-cookie']]
IGWriter.writerows(data)

for url in urlList:
	if url == '' :
		continue
	print 'analyze : %s' % url
	try :
		r = requests.get(url, timeout = 3)
	except requests.exceptions.RequestException as e :
		data = [[url, e]]
		IGWriter.writerows(data)
		time.sleep(0.5)
		continue
	if 'set-cookie' not in r.headers:
		r.headers['set-cookie'] = 'empty'
	if 'Server' not in r.headers:
		r.headers['Server'] = 'empty'
	data = [[url, r.status_code, r.headers['Server'], r.headers['set-cookie']]]
	IGWriter.writerows(data)
	time.sleep(0.5)

IGFile.close()
