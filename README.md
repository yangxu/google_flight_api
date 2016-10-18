
======
google_flight_api
======

A simple wrapper for the google flight api

Usage
=====

First, get yourself a `QPX Express Airfare API <https://developers.google.com/qpx-express/>`_.

Test your json request https://qpx-express-demo.itasoftware.com/

::

    from google_flight import google_flight_api


    g = google_flight_api.GoogleFlight("MY_API_KEY")
    data = {
              "request": {
                "slice": [
                  {
                    "origin": "PVD",
                    "destination": "MCO",
                    "date": "2016-12-04"
                  },
                  {
                    "origin": "MCO",
                    "destination": "PVD",
                    "date": "2016-12-24"
                  }
                ],
                "passengers": {
                  "adultCount": 1,
                  "infantInLapCount": 0,
                  "infantInSeatCount": 0,
                  "childCount": 0,
                  "seniorCount": 0
                },
                "solutions": 20,
                "refundable": 'false'
              }
            }
    g.get(data)



Examples
========
    g.KEY
    g.URL
    g.request
    g.params
    g.count
    g.data
    g.trips

Return the first tripOption

    g.lowest()

Print out all the search result

    g.print_result()

Print out json to readable

    g.readable(json_data)
    

