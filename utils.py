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
            data = r.text 
            data = data[1:]
            data = data[:-1]
            data = json.loads(data)
            general_data = {
                            "date": data['date'],
                            "titilepage": data['titlepage'],
                            "metadescription": data['metadescription'],
                            "features" : [
                                {
                                "title": "Alternativas Textuales",
                                "description": "Todos los elementos no visuales de la pagina deben incluir la etiqueta alt para facilitar la lectrura por el robot de Google.",
                                "boolean": True,
                                "endpoint": "/textualalternatives"
                                },
                                {
                                "title": "Titulo de pagina",
                                "description": "Unicamente debe exister una etiqueta title dentro de la estructura de la pagina y el contendio de esta debe ser descriptivo en relación al contenido de la pagina.",
                                "boolean": True,
                                "endpoint": "/titlepage"
                                },
                                {
                                "title": "Deaclaración de idioma",
                                "description": "Se debe especificar el idioma de la pagina con la etiqueta: <html lang=eng>.",
                                "boolean": True,
                                "endpoint": "???"
                                },
                                {
                                "title": "Estructura Semantica",
                                "description": "La pagina deberia utilizar un mínimo de etiquetas semánticas las cuales son: header, section, footer, main.",
                                "boolean": True,
                                "endpoint": "???"
                                },
                                {
                                "title": "Etiqueta Arial",
                                "description": "Las etiquetas de button e input deberian tener el atributo aria-label y el contenido de este debe ser superior a 6 caracteres.",
                                "boolean": True,
                                "endpoint": "???"
                                },
                                {
                                "title": "Jerarquias Textuales",
                                "description": "La etiquetas de titulos deben seguir un jerarquia de acuerdo a su orden, solo deberia usarse una vez la etiqueta <h1> por ejemplo.",
                                "boolean": True,
                                "endpoint": "/textualhierarchies"
                                },
                                {
                                "title": "Etiquetas en desuso",
                                "description": "Con el paso de las versiones de html se han dejado de usar ciertas etiquetas, se recomienda su sustitución.",
                                "boolean": True,
                                "endpoint": "/disusedlabels"
                                },
                                {
                                "title": "Meta información",
                                "description": "Se recomienda el uso de las etiquetas de meta información para asegurar que el robot de google entienda nuestra pagina. Así como para la correcta representación en redes sociales.",
                                "boolean": True,
                                "endpoint": "/metadescription"
                                }
                            ]
                        }
        else: 
            data = 0
        return data, general_data
    
    def get_textual_alternatives(data):
        """ something """
        textual_data = {
                            "imgwithoutalt": data['imgwithoutalt'],
                            "qtyimgwithoutalt": data['qtyimgwithoutalt'],
                            "imgwithaltempty": data['imgwithaltempty'],
                            "qtyimgwithaltempty": data['qtyimgwithaltempty'],
                            "totalimg": data['totalimg'],
                            "percentajeemptyaltinimg": data['percentajeemptyaltinimg']
                        }
        return textual_data
    
    def get_meta_data(data):
        """ something """
        meta_data = {
                        "metadescription": data['metadescription'],
                        "lenthmetadescription": data['lenthmetadescription'],
                        "rigthdimensionmetadescription": data['rigthdimensionmetadescription'],
                        "qtymetadescription": data['qtymetadescription'],
                        "google": data['google'],
                        "facebook": data['facebook'],
                        "twitter": data['twitter']
                    }
        return meta_data


    def get_titlepage_data(data):
        """something"""
        titlepage_data = {
                            "titlepage": data['titlepage'],
                            "qtytitlepage": data['qtytitlepage'],
                            "lenthtitlepage": data['lenthtitlepage'],
                            "rigthdimensiontitlepage": data['rigthdimensiontitlepage'],
                        }
        return titlepage_data
    


    def get_textualhierarchies_data(data):
        """something"""
        textualhierarchies_data = {
                                    "h1title": data['h1title'],
                                    "qtyh1title": data['qtyh1title'],
                                }
        return textualhierarchies_data

    def get_disusedlabels_data(data):
        """something"""
        disusedlabels_data = {
                                "keywords": data['keywords'],
                                "qtymeta_keywords": data['qtymeta_keywords'],
                            }
        return disusedlabels_data