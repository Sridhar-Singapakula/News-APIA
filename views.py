from django.shortcuts import render

import requests
import json
# Create your views here.
API_KEY="4331975854ef4ce78569045d1776f692"

def home(request):
    country=request.GET.get('country')
    url=f'https://newsapi.org/v2/top-headlines?country={country}&category=business&apiKey={API_KEY}'
    response=requests.get(url)
    data=response.json()
    
    articles=data['articles']
    
    
    name={
        
        'articles' : articles
    }
    
    return render(request,'home.html',name)