# -*- encoding: utf-8 -*-
'''
__author__ = "Larry_Pavanery
'''

from redis import Redis, ConnectionPool

import abc
import six
import surl.helpers.shared as utils


@six.add_metaclass(abc.ABCMeta)
class AbstractRedisdb():

    def __init__(self):
        self.conf = utils.load_redis_config()
        self._redis_pool = ConnectionPool(host=self.conf['host'], port=self.conf['port'], db=0)

    def get(self, key):
        value = Redis(connection_pool=self._redis_pool).get(key)
        try:
            return utils.decode_obj(value)
        except:
            return value

    def save(self, key, value):
        try:
            Redis(connection_pool=self._redis_pool).set(key, utils.encode_obj(value))
            return value
        except Exception:
            return None

    def delete(self, key):
        try:
            Redis(connection_pool=self._redis_pool).delete(key)
            return True
        except:
            return False

    def exists(self, key):
        return Redis(connection_pool=self._redis_pool).exists(key)

    def next_id(self, id_auto_inc_name):
        Redis(connection_pool=self._redis_pool).incr(id_auto_inc_name)
        return Redis(connection_pool=self._redis_pool).get(id_auto_inc_name)
