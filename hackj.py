import requests
import googlemaps
import socket
import geocoder
import time
while True:
    def countdown(t):
        
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
    timelol = 10
    countdown(timelol)
    g = geocoder.ip('me')
    lat = str(g.latlng[0])
    lng = str(g.latlng[1])
    print(lat)
    print(lng)
    response = requests.get("https://roads.googleapis.com/v1/speedLimits?path=" + lat + "," + lng + "&key=AIzaSyAWnZwkKruuvUwhrqWF51ZqIYggXZ7Y64s")

    if response.status_code == 404:
        speedLimit = 100

    

    #get speed of vehicle

    import subprocess
    import ast
    import time
    from math import asin, cos, pi, sqrt
    r = 6371 #earth radius in Kilometers
    p = pi/180
    timelol = 10
    

    countdown(timelol)
    lat2 = g.latlng[0]
    lng2 = g.latlng[1]
    lat = float(lat)
    lng = float(lng) 
    distance = 2 * r * asin(sqrt(0.5 - cos((lat2 - lat) * p)/2 + cos(lat * p) * cos(lat2 * p) * (1 - cos((lng2 - lng) * p)) / 2))
    speed = (distance*3600//timelol) #Multiplying by 3600 for Km/Hrs
    if speed<= speedLimit:
        print("You are below the speed limit!")


