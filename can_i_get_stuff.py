import json

class TracksResourceLocation:
  layer = 753
  max_results = 10
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
            'geometry': 'true'
    }

class Track:
  def __init__(self, name, lat, long):
    self.name = name
    self.lat = lat
    self.long = long

  def asJson(self):
    return json.dumps(self.__dict__)

  def __str__(self):
    return self.asJson()


def zipper(coordlist):
    return [float(sum(i))/len(i) for i in zip(*coordlist)]

class MLSAverage:
  def __init__(self, trackcoords):
    self.trackcoords = trackcoords

  def getAverage(self):
    subavgs = []
    for coordlist in self.trackcoords:
          subavgs.append(zipper(coordlist))
    return zipper(coordlist)

class LSAverage:
  def __init__(self, trackcoords):
    self.trackcoords = trackcoords

  def getAverage(self):
    return zipper(self.trackcoords)

class TracksBuilder:
  def __init__(self, tracksDict):
    self.tracksDict = tracksDict

  def getTracks(self):
    tracks = []
    for track in self.tracksDict['vectorQuery']['layers']['753']['features']:
      geo = track['geometry']

      tracktype = geo['type']
      trackcoords = geo['coordinates']
      avgr =  MLSAverage(trackcoords) if tracktype == 'MultiLineString' else LSAverage(trackcoords)
      avg = avgr.getAverage()
      tracks.append(Track(track['properties']['DESCRIPTION'], avg[0], avg[1]))

    return tracks

