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

data11 = 0
data22 = 0

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
        global data11
        global data22
        data11, data22 = Utils.get_scrapi_data(web_site)
        if data11 == 0 :
            response = make_response(f'something was wrong with {web_site}, please check if the web site is correct',
                    400,)
        else : 
            response = make_response(
                        jsonify({'web' : web_site}),
                        200,)    
    else:
        response = make_response('You most use POST method',
                    400,)
    return response


@app.route('/data1', methods=['GET'])
@cross_origin()
def data1():
    response = make_response(data11,200,)
    return response
        

@app.route('/data2', methods=['GET'])
@cross_origin()
def data2():
    response = make_response(data22, 200,)
    return response


@app.route('/date', methods=['GET'])
@cross_origin()
def date():
    response = make_response(
                        jsonify({'date' : data['date']}),
                        200,)
    return response

@app.route('/titlepage', methods=['GET'])
@cross_origin()
def titlepage():
    response = make_response(
                        jsonify({'titlepage' : data['titlepage']}),
                        200,)
    return response

@app.route('/qtytitlepage', methods=['GET'])
@cross_origin()
def qtytitlepage():
    response = make_response(
                        jsonify({'qtytitlepage' : data['qtytitlepage']}),
                        200,)
    return response

@app.route('/lenthtitlepage', methods=['GET'])
@cross_origin()
def lenthtitlepage():
    response = make_response(
                        jsonify({'lenthtitlepage' : data['lenthtitlepage']}),
                        200,)
    return response

@app.route('/rigthdimensiontitlepage', methods=['GET'])
@cross_origin()
def rigthdimensiontitlepage():
    response = make_response(
                        jsonify({'rigthdimensiontitlepage' : data['rigthdimensiontitlepage']}),
                        200,)
    return response

@app.route('/metadescription', methods=['GET'])
@cross_origin()
def metadescription():
    response = make_response(
                        jsonify({'metadescription' : data['metadescription']}),
                        200,)
    return response

@app.route('/lenthmetadescription', methods=['GET'])
@cross_origin()
def lenthmetadescription():
    response = make_response(
                        jsonify({'lenthmetadescription' : data['lenthmetadescription']}),
                        200,)
    return response

@app.route('/rigthdimensionmetadescription', methods=['GET'])
@cross_origin()
def rigthdimensionmetadescription():
    response = make_response(
                        jsonify({'rigthdimensionmetadescription' : data['rigthdimensionmetadescription']}),
                        200,)
    return response


@app.route('/qtymetadescription', methods=['GET'])
@cross_origin()
def qtymetadescription():
    response = make_response(
                        jsonify({'qtymetadescription' : data['qtymetadescription']}),
                        200,)
    return response

@app.route('/keywords', methods=['GET'])
@cross_origin()
def keywords():
    response = make_response(
                        jsonify({'keywords' : data['keywords']}),
                        200,)
    return response


@app.route('/qtymeta_keywords', methods=['GET'])
@cross_origin()
def qtymeta_keywords():
    response = make_response(
                        jsonify({'qtymeta_keywords' : data['qtymeta_keywords']}),
                        200,)
    return response


@app.route('/h1title', methods=['GET'])
@cross_origin()
def h1title():
    response = make_response(
                        jsonify({'h1title' : data['h1title']}),
                        200,)
    return response

@app.route('/qtyh1title', methods=['GET'])
@cross_origin()
def qtyh1title():
    response = make_response(
                        jsonify({'qtyh1title' : data['qtyh1title']}),
                        200,)
    return response


@app.route('/imgwithoutalt', methods=['GET'])
@cross_origin()
def imgwithoutalt():
    response = make_response(
                        jsonify({'imgwithoutalt' : data['imgwithoutalt']}),
                        200,)
    return response

@app.route('/qtyimgwithoutalt', methods=['GET'])
@cross_origin()
def qtyimgwithoutalt():
    response = make_response(
                        jsonify({'qtyimgwithoutalt' : data['qtyimgwithoutalt']}),
                        200,)
    return response


@app.route('/imgwithaltempty', methods=['GET'])
@cross_origin()
def imgwithaltempty():
    response = make_response(
                        jsonify({'imgwithaltempty' : data['imgwithaltempty']}),
                        200,)
    return response


@app.route('/qtyimgwithaltempty', methods=['GET'])
@cross_origin()
def qtyimgwithaltempty():
    response = make_response(
                        jsonify({'qtyimgwithaltempty' : data['qtyimgwithaltempty']}),
                        200,)
    return response


@app.route('/totalimg', methods=['GET'])
@cross_origin()
def totalimg():
    response = make_response(
                        jsonify({'totalimg' : data['totalimg']}),
                        200,)
    return response

@app.route('/percentajeemptyaltinimg', methods=['GET'])
@cross_origin()
def percentajeemptyaltinimg():
    response = make_response(
                        jsonify({'percentajeemptyaltinimg' : data['percentajeemptyaltinimg']}),
                        200,)
    return response

@app.route('/google', methods=['GET'])
@cross_origin()
def google():
    response = make_response(
                        jsonify({'google' : data['google']}),
                        200,)
    return response

@app.route('/facebook', methods=['GET'])
@cross_origin()
def facebook():
    response = make_response(
                        jsonify({'facebook' : data['facebook']}),
                        200,)
    return response

@app.route('/twitter', methods=['GET'])
@cross_origin()
def twitter():
    response = make_response(
                        jsonify({'twitter' : data['twitter']}),
                        200,)
    return response


if __name__ == "__main__":
    app.run()
