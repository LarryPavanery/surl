# -*- encoding: utf-8 -*-
'''
__author__ = "Larry_Pavanery
'''

from constants import API_VERSION
from ConfigParser import RawConfigParser
from datetime import datetime
from time import time
from faker import Factory

import base64

import pytz
import ujson as json


def shorturl(url):
    return  root_url() + base64_url(url)

def base64_url(url):
    return base64.b64encode(url[5:15])

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
    print(load_configs())
    return configs.get('DEFAULT', 'debug').lower() == 'true'

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