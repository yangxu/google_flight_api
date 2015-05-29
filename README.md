
======
google_flight_api
======

A simple wrapper for the google flight api

Usage
=====

First, get yourself a `QPX Express Airfare API <https://developers.google.com/qpx-express/>`_.

::

    from google_flight import google_flight_api


    g = GoogleFlight("MY_API_KEY")
    data = {
             "request":
             {
                "passengers":
                {
                   "adultCount": 1
                },
                "slice":
                [
                   {
                      "origin": "BOS",
                      "destination": "PVD",
                      "date": "2015-08-04"
                   },
                   {
                      "origin": "PVD",
                      "destination": "GNV",
                      "date": "2015-08-24"
                   }
                 ]
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
    

