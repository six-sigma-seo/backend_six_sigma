""" Some utilities that are used in the application"""

#Python
import requests
import json


class Utils:

    def get_scrapi_data(web_site):
        """ this funcion resive a web_site and return a diccionary 
            with information about the web site based on a scrapy sistem. """
        r = requests.get('https://app.scrapinghub.com/api/v2/datasets/UhNGprd2Cts/download?format=json') 
        if r.status_code == 200:
            data1 = r.text 
            data2 = r.text
            data1 = data1[1:]
            data1 = data1[:-1]
            data1 = json.loads(data1)
        else: 
            data1 = 0
            data2 = 0
        return data1, data2