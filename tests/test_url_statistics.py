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
    
    def create_user_and_shorturl(self):
        self.user_id = self.create_user()
        self.response = self.post_url()
        
    def create_user(self):
        user_id = utils.fake_name()
        path = '/users'
        body = utils.encode_obj({'id': user_id})
        headers = {'Content-Type': 'application/json'}
        response = self.simulate_post(path, body=body, headers=headers)
        response_user_id = utils.decode_obj(response[0])['id']
        self.assertEquals(user_id, response_user_id)
        self.assertEqual(self.srmock.status, falcon.HTTP_201)
        return response_user_id
        
    def post_url(self):
        url = utils.fake_url()
        path = '/users/{0}/urls'.format(self.user_id)
        body = utils.encode_obj({'url': url})
        headers = {'Content-Type': 'application/json'}
        return self.simulate_post(path, body=body, headers=headers)
        
    def get_urls(self):
        self.id_surl = utils.decode_obj(self.response[0])['shorturl'].split('/')[-1]
        path = '/urls/{0}'.format(self.id_surl)
        self.simulate_request(path)
        self.assertEqual(self.srmock.status, falcon.HTTP_301)
        
    def get_stats(self):
        path = '/stats/{0}'.format(self.id_surl)
        self.response_get_stats = self.simulate_request(path)
        self.assertEqual(self.srmock.status, falcon.HTTP_200)
        self.hits = utils.decode_obj(self.response_get_stats[0])['hits']
        
    def increment_hits(self):
        self.get_urls()
        self.get_stats()
        
    def test_get_urls_301(self):
        self.create_user_and_shorturl()
        self.increment_hits()
        self.assertEqual(self.hits, 1)
        self.increment_hits()
        self.assertEqual(self.hits, 2)
        for i in range(1000):
            self.increment_hits()
        self.assertEqual(self.hits, 1002)
        