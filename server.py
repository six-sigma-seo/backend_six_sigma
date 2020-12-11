"""This is the main  file that control all aplication internal  flow"""
#Flask
from flask import Flask, make_response, request , jsonify,  redirect, url_for, session
from configuration import Configuration
from flask_cors import CORS, cross_origin


#six_sigma
from utils import Utils

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

data = 0
# Routes
@app.route('/', methods=['GET'])
@cross_origin()
def init():
    """ return a message to be display on root route"""

    return "Welcome to SIX SIGMA, this api is only available to SIX SIGMA developers"

@app.route('/web', methods=['POST'])
@cross_origin()
def get_web():
    """ resive a web address by POST method and response with 200 Ok if all work ok
        and 400 if not"""
    if request.method == 'POST':
        web_site = request.json['web']
        global data
        data, general_data = Utils.get_scrapi_data(web_site)
        if data == 0 :
            response = make_response(f'something was wrong with {web_site}, please check if the web site is correct',
                    400,)
        else : 
            response = make_response(general_data,200,)
    else:
        response = make_response('You most use POST method',
                    400,)
    return response


@app.route('/textualalternatives', methods=['GET'])
@cross_origin()
def textualalternatives():
    textual_data = Utils.get_textual_alternatives(data)
    response = make_response(textual_data,200,)
    return response
        

@app.route('/metadescription', methods=['GET'])
@cross_origin()
def metadescription():
    meta_data = Utils.get_meta_data(data)
    response = make_response(meta_data,200,)
    return response


@app.route('/titlepage', methods=['GET'])
@cross_origin()
def titlepage():
    titlepage_data = Utils.get_titlepage_data(data)
    response = make_response(titlepage_data,200,)
    return response


@app.route('/textualhierarchies', methods=['GET'])
@cross_origin()
def textualhierarchies():
    textualhierarchies_data = Utils.get_textualhierarchies_data(data)
    response = make_response(textualhierarchies_data,200,)
    return response

@app.route('/disusedlabels', methods=['GET'])
@cross_origin()
def disusedlabels():
    disusedlabels_data = Utils.get_disusedlabels_data(data)
    response = make_response(disusedlabels_data,200,)
    return response

if __name__ == "__main__":
    app.run()
