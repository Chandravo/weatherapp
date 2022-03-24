from django.conf import settings
from django.shortcuts import render
import json
import urllib.request
import requests

def index(request):
    if (request.method == "POST"):
        city=request.POST['city']
        u_city=city
        
        #res=urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q'+city+'&appid=2da7194f075903ecb881d9d150c3376e').read()
        #j_data=json.load(res)
        #data={
        #    "country_code":str(json_data(['sys']))
        #}
        icon_url1 = "http://openweathermap.org/img/wn/"
        icon_url2="@2x.png"
        open_weather_api_key=str(settings.OPEN_WEATHER_API_KEY)
        accuweather_api_key=str(settings.ACCUWEATHER_API_KEY)
        OPEN_URL = 'https://api.openweathermap.org/data/2.5/weather?'
        open_param={'q':city,'appid':open_weather_api_key,'units':'metric'}
        open_r=requests.get(url=OPEN_URL,params=open_param)
        res=open_r.json()
        data={
            'country_code':str(res['sys']['country']),
            'coordinate':str(res['coord']['lon'])+' '+str(res['coord']['lat']),
            'temp':str(res['main']['temp'])+' °C',
            'pressure': str(res['main']['pressure']),
            'humidity': str(res['main']['humidity']),
            'description': str(res['weather'][0]['description']),
            'wspeed': str(res['wind']['speed']),
            'icon':icon_url1 + str(res['weather'][0]['icon'])+ icon_url2,
            'city': u_city.upper(),
            
        }
        
    else:
        city=''
        data={}
    
    return render(request,'login.html',{city:'city','data':data})