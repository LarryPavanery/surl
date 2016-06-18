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

    def get(self, hash_name, key):
        if hash_name not in key:
            key = '%s%s' % (hash_name, key)
        value = Redis(connection_pool=self._redis_pool).get(key)
        try:
            return utils.decode_obj(value)
        except:
            return value

    def save(self, hash_name, key, value):
        _key = '%s%s' % (hash_name, key)
        try:
            Redis(connection_pool=self._redis_pool).set(_key, utils.encode_obj(value))
            return value
        except Exception:
            return None

    def delete(self, hash_name, key):
        _key = '%s%s' % (hash_name, key)
        try:
            Redis(connection_pool=self._redis_pool).delete(_key)
            return True
        except:
            return False

    def keys(self, hash_name):
        _key_pattern = '%s*' % (hash_name)
        return Redis(connection_pool=self._redis_pool).keys(_key_pattern)

    def exists(self, hash_name, key):
        _key = '%s%s' % (hash_name, key)
        return Redis(connection_pool=self._redis_pool).exists(_key)

    def next_id(self, id_auto_inc_name):
        Redis(connection_pool=self._redis_pool).incr(id_auto_inc_name)
        return Redis(connection_pool=self._redis_pool).get(id_auto_inc_name)
