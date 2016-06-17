# -*- encoding: utf-8 -*-
'''
__author__ = "Larry_Pavanery
'''

from abstract_redis_database import AbstractRedisdb
from surl.model.user import User


class UserDB(AbstractRedisdb):

    def __init__(self):
        super(UserDB, self).__init__()

    def create(self, id):
        key = id
        value = User(id)
        return super(UserDB, self).create(key, value)

