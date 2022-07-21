import requests
import unittest
import json

# url of our REST API
api_url = "http://127.0.0.1:5000/locations?"

class Tests(unittest.TestCase):
    def test1(self):
        location_key = "ABBN"
        response = requests.get(api_url + "location=" + location_key)
        response = response.text
        json_string = json.loads(response)
        self.assertEqual(json_string["Temperature"], '35 F (2 C)')
        self.assertEqual(json_string["Pressure"], '30.39 in. Hg (1029 hPa)')

    def test2(self):
        location_key = "AGGL"
        response = requests.get(api_url + "location=" + location_key)
        response = response.text
        json_string = json.loads(response)
        self.assertEqual(json_string["Temperature"], '84 F (29 C)')
        self.assertEqual(json_string["Pressure"], '29.83 in. Hg (1010 hPa)')


if __name__ == '__main__':
    unittest.main()