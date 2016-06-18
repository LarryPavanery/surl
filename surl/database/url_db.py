# -*- encoding: utf-8 -*-
'''
__author__ = "Larry_Pavanery
'''

from abstract_redis_database import AbstractRedisdb
from surl.model.url import URL
from surl.helpers.shared import root_url


class URLDB(AbstractRedisdb):

    def __init__(self):
        super(URLDB, self).__init__()
        self.id_auto_inc_name = 'id_url_auto_increment'

    def get(self, id):
        key = '%s%s' % (root_url(), id)
        return super(URLDB, self).get(key)

    def save(self, url, shorturl):
        url_id = self.next_id(self.id_auto_inc_name)
        return super(URLDB, self).save(shorturl, URL(url_id, url, shorturl))

    def increment_hits(self, id):
        url = self.get(id)
        update_hits = URL(url['id'], url['url'], url['shorturl'], url['hits'])
        update_hits.increment_hits()
        return super(URLDB, self).save(url['shorturl'], update_hits)
