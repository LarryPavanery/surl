# -*- encoding: utf-8 -*-
'''
__author__ = "Larry_Pavanery
'''

from base_response import BaseResponse
from surl.database.url_db import URLDB
from surl.database.user_db import UserDB

import falcon


class UserStats(BaseResponse):

    def __init__(self):
        super(UserStats, self).__init__()
        self.user_db = UserDB()
        self.url_db = URLDB()

    def on_get(self, req, resp, userId):
        """ GET /users/:userId/stats """

        user = self.user_db.get(userId)
        if user:
            self.process_stats(resp, user)
        else:
            resp.status = falcon.HTTP_404

    def process_stats(self, resp, user):
        stats = []
        for url_key in user['url_keys']:
            '''TODO: change this!'''
            key = url_key.split('/')[-1]
            stats.append(self.url_db.get(key))
        self.return_body(resp, stats, falcon.HTTP_200)
