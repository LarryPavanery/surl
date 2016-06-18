# -*- encoding: utf-8 -*-
'''
__author__ = "Larry_Pavanery
'''

import datetime
import falcon
import surl.helpers.shared as utils

from base import TestBase
        
class TestManagerURL(TestBase):
    def setUp(self):
        super(TestManagerURL, self).setUp()

    def tearDown(self):
        super(TestManagerURL, self).tearDown()
        
    def create_user(self):
        self.user_id = utils.fake_name()
        path = '/users'
        body = utils.encode_obj({'id': self.user_id})
        headers = {'Content-Type': 'application/json'}
        response = self.simulate_post(path, body=body, headers=headers)
        response_user_id = utils.decode_obj(response[0])['id']
        self.assertEquals(self.user_id, response_user_id)
        self.assertEqual(self.srmock.status, falcon.HTTP_201)
        return response_user_id
        
    def post_url(self):
        url = utils.fake_url()
        path = '/users/{0}/urls'.format(self.user_id)
        body = utils.encode_obj({'url': url})
        headers = {'Content-Type': 'application/json'}
        return self.simulate_post(path, body=body, headers=headers)
        
    def get_stats_by_userid(self):
        path = '/users/{0}/stats'.format(self.user_id)
        self.response_get_stats = self.simulate_request(path)
        self.assertEqual(self.srmock.status, falcon.HTTP_200)
        self.stats = utils.decode_obj(self.response_get_stats[0])

    def test_get_users_stats_by_userid(self):
        self.create_user()
        for i in range(10):
            self.post_url()
        self.get_stats_by_userid()
        self.assertEqual(len(self.stats), 10)
        

        