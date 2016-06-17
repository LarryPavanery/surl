# -*- encoding: utf-8 -*-
'''
__author__ = "Larry_Pavanery
'''

import falcon
from surl.helpers.shared import encode_obj


class BaseResponse(object):
    def on_get(self, req, resp, *args, **kwargs):
        resp.body = encode_obj({'status': 'ok'})
        resp.status = falcon.HTTP_200

    def return_body(self, resp, body, status=None):
        resp.body = encode_obj(body)
        resp.set_header('Content-Type', 'application/json')
        resp.content_type = "application/json"
        if status:
            resp.status = status
