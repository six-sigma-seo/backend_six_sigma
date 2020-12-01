"""This is the main  file that control all aplication internal  flow"""
#Flask
from flask import Flask, make_response, jsonify, redirect, url_for
from configuration import Configuration
from flask_cors import CORS, cross_origin

#six_sigma
#from utils import Utils

# Test
#import unittest

# Initializing app
app = Flask(__name__)
app.config.from_object(Configuration)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'SixSigma'

# app tests
#@app.cli.command()
# def test():
#    test = unittest.TestLoader().discover('test')
#    unittest.TextTestRunner().run(test)

# Routes
@app.route('/', methods=['GET'])
@cross_origin()
def init():
    return "Welcome to SIX SIGMA, this api is only available to SIX SIGMA developers"


        
        


if __name__ == "__main__":
    app.run()
