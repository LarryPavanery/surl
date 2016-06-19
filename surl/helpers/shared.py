# -*- encoding: utf-8 -*-
'''
__author__ = "Larry_Pavanery
'''

from constants import UNIVERSE_COMBINATIONS
from ConfigParser import RawConfigParser
from constants import API_VERSION
from datetime import datetime
from faker import Factory
from time import time


import pytz
import ujson as json


def shorturl(id_url):
    return '%s%s' % (root_url(), id_url)


def get_index_id_url(indexs):
    length = length_id_url()
    for i in range(length):
        index = indexs[i]
        if index < len(UNIVERSE_COMBINATIONS) - 1:
            indexs[i] += 1
            return indexs
        indexs[i] = 0
        continue
    else:
        '''full combination'''
        return [-1 for i in range(length)]


def root_url():
    ini = load_env()
    root = 'http://%s' % (ini['host'])
    if ini['port']:
        root += ':%s/' % (ini['port'])
    return root


def load_configs():
    configs = RawConfigParser()
    configs.read('etc/api-config.conf')
    return configs


def load_ini():
    configs = RawConfigParser()
    configs.read('etc/api-config.ini')
    return configs


def load_env():
    return dict(load_ini().items('server:main'))


def load_references():
    configs = load_configs()
    references = {}

    for api_name, api_reference in configs.items('dispatcher'):
        if API_VERSION in api_name:
            references[api_name] = api_reference
    return references


def load_redis_config():
    return dict(load_configs().items('redis-server'))


def log_enable():
    configs = load_configs()
    return configs.get('DEFAULT', 'debug').lower() == 'true'


def length_id_url():
    configs = load_configs()
    return int(configs.get('DEFAULT', 'length_id_url'))


def size_top_urls():
    configs = load_configs()
    return int(configs.get('DEFAULT', 'size_top_urls'))


def encode_obj(obj):
    return json.dumps(obj, ensure_ascii=False).encode('utf8')


def decode_obj(obj):
    return json.loads(obj)


def timestamp():
    return datetime.fromtimestamp(time(), tz=pytz.utc).strftime('%Y-%m-%dT%H:%M:%S.%fZ')


def fake_name():
    fake = Factory.create('en_US')
    return fake.name()


def fake_url():
    fake = Factory.create('en_US')
    return 'http://www.%s' % (fake.email().replace('@', '.'))
