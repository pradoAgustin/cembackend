import configparser
import os
from configparser import ConfigParser

import pymongo


class ClientConfiguration:

    @staticmethod
    def get_client():
        config = configparser.ConfigParser()
        config.read('database/settings.ini')
        mongodb_path = "mongodb://%s:%s/" % (config['DEFAULT']['endpoint'], config['DEFAULT']['port'])

        client = pymongo.MongoClient(mongodb_path)

        return client


    @staticmethod
    def get_parser():
        config = configparser.ConfigParser()
        config.read('database/settings.ini')
        return config