import json
from GBIFOccurrencesLib import OccurrenceSearchController
from AtlasOfLivingAustraliaOccurrencesLib import OccurrenceController

class TracksResourceLocation:
  layer = 753
  max_results = 100
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

class FloraResourceSearcher:
    username = 'caitlinhmiller@gmail.com'
    not_password = 'uI5wk4UxaoUd52Q'
    limit = 10
    radius = 1

    def __init__(self, lat, lon):
        self.x = long
        self.y = lat
        self.search_controller = OccurrenceSearchController(self.username, self.not_password)

    def search(self):
        return self.search_controller.get_occurrence_search_search({
            'decimalLatitude': self.x,
            'decimalLongitude': self.y,
            'limit': self.limit,
            'radius':self.radius,
        })

class Flora:
  def __init__(self, lat, long, genericName, scientificName, references):
    self.lat = lat
    self.long = long
    self.genericName = genericName
    self.scienticName = scientificName
    self.references = references
    self.type = 'plant'

  def asJson(self):
    return json.dumps(self.__dict__)

  def __str__(self):
    return self.asJson()

class FloraBuilder:
  def __init__(self, floraDict):
    self.floraDict = floraDict

  def getItems(self):
    flora = []
    for florum in self.floraDict['results']:
      flora.append(Flora(florum['decimalLatitude'],
                    florum['decimalLongitude'],
                    florum['genericName'],
                    florum['scientificName'],
                    florum['references']))
    return flora


class FaunaResourceSearcher(FloraResourceSearcher):

    def __init__(self, lat, lon):
        self.x = long
        self.y = lat
        self.search_controller = OccurrenceController()

    def search(self):
        return self.search_controller.get_occurrence_search({
            'decimalLatitude': self.x,
            'decimalLongitude': self.y,
            'limit': self.limit,
            'radius':self.radius,
        })

class FaunaBuilder(FloraBuilder):
    def getItems(self):
        flora = []
        #print self.floraDict
        for florum in self.floraDict['occurrences']:
            flora.append(Flora(florum['decimalLatitude'],
                    florum['decimalLongitude'],
                    florum['raw_scientificName'],
                    florum['raw_scientificName'],
                    ''))
        return flora

class Fauna(Flora):
    pass
