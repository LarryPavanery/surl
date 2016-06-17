# -*- encoding: utf-8 -*-
'''
__author__ = "Larry_Pavanery
'''

import datetime
import ujson as json

import falcon
import falcon.testing as testing

from surl.endpoints import base_response


class TestBaseResponse(testing.TestBase):
    def before(self):
        self.base_response_resource = base_response.BaseResponse()
        self.api.add_route('/', self.base_response_resource)

    def test_response_ok(self):
        result = self.simulate_request('/')
        self.assertEqual(self.srmock.status, falcon.HTTP_200)
        response = json.loads(result[0])
        self.assertTrue(response[u'status'] == 'ok')
        
    def test_content_type_not_is_json(self):
        result = self.simulate_request('/')
        self.assertTrue('application/json' in dict(self.srmock.headers)['content-type'])
        
    def test_encoding_is_utf8(self):
        result = self.simulate_request('/')
        self.assertTrue('charset=UTF-8' in dict(self.srmock.headers)['content-type'])
        
    def test_return_body_override(self):
        class OverrideBaseResponse(base_response.BaseResponse):
            def on_get(self, req, resp, *args, **kwargs):
                self.return_body(resp, {'some': 'thing'})
                resp.status = falcon.HTTP_200
        
        self.api.add_route('/', OverrideBaseResponse())
        result = self.simulate_request('/')
        self.assertEqual(self.srmock.status, falcon.HTTP_200)
        response = json.loads(result[0])
        self.assertTrue(response[u'some'] == 'thing')
        