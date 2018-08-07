from datetime import datetime
import time
import requests
import json

def queryAQI():
	tokenAPI = ''
	coordinates = '49.0069;8.4037'
	requestAQI = 'http://api.waqi.info/feed/geo:' + coordinates + '/?token=' + tokenAPI
	r = requests.get(requestAQI)
	JSON = json.loads(r.text)
	resultAQI = JSON['data']['aqi']

	return resultAQI

def queryHC():
	URLOpenMaps = 'http://api.openweathermap.org/data/2.5/weather?id=2892794&APPID=fdfd94179b48c4f5bddf8aa28734aebe'
	r = requests.get(URLOpenMaps)
	JSON = json.loads(r.text)
	#city = JSON['name']
	humCurrent= JSON['main']['humidity']
	#tempCurrentRaw = JSON['main']['temp']
	return humCurrent
	
def queryTemp():
	URLOpenMaps = 'http://api.openweathermap.org/data/2.5/weather?id=2892794&APPID=fdfd94179b48c4f5bddf8aa28734aebe'
	r = requests.get(URLOpenMaps)
	JSON = json.loads(r.text)
	#city = JSON['name']
	#humCurrent= JSON['main']['humidity']
	tempCurrentRaw = JSON['main']['temp']
	
	return tempCurrentRaw

def queryLoop(loopOn):
	while True:
		if loopOn.value == True:
			queryAQI()
			queryTemp()
			queryHC()
			t = str(datetime.now())
			print("query made at " + t)
		time.sleep(200)


#print(queryAQI())
#print(queryTemp())
#print(queryHC())
