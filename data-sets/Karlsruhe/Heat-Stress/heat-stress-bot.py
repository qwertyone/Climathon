import requests
import json
from numpy import random 
import tweepy
from tweepy import OAuthHandler

##twitter initialization
#details provided at https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens.html
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

##Tips to be posted with the heat conditions to help people cope
#random relevant facts Safe

s1 = '#OSHA will tell you that sweating does not work as well on humid days as it does on dry days. It is this muggy feeling. #Karlsruhe'
s2 = 'When the weather is dry, please drink more water. Sweat evaporates more quickly than in #highhumidity. #Karlsruhe'
s3 = '#Work #schedules will need to change as #Climate warms to avoid the negative effects of increasing heat. #Karlsruhe'
s4 = 'This twitter feed is both bot and real person. The #HeatStress bot provides clues on how heat will change work in the coming years. #Karlsruhe'
s5 = 'People will acclimate to increased tempratures, up to a point. This can take up to 2 weeks. #Karlsruhe'
s6 = 'Take it easy when the summer comes. This bot will help to keep you ready for the times when the heat is too much. #Karlsruhe'

S = [s1, s2, s3, s4, s5, s6]

#Yellow status results
y1 = '#Sports in #Karlsuhe need a tweaking. The #HeatIndex has reached light orange levels, meaning staying hydrated is important. Make sure water is accessible.'
y2 = 'The #HeatIndex in #Karlsruhe is high. Take water breaks every 30 to 45 minutes.'
y3 = 'Ten minutes out of the sun is a good idea right now. #Karlsruhe'
y4 = 'If it gets any hotter... Ice down towels-- it is getting hot in #Karlsruhe.'
y5 = 'It is beginning to be hot enough to rethink activities, maybe make them shorter or reschedule for the evening.'
y6 = 'Your helmets and safety equipment might be getting a little hotter than normal. #Karlsruhe'
y7 = 'Though not serious now, watch for signs of heat-related illness. The #HeatIndex in #Karlsruhe is light orange.'
y8 = 'Be sure to start drinking #moreWater on days like this. #HeatIndex #Karlsruhe'
y9 = 'At moments like this, stay inside or in the shade. It is hot in #Karlsruhe.'
y10 = 'Switch to less strenuous work or easier tasks. This #heat is a good reason to take it easy in #Karlsruhe.'

Y = [y1, y2, y3, y4, y5, y6, y7, y8, y9, y10]

#Light Orange Status results
l1 = 'The #HeatIndex in #Karlsruhe has hit Light Orange. Uniforms might need altered to deal with the heat.'
l2 = 'I hope you have dry uniforms for #Sports. The #HeatIndex in #Karlsruhe has hit Light Orange.'
l3 = 'Outdoor activities need to be limited to 2 hours or less. The #HeatIndex in #Karlsruhe has hit Light Orange.'
l4 = 'The #HeatIndex in #Karlsruhe has hit Light Orange. Maybe activities need moved to morning or evening times. It is cooler.'
l5 = 'It is hot enough to remove inessential equipment. The #HeatIndex in #Karlsruhe has hit Light Orange.'
l6 = 'If you are paying attention, GREAT! The heat is high and so is the risk. Reading this alert and being aware is a first step. #Karlsruhe'
l7 = 'Try to limit physical exertion. Use mechanical tools to reduce #HeatStress right now in #Karlsruhe.'
l8 = 'It is hot enough to have a #HeatStress expert nearby. The risk for #HeatStroke is high in #Karlsruhe.'
l9 = 'It is a good time to balance work and rest, as well as maintaining work discipline. It is hot in #Karlsruhe.'
l10 = 'If you are working outdoors, reschedule work activities to the morning or evening, when it is much cooler. You will save work and money doing so in #Karlsruhe.' 

L = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10]

