
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

def tweetHeat(tipHI):
	from twython import Twython,TwythonError
	twitter = Twython(consumer_key, consumer_secret, access_token, access_secret)

	try:
		twitter.update_status(status = '#Karlsruhe #Heat ' + tipHI)
			
	except TwythonError as e:
		print e

def tweetAQI(currentStateAQI,resultAQI,tipAQI):
	from twython import Twython,TwythonError
	twitter = Twython(consumer_key, consumer_secret, access_token, access_secret)

	try:
		twitter.update_status(status = '#Karlsruhe #airQuality is ' + currentStateAQI + ' (' + str(resultAQI) + ')' + tipAQI)
			
	except TwythonError as e:
		print e
