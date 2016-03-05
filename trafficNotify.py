#!/usr/bin/env python3

#	traffic notification based on Bing maps traffic
#	https://msdn.microsoft.com/en-us/library/ff701717.aspx
#
#	requirements:
# 		BingMapsKey:	
#		pushover Acoount

import sys
import http.client
import requests
import json
import urllib
import datetime

def xrange(x):
    return iter(range(x))

#	url:
# 		wp.0=	starting point like  21.244467,6.692387
#		wp.1=	end point like 20.963454,7.049286
#		key=	BINGMAPSKEY
currentTime = datetime.datetime.now()
if currentTime.hour < 12:
	url = "http://dev.virtualearth.net/REST/V1/Routes/Driving?wp.0=21.244467,6.692387&wp.1=20.963454,7.049286&optmz=timeWithTraffic&routeAttributes=routePath&key=BINGMAPSKEY"
elif 12 <= currentTime.hour < 20:
	url = "http://dev.virtualearth.net/REST/V1/Routes/Driving?wp.0=20.963454,7.049286&wp.1=21.244467,6.692387&optmz=timeWithTraffic&routeAttributes=routePath&key=BINGMAPSKEY"

r = requests.get(url)
json_data = r.json()

message = "Fahrweg aktuell: " + json_data['resourceSets'][0]['resources'][0]['routeLegs'][0]['description'] + "\r\n"

elements = len(json_data['resourceSets'][0]['resources'][0]['routeLegs'][0]['itineraryItems'])
for x in xrange(elements):
	message += json_data['resourceSets'][0]['resources'][0]['routeLegs'][0]['itineraryItems'][x]['instruction']['text'] + "\r\n"
	pass

conn = http.client.HTTPSConnection("api.pushover.net:443")
conn.request("POST", "/1/messages.json",
	urllib.parse.urlencode({
		"token": "your pushover token",
		"user": "your pushover user",
		"message": message,
	}), { "Content-type": "application/x-www-form-urlencoded" })
conn.getresponse()

