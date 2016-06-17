# -*- encoding: utf-8 -*-
'''
__author__ = "Larry_Pavanery
'''

import falcon
from base_response import BaseResponse


class URLStatistics(BaseResponse):

    def on_get(self, req, resp):
        """ GET /stats/:id """
        print ('UserStatistics')
