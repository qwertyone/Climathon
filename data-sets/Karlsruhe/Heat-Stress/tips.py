from numpy import random

############AQI recommendations G, M, U1, U2, V, H
g1 = ''
g2 = ''
g3 = ''
g4 = ''
g5 = ''
g6 = ''

#moderate status results
m1 = 'Some people might be sensitive to the air right now.'
m2 = 'In rare cases, this air quality might bother some.'
m3 = 'Consider avoiding prolonged or heavy exertion if #airQuality affects you.'
m4 = 'For most, this air is nice.'

#unhealthy for sensitive group results
u11 = 'People who are sensitive to pollution might want to stay inside right now.'
u12 = 'If the particle pollution rises, the air will become #Unhealthy.'
u13 = 'People, whom are elderly, young, #diabetic, lower SES and with either #heart or #lung #disease are at risk for adverse health effects right now'
u14 = 'If you are sensitive to air pollution, more frequent breaks will help you right now.'
u15 = 'Asthmatics should have their medicines ready, action plans prepared.'
u16 = 'If you have #heartDisease, please contact your doctor if you feel palpitations, shortness of breath, or unusual fatigue.'

#unhealthy results
u21 = '#airQuality might affect outdoor activities for everyone. Please take caution.'
u22 = 'Sensitive groups are likelier now to demonstrate adverse health symptoms.'
u23 = 'It tastes dustier than normal. Your workout is probably suffering from it.'
u24 = 'Avoid either heavy or prolonged outdoor exercise right now - reschedule activities or move indoors. Be ready for more breaks if you choose to be outside.'
u25 = 'If you are #running, stay away from well traveled pathes. The location will increase the dirty air you breathe in.'
u26 = 'Switch the car ventilation setting to recirculate to filter the air when driving.'

#very unhealthy results
v1 = '#airQuality is expected to adversely affect everyone right now. Please shift outdoor activities to later or tomorrow morning.'
v2 = 'If you are sensitive to #airPollution, avoid outdoor activities.'
v3 = 'I recommend buying a portable oxygen tank right now.'

#hazardous results
h1 = 'Watch credible news outlets right now. They should be getting loud now.'
h2 = 'Shifting to indoor activities is better for your health.'
h3 = 'Just stay inside unless absolutely necessary. This air is bad for everyone.'

####Heat Index Tips (S,L,Y,D,R)

#Safe status results
s1 = '#OSHA will tell you that sweating does not work as well on humid days as it does on dry days.'
s2 = 'When the weather is dry, carry a sports bottle with water. You will be better prepared.'
s3 = 'Work schedules will need to change as Climate warms to avoid the negative effects of increasing heat.'
s4 = 'This bot is a pop-culture tool. It is best used as a starting point.'
s5 = 'People will acclimate to increased tempratures, up to a point. This can take up to 2 weeks.'
s6 = 'There are 3 strategic controls for heat: convective, radiant, and evaporative. This bot will explain in future tweets.'

#Yellow status results
y1 = 'It is a nice day in the city. Your children will love it.'
y2 = 'Fatigue is possible now if you are outside for extended times or perform heavy tasks.'
y3 = 'Drink water from your sports bottle and stay in the shade if possible.'
y4 = 'Remember to carry a water bottle with you.'
y5 = 'Hydration before any activity improves how the day ends.'
y6 = 'Turn on fans to move the air. To be effective, the moving air must contact your body. #Convection'

#work strategies 1) reduce heat source 2) convective heat control 3) radiant heat control 4) evaporative heat control
# 1) limit exposure time and/or temprature, 2) reduce metabolic heat load (i.e. automation, job redesign), 3) enhance tolerance time (exercise, fitness, electrolyte balance), 4) health and safety training
# 5) screen for heat intolerance (medical history, physical unfitness
# brainstorm from http://iloencyclopaedia.org/part-vi-16255/heat-and-cold/76-42-heat-and-cold/assessment-of-heat-stress-and-heat-stress-indicies
# resource at https://www.osha.gov/SLTC/emergencypreparedness/guides/heat.html

#Light Orange Status results
l1 = 'Uniforms might need altered to deal with the heat.'
l2 = 'I hope you have dry uniforms and a sports bottle with water for #Sports.'
l3 = 'Outdoor activities need to be limited to 2 hours or less.'
l4 = 'Maybe activities need moved to morning or evening times. It is cooler.'
l5 = 'It is hot enough to remove inessential equipment.'
l6 = 'Soon, convection or air flow strategies to deal with heat will be ineffective alone. Combine with shade.'
l7 = 'Plants have optimum conditions for growth. 5 C above this point, plants experience their own form of fatigue.' #https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3728475/
l7 = 'If you have a bottle, please fill it is free: http://bit.ly/DrinkWaterKA'
l8 = 'Important: free Water Fountain App by @stadtwerke_KA - http://bit.ly/DrinkWaterKA'

#Dark Orange results
d1 = 'It is time to move indoors and into a cool area.'
d2 = 'If you are playing a sport with a helmet or shoulder pads, please take them off.'
d3 = 'Due to the heat, consider earlier as well as later start times and split shifts for outdoor work.'
d4 = '#Safety caution: avoid strenuous work due to the high heat in #Karlsruhe.'
d5 = 'Heat cramps and heat exhaustion likely.'

#Red results
r1 = 'Please stay inside an air conditioned building.'
r2 = 'Heat stroke is likely.'

def R():
	R = [r1,r2]
	tipHI = random.choice(R)
	return tipHI

def L():
	L=[l1, l2, l3, l4, l5, l6, l7, l8]
	tipHI = random.choice(L)
	return tipHI

def D():
	D = [d1, d2, d3, d4, d5]
	tipHI = random.choice(D)
	return tipHI

def Y():
	Y=[y1, y2, y3, y4, y5, y6]
	tipHI = random.choice(Y)
	return tipHI

def S():
	S=[s1, s2, s3, s4, s5, s6]
	tipHI = random.choice(S)
	return tipHI
	
def G():
	G = [g1, g2, g3, g4, g5, g6]
	tipAQI = random.choice(G)
	return tipAQI

def M():
	M = [m1, m2, m3, m4]
	tipAQI = random.choice(M)
	return tipAQI

def U1():
	U1 = [u11,u12,u13, u14, u15, u16]
	tipAQI = random.choice(U1)
	return tipAQI
	
def U2():
	U2 = [u21, u22, u23, u24, u25, u26]
	tipAQI = random.choice(U2)
	return tipAQI

def V():
	V = [v1, v2, v3, u26]
	tipAQI = random.choice(V)
	return tipAQI

def H():
	H = [h1, h2, h3, u26]
	tipAQI = random.choice(H)
	return tipAQI
