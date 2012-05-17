from pymongo import Connection, ASCENDING, DESCENDING
#from bson.code import Code
#from bson.objectid import ObjectId

from bson.code import Code
from bson.objectid import ObjectId


connection = Connection("ds031867.mongolab.com", 31867)
db = connection["heroku_app3954850"]
db.authenticate("heroku_app3954850", "2o4lqlsq3mac57qj608kk8gbsp")

import algv2

signals = {
        "00:20:d8:28:8f:43": 15.6666666667, 
        "00:20:d8:28:8f:42": 20.3333333333, 
        "00:20:d8:2d:65:02": 13.3333333333, 
        "00:20:d8:2d:65:03": 10.0, 
        "00:20:d8:28:0e:42": 17.6666666667, 
        "00:20:d8:28:0e:43": 10.6666666667, 
        "00:20:d8:28:7a:43": 36.3333333333, 
        "00:20:d8:28:7a:42": 40.3333333333, 
        "00:20:d8:28:a8:02": 12.6666666667, 
        "00:20:d8:2d:b3:c0": 9.0
      }


algv2.binds = db.binds
print algv2.nearest_binds(signals)
