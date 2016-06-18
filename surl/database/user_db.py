# -*- encoding: utf-8 -*-
'''
__author__ = "Larry_Pavanery
'''

from abstract_redis_database import AbstractRedisdb
from surl.model.user import User


class UserDB(AbstractRedisdb):

    def __init__(self):
        super(UserDB, self).__init__()

    def save(self, user_id):
        return super(UserDB, self).save(user_id, User(user_id))

    def user_has_url(self, user_id, url_key):
        user = super(UserDB, self).get(user_id)
        return url_key in user['url_keys']

    def update_user(self, user_id, url_key):
        user = super(UserDB, self).get(user_id)
        user['url_keys'].append(url_key)
        return super(UserDB, self).save(user_id, User(user_id, user['url_keys']))
