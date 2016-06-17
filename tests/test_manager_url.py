# -*- encoding: utf-8 -*-
'''
__author__ = "Larry_Pavanery
'''

import datetime
import falcon
import surl.helpers.shared as utils

from surl.endpoints.manager_url import ManagerURL
from base import TestBase
        
class TestManagerURL(TestBase):
    def setUp(self):
        super(TestManagerURL, self).setUp()

    def tearDown(self):
        super(TestManagerURL, self).tearDown()

    def get_url_404(self):
        response = self.simulate_request('/urls/{id}')
        self.assertEqual(self.srmock.status, falcon.HTTP_404)

    def post_url(self):
        self.url_id = utils.fake_url()
        path = '/users/{0}/urls'.format('larry')
        body = utils.encode_obj({'url': self.url_id})
        headers = {'Content-Type': 'application/json'}
        response = self.simulate_post(path, body=body, headers=headers)
        
        response_url = utils.decode_obj(response[0])['url']
        response_short_url = utils.decode_obj(response[0])['shorturl']
        id_short_url = utils.root_url() + response_short_url.split('/')[-1]
        
        self.assertEquals(self.url_id, response_url)
        self.assertEquals(id_short_url, response_short_url)
        self.assertEqual(self.srmock.status, falcon.HTTP_201)
                
    def test_url(self):
        self.get_url_404()
        self.post_url()

