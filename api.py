import requests
import bs4 as bs
from flask import Flask, request
from flask_restful import Resource, Api

#############
# DEFINITIONS
#############
source_data_url = "https://tgftp.nws.noaa.gov/data/observations/metar/decoded/" # url of our data source
server = Flask(__name__)
rest_api = Api(server)

##################
# HELPER FUNCTIONS
##################
'''
Helper function for parsing weather info and return a dictionary
that contains station name, temperature data and pressure data
'''
def parse_response(s):
    dic = {}
    split = s.split('\n')
    for line in split:
        if line.lower().startswith("temperature"):
            dic['Temperature'] = line.split(':')[1].strip()
        if line.lower().startswith("pressure"):
            dic['Pressure'] = line.split(':')[1].strip()
    return dic

'''
Helper function that gets all valid location keys from our data source
'''
def get_valid_keys(url):
    valid_keys = []
    response = requests.get(url)
    soup = bs.BeautifulSoup(response.text, "html.parser")
    for link in soup.find_all('a'):
        valid_keys.append(link.get('href'))
    return valid_keys


##################
# CREATE ENDPOINT
##################
class Locations(Resource):
    # our GET method of api
    def get(self):
        # parse arguments
        location = request.args.get('location')
        filename = location + ".TXT"

        # check if the provided key is valid. Return error message for invalid requests
        valid_keys = get_valid_keys(source_data_url)
        if filename not in valid_keys:
            return "Invalid location key! Bad request!", 400

        # query weather data from our data source
        url = source_data_url + location + ".TXT"
        response = requests.get(url)

        # parse response and extract temperature and pressure information
        response = parse_response(response.text)
        temp = response['Temperature']
        pres = response['Pressure']

        return {'Key': location,'Temperature': temp, 'Pressure': pres}, 200

# '/locations' is the endpoint to query weather data
rest_api.add_resource(Locations, '/locations')

if __name__ == '__main__':
    server.run()