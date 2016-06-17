# -*- encoding: utf-8 -*-
'''
__author__ = "Larry_Pavanery
'''

from falcon import API
from routes import Routes
from surl.helpers.log import Log

logging = Log(__name__)

api = API()
rts = Routes()


def launch(conf, config_file="etc/api-config.conf"):
    for uri_template, resource in rts.get():
        logging.info('Register uri_template: {} to resource: {}.'.format(uri_template, resource))
        api.add_route(uri_template, resource)

    return api
