import os
import json
basedir = os.path.abspath(os.path.dirname(__file__))

with open("%s/data/access_password.json" %basedir,'r') as json_file:
    access_password = json.load(json_file)

with open("%s/data/seiscomp_database.json" %basedir,'r') as json_file:
    seiscomp_database = json.load(json_file)


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN') or  access_password['access_password']

    DB_USER = seiscomp_database['user']
    DB_PASSWORD = seiscomp_database['password']
    DB_HOST = seiscomp_database['ip']
    DB_NAME = seiscomp_database['database']

    
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config): 

    DEBUG = False

config = {
        'development': DevelopmentConfig,
        'production': ProductionConfig, 

        'default': DevelopmentConfig

            }
