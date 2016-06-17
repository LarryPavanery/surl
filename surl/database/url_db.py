# -*- encoding: utf-8 -*-
'''
__author__ = "Larry_Pavanery
'''

from abstract_redis_database import AbstractRedisdb
from surl.model.url import URL


class URLDB(AbstractRedisdb):

    def __init__(self):
        super(URLDB, self).__init__()

    def create(self, id, url, shorturl):
        key = shorturl
        value = URL(id, url, shorturl)
        return super(URLDB, self).create(key, value)

