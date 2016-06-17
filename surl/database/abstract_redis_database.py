# -*- encoding: utf-8 -*-
'''
__author__ = "Larry_Pavanery
'''

from redis import Redis, ConnectionPool

import abc
import six
import ujson as json
import surl.helpers.shared as utils


@six.add_metaclass(abc.ABCMeta)
class AbstractRedisdb():

    def __init__(self):
        self.conf = utils.load_redis_config()
        self._redis_pool = ConnectionPool(host=self.conf['host'], port=self.conf['port'], db=0)

    def get(self, key):
        return Redis(connection_pool=self._redis_pool).get(key)

    def create(self, key, value):
        try:
            Redis(connection_pool=self._redis_pool).set(key, utils.encode_obj(value))
            return value
        except Exception as e:
            return None

    def delete(self, key):
        try:
            Redis(connection_pool=self._redis_pool).delete(key)
            return True
        except:
            return False

    def exists(self, key):
        return Redis(connection_pool=self._redis_pool).exists(key)
