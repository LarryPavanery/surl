# -*- encoding: utf-8 -*-
'''
__author__ = "Larry_Pavanery
'''

from abstract_redis_database import AbstractRedisdb
from surl.helpers.constants import USER_HASH
from surl.model.user import User


class UserDB(AbstractRedisdb):

    def __init__(self):
        super(UserDB, self).__init__()
        self.hash_name = USER_HASH

    def get(self, user_id):
        return super(UserDB, self).get(
            self.hash_name,
            user_id
        )

    def save(self, user_id, user=None):
        value = user if user else User(user_id)
        return super(UserDB, self).save(
            self.hash_name,
            user_id,
            value
        )

    def user_has_url(self, user_id, url_key):
        user = self.get(user_id)
        return url_key in user['url_keys']

    def update_user(self, user_id, url_key):
        user = self.get(user_id)
        user['url_keys'].append(url_key)
        return self.save(
            user_id,
            User(user_id, user['url_keys'])
        )

    def keys(self):
        return super(UserDB, self).keys(
            self.hash_name
        )

    def delete(self, user_id):
        return super(UserDB, self).delete(
            self.hash_name,
            user_id
        )

    def exists(self, user_id):
        return super(UserDB, self).exists(
            self.hash_name,
            user_id
        )
