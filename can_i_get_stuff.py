import requests
import json

class TracksResourceLocation:
  layer = 753
  max_results = 5
  key = '2342af39f38841248750a72eb5a1a0c5'
  radius = 20000  

  def __init__(self, lat, long):
    self.x = long
    self.y = lat

  def getUri(self):
    return 'http://api.koordinates.com/api/vectorQuery.json/'

  def getRequestParams(self):
    return {
            'layer': self.layer, 
            'max_results': self.max_results,
            'key': self.key,
            'radius': self.radius, 
            'x': self.x, 
            'y': self.y,
            'geometry': 'false'
    }

class Track:
  def __init__(self, name, lat, long):
    self.name = name
    self.lat = lat
    self.long = long

  def asJson(self):
    return json.dumps(self.__dict__)

class TracksBuilder:
  def __init__(self, tracksDict):
    self.tracksDict = tracksDict

  def getTracks(self):
    for t in self.tracksDict['vectorQuery']['layers']['753']['features']:
      print "track name: %s" % t['properties']['DESCRIPTION']
    return []

t = Track("Matiu", 123, 345)
print t.asJson()

#41.2889 S, 174.7772 E is wellington
loc = TracksResourceLocation(-41.2889, 174.7772)
r = requests.get(loc.getUri(), loc.getRequestParams())
print "response: %s" % r.status_code
ts = TracksBuilder(r.json()).getTracks()
