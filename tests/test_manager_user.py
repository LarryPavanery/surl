# -*- encoding: utf-8 -*-
'''
__author__ = "Larry_Pavanery
'''

import datetime
import falcon
import surl.helpers.shared as utils

from base import TestBase
        
class TestManagerUser(TestBase):
    def setUp(self):
        super(TestManagerUser, self).setUp()

    def tearDown(self):
        super(TestManagerUser, self).tearDown()

    def get_user(self):
        pass

    def post_user(self):
        self.user_id = utils.fake_name()
        path = '/users'
        body = utils.encode_obj({'id': self.user_id})
        headers = {'Content-Type': 'application/json'}
        response = self.simulate_post(path, body=body, headers=headers)
        response_user_id = utils.decode_obj(response[0])['id']
        self.assertEquals(self.user_id, response_user_id)
        self.assertEqual(self.srmock.status, falcon.HTTP_201)
        
    def post_user_registered(self):
        path = '/users'
        body = utils.encode_obj({'id': self.user_id})
        headers = {'Content-Type': 'application/json'}
        response = self.simulate_post(path, body=body, headers=headers)
        self.assertEqual(self.srmock.status, falcon.HTTP_409)

    def put_user(self):
        pass

    def delete_user(self):
        path = '/user/{0}'.format(self.user_id)
        self.simulate_delete(path)
        self.assertEqual(self.srmock.status, falcon.HTTP_200)

    def delete_user_not_registered(self):
        path = '/user/{0}'.format('whatsOo')
        self.simulate_delete(path)
        self.assertEqual(self.srmock.status, falcon.HTTP_404)
        
    def test_user(self):
        self.post_user()
        self.post_user_registered()
        self.get_user()
        self.put_user()
        self.delete_user()
        self.delete_user_not_registered()
