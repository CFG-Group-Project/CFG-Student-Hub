from django.shortcuts import render
from .models import timeritem
# Create your views here.
import requests

def study(request):
    url = "https://motivational-quotes1.p.rapidapi.com/motivation"

    payload = {
        "key1": "value",
        "key2": "value"
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "7131b4b784mshfcc1203f2832389p1f0b8cjsn7f45824084c1",
        "X-RapidAPI-Host": "motivational-quotes1.p.rapidapi.com"
    }

    quotes = requests.request("POST", url, json=payload, headers=headers)

    print(quotes.text)
    return render(request, "studyzone/study.html", {'quotes': quotes})
