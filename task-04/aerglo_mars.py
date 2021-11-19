# import the necessary packages
import argparse
import requests
import urllib, json
import json

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--date", required=True,
	help="date when the picture was taken")
args = vars(ap.parse_args())

j ="https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date={}&api_key=HXfP0jiCzcdePKZ3zsPmstx3gddx0K6oPKmJsvT1".format(args["date"])
url = j
response = urllib.request.urlopen(url)
data = json.loads(response.read())
file = "aerglo_mars.json"
with open(file, 'w') as file_object:
 json.dump(data, file_object)