import requests
import json
from numpy import random 
import tweepy
from tweepy import OAuthHandler


g1 = ''
g2 = ''
g3 = ''
g4 = ''
g5 = ''
g6 = ''
G = [g1, g2, g3, g4, g5, g6]

#moderate status results
m1 = 'Some people might be sensitive to the air right now.'
m2 = 'In rare cases, this air quality might bother some.'
m3 = 'Consider avoiding prolonged or heavy exertion if #airQuality affects you.'
m4 = 'For most, this air is nice.'
M = [m1, m2, m3, m4]

#unhealthy for sensitive group results
u11 = 'People who are sensitive to pollution might want to stay inside right now.'
u12 = 'If the particle pollution rises, the air will become #Unhealthy.'
u13 = 'People, whom are elderly, young, #diabetic, lower SES and with either #heart or #lung #disease are at risk for adverse health effects right now'
u14 = 'If you are sensitive to air pollution, more frequent breaks will help you right now.'
u15 = 'Asthmatics should have their medicines ready, action plans prepared.'
u16 = 'If you have #heartDisease, please contact your doctor if you feel palpitations, shortness of breath, or unusual fatigue.'

U1 = [u11,u12,u13, u14, u15, u16]

#unhealthy results
u21 = '#airQuality might affect outdoor activities for everyone. Please take caution.'
u22 = 'Sensitive groups are likelier now to demonstrate adverse health symptoms.'
u23 = 'It tastes dustier than normal. Your workout is probably suffering from it.'
u24 = 'Avoid either heavy or prolonged outdoor exercise right now - reschedule activities or move indoors. Be ready for more breaks if you choose to be outside.'
u25 = 'If you are #running, stay away from well traveled pathes. The location will increase the dirty air you breathe in.'
u26 = 'Switch the car ventilation setting to recirculate to filter the air when driving.'


U2 = [u21, u22, u23, u24, u25, u26]

#very unhealthy results
v1 = '#airQuality is expected to adversely affect everyone right now. Please shift outdoor activities to later or tomorrow morning.'
v2 = 'If you are sensitive to #airPollution, avoid outdoor activities.'
v3 = 'I recommend buying a portable oxygen tank right now.'


V = [v1, v2, v3, u26]

#hazardous results
h1 = 'Watch credible news outlets right now. They should be getting loud now.'
h2 = 'Shifting to indoor activities is better for your health.'
h3 = 'Just stay inside unless absolutely necessary. This air is bad for everyone.'

H = [h1, h2, h3, u26]

##initialization
tokenAPI = ''
#city coordinates here
coordinates = '' 
requestAQI = 'http://api.waqi.info/feed/geo:' + coordinates + '/?token=' + tokenAPI
r = requests.get(requestAQI)

JSON = json.loads(r.text)
result = JSON['data']['aqi']

currentCondition = ''
tip = ''

def IndexAirQuality(result):
    if result < 50:
        currentCondition = 'Good'
        return currentCondition
    elif 51 > result and result <= 100:
        currentCondition = 'Moderate'
        return currentCondition
    elif 101 > result and result <= 150:
        currentCondition = 'Unhealthy for Sensitive Groups'
        return currentCondition
    elif 151 > result and result <= 200:
        currentCondition = 'Unhealthy'
        return currentCondition
    elif 201 > result and result <= 300:
        currentCondition = 'Very Unhealthy'
        return currentCondition
    else:
        currentCondition = 'Hazardous'
        return currentCondition

def tipsAir(currentState):

    if currentState == 'Good':
        tip = random.choice(G)
        return tip
    elif currentState == 'Moderate':
        tip = random.choice(M)
        return tip
    elif currentState == 'Unhealthy for Sensitive Groups':
        tip = random.choice(U1)
        return tip
    elif currentState == 'Unhealthy':
        tip = random.choice(U2)
        return tip
    elif currentState == 'Very Unhealthy':
        tip = random.choice(V)
        return tip
    else:
        tip = random.choice(H)
        return tip

currentState = IndexAirQuality(result)
tip = tipsAir(currentState)
post = '#Karlsruhe #airQuality is ' + currentState + '(' + str(result) + ')' + tip
#print(post)

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

if (not api):
    print ('Problem connecting to API')

try:
    if api.update_status(status=post):
        print("Successful posting")

except tweepy.error.TweepError as e:
    print(e)