#Dark Orange results
d1 = 'It is time to move indoors and into a cool area. The #HeatIndex in #Karlsruhe has hit Dark Orange. '
d2 = 'You know bad ideas. Here is one -- work outside in #Karlsruhe right now.'
d3 = 'Due to the heat, consider earlier as well as later start times and split shifts for outdoor work in #Karlsruhe.'
d4 = '#Safety caution: avoid strenuous work due to the high heat in #Karlsruhe.'
d5 = ''
d6 = ''

D = [d1, d2, d3, d4]

#Red results
r1 = 'It is dangerous outside. Please stay inside #Karlsruhe.'

R = [r1]
cityID = ''
###### retrieve cityID from http://bulk.openweathermap.org/sample/city.list.json.gz
apiID = ''
###### create your appID at https://home.openweathermap.org/api_keys

##get current weather data from openmaps
URLOpenMaps = 'http://api.openweathermap.org/data/2.5/weather?id=' + cityID + '&APPID=' + apiID
r = requests.get(URLOpenMaps)
JSON = json.loads(r.text)
city = JSON['name']
tempCurrentRaw = JSON['main']['temp']
humCurrent = JSON['main']['humidity']
currentCondition = 'Safe'
result = (tempCurrentRaw * 1.8) - 459.67
tip = random.choice(S)

#transform data to heat index data
#from Kelvin to C -- drybulb temprature assumed

def IndexHeat (tempCurrentRaw, humCurrent):
#equations from NOAA's heat index calculation methods @ http://www.wpc.ncep.noaa.gov/html/heatindex_equation.shtml
    tempCurrentF = (tempCurrentRaw * 1.8) - 459.67
    indexHeat = -42.379 + 2.04901523*tempCurrentF + 10.14333127*humCurrent - .22475541*tempCurrentF*humCurrent - .00683783*tempCurrentF*tempCurrentF - .05481717*humCurrent*humCurrent + .00122874*tempCurrentF*tempCurrentF*humCurrent + .00085282*tempCurrentF*humCurrent*humCurrent - .00000199*tempCurrentF*tempCurrentF*humCurrent*humCurrent
    
    ADJUSTMENT = 0
    
    if humCurrent < 13 and tempCurrentF > 80 and tempCurrentF < 112:
        ADJUSTMENT = ((13-humCurrent)/4) * sqrt((17 - abs(tempCurrentF - 95))/17)
        return ADJUSTMENT
    elif humCurrent > 85 and tempCurrentF > 80 and tempCurrentF < 87:
        ADJUSTMENT = (((humCurrent-85)/10) * ((87-tempCurrentF)/5))
        return ADJUSTMENT
    else:
        pass
   
    indexHeat = indexHeat - ADJUSTMENT
    result = (indexHeat + tempCurrentF)/2
    
    return result

#Heat Index Color Code
def IndexHeatState(currentCondition, result):
    if result < 80:
        currentCondition = 'Safe'
        return currentCondition
    elif 80 > result and result <= 90:
        currentCondition = 'Yellow'
        return currentCondition
    elif 90 > result and result <= 103:
        currentCondition = 'L_Orange'
        return currentCondition
    elif 103 > result and result <= 124:
        currentCondition = 'D_Orange'
        return currentCondition
    else:
        currentCondition = 'Red'
        return currentCondition

def tipsHeat(currentState):

    if currentState == 'Safe':
        tip == random.choice(S)
        return tip
    elif currentState == 'Yellow':
        tip == random.choice(Y)
        return tip
    elif currentState == 'L_Orange':
        tip == random.choice(L)
        return tip
    elif currentState == 'D_Orange':
        tip == random.choice(D)
        return tip
    else:
        tip == random.choice(R)
        return tip

currentIndexHeat = IndexHeat (tempCurrentRaw, humCurrent)
currentState = IndexHeatState(currentCondition, result)
 
##post to twitter
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

if (not api):
    print ('Problem connecting to API')

try:
    if api.update_status(status='The current Heat Index color is' + currentState +': ' +tip):
        print("Successful posting")

except tweepy.error.TweepError as e:
    print(e)

