from django.conf import settings
from django.shortcuts import render
import json
import urllib.request
import requests

def index(request):
    if (request.method == "POST"):
        city=request.POST['city']
        #res=urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q'+city+'&appid=2da7194f075903ecb881d9d150c3376e').read()
        #j_data=json.load(res)
        #data={
        #    "country_code":str(json_data(['sys']))
        #}
        
        api_key=str(settings.API_KEY)
        URL = 'https://api.openweathermap.org/data/2.5/weather?'
        param={'q':city,'appid':api_key,'units':'metric'}
        r=requests.get(url=URL,params=param)
        res=r.json()
        data={
            'country_code':str(res['sys']['country']),
            'coordinate':str(res['coord']['lon'])+' '+str(res['coord']['lat']),
            'temp':str(res['main']['temp'])+' Celcius',
            'pressure': str(res['main']['pressure']),
            'humidity': str(res['main']['humidity']),
            'description': str(res['weather'][0]['description']),
            'wspeed': str(res['wind']['speed']),
            
        }
        
    else:
        city=''
        data={}
    
    return render(request,'index.html',{city:'city', 'data':data})