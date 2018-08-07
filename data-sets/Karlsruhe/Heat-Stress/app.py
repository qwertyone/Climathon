from datetime import datetime
from flask import Flask,render_template
import time
from twitter import tweetAQI, tweetHeat
from multiprocessing import Process, Value
from query import queryLoop, queryAQI
from helper import IndexAirQuality, tipsAQI, tipsHI, calcC, dirHI, indexHeatStateColor

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	currentStateAQI = IndexAirQuality()
	resultAQI = queryAQI()
	tipAQI = tipsAQI()
	tweetAQI(currentStateAQI,resultAQI,tipAQI)
	tipHI = tipsHI()
	tempCurrentC = calcC()
	direction = dirHI()
	indexHeatState = indexHeatStateColor()
	tweetHeat(tipHI)
	return render_template('index.html', resultAQI=resultAQI, indexHeatState=indexHeatState, tempCurrentC=tempCurrentC, currentStateAQI=currentStateAQI, tipAQI=tipAQI, tipHI=tipHI, direction=direction)

@app.route('/posterClimate.html')
def poster():
	return render_template('posterClimate.html')

@app.route('/styles.css')
def css():
	return render_template('styles.css')

if __name__ == '__main__':
	recording_on = Value('b', True)
	p = Process(target = queryLoop, args = (recording_on,))
	p.start()
	app.run(host='0.0.0.0', port="5000", use_reloader = False)
	p.join()
