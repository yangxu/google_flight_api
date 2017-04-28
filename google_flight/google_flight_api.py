import requests
import json


LOCALFILE = False

try:
    from local_settings import *
except ImportError, e:
    pass


__version__ = "0.1"

URL = 'https://www.googleapis.com/qpxExpress/v1/trips/search'
headers = {'Content-Type': 'application/json'}

class Struct:
    def __init__(self, **entries): 
        self.__dict__.update(entries)

class GoogleFlight(object):

   def __init__(self, key):
       self.URL = 'https://www.googleapis.com/qpxExpress/v1/trips/search?key=%s'%key
       self.KEY = key
       self.DEBUG = False
       self.request = None
       self.params = {}
       self.count = 0
       self.data = {}
       self.trips = None

   def get(self, params):
       self.params = params
       
       if LOCALFILE:
          with open('data.json') as data_file:
            data = json.load(data_file)

       else:
          r = requests.post(self.URL, data=json.dumps(params), headers=headers)
          self.request = r
          data = json.loads(r.text)

       self.data = data

       if self.DEBUG:
          self.write(self.data)
          
       try:
          self.count = len(self.data["trips"]["tripOption"])
       except:
           raise Exception(self.data)
       self.trips = self.data["trips"]["tripOption"]

   def write(self, data):
       f = open('debug.json', 'w')
       f.write(str(data))
       f.close()

   def readable(self,data):
      print json.dumps(data, indent=4, sort_keys=True)


   def print_trip(self,trip):
      Slice = 0
      for s in trip["slice"]:
         Slice = Slice + 1
         print "   Slice %s" % Slice
         for flight in s["segment"]:
            flight_number = flight["flight"]["number"]
            flight_carrier = flight["flight"]["carrier"]
            flight_origin = flight['leg'][0]['origin']
            flight_departureTime = flight['leg'][0]['departureTime']
            flight_destination = flight['leg'][0]['destination']
            flight_arrivalTime = flight['leg'][0]['arrivalTime']
            flight_mileage = flight['leg'][0]['mileage']
            print "      %s%s %s %s %s %s %s mileage"%(flight_carrier, flight_number, flight_origin, flight_departureTime, flight_destination, flight_arrivalTime, flight_mileage)


   def print_result(self):
       if self.trips != None:
          Solution = 0
          for trip in self.trips:
            Solution = Solution + 1
            print "\nSolution# %s Sale Price: %s"% (Solution, trip["saleTotal"])
            self.print_trip(trip)
       else:
          print "No data yet"

   def lowest(self):
      if self.trips != None:
        lowest = self.data["trips"]["tripOption"][0]
        for trip in self.data["trips"]["tripOption"]:
           if trip['saleTotal'] < lowest['saleTotal']:
              lowest = trip
        return Struct(**lowest)
      else:
         print "No data yet"


