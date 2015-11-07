from django.http import HttpResponse
from django.shortcuts import render
import requests
import json
from can_i_get_stuff import TracksResourceLocation, TracksBuilder

def homepage(request):
    loc = TracksResourceLocation(-41.2889, 174.7772)
    r = requests.get(loc.getUri(), loc.getRequestParams())
    ts = TracksBuilder(r.json()).getTracks()
    jsonList = [t.asJson() for t in ts]
    return HttpResponse(json.dumps(jsonList))

def index(request):

    return render(request, 'naturehack/index.html', {})

