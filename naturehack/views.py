from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import requests
from json import JSONEncoder
import json
from can_i_get_stuff import TracksResourceLocation, TracksBuilder, \
                FloraResourceSearcher, FloraBuilder, \
                FaunaResourceSearcher, FaunaBuilder

class DeepEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

def homepage(request):
    #Auckland
    #loc = TracksResourceLocation(-36.8406 , 174.7400)
    #Wellington
    loc = TracksResourceLocation(-41.2889, 174.7772)
    r = requests.get(loc.getUri(), loc.getRequestParams())
    ts = TracksBuilder(r.json()).getTracks()
    jsonDict = {"response": ts}
    return JsonResponse(jsonDict, encoder=DeepEncoder)

def stuff(request):
    lat = float(request.GET.get('lat'))
    long = float(request.GET.get('long'))
    print "lat: %s long: %s" % (lat, long)
    #TODO: use lat and long to search for stuff...
    return JsonResponse({"response": [
       {"name": "Kiwi" , "type": "bird" },
       {"name": "Kaka" , "type": "bird" },
       {"name": "Tui"  , "type": "bird" },
       {"name": "Kauri", "type": "plant"}
    ]})

def index(request):
    return render(request, 'naturehack/index.html', {})

def searchflora(request):
    lat = float(request.GET.get('lat'))
    long = float(request.GET.get('long'))
    flora = FloraResourceSearcher(lat, long)
    results = FloraBuilder(flora.search()).getItems()
    jsonDict = {"response": results}
    return JsonResponse(jsonDict, encoder=DeepEncoder)

def searchfauna(request):
    lat = float(request.GET.get('lat'))
    long = float(request.GET.get('long'))
    fauna = FaunaResourceSearcher(lat, long)
    results = FaunaBuilder(fauna.search()).getItems()
    jsonDict = {"response": results}
    return JsonResponse(jsonDict, encoder=DeepEncoder)
