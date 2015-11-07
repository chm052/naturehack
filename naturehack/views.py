from django.http import HttpResponse
import requests
from can_i_get_stuff import TracksResourceLocation, TracksBuilder

def homepage(request):
    loc = TracksResourceLocation(-41.2889, 174.7772)
    r = requests.get(loc.getUri(), loc.getRequestParams())
    ts = TracksBuilder(r.json()).getTracks()
    return HttpResponse(ts)


