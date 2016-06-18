# -*- encoding: utf-8 -*-
'''
__author__ = "Larry_Pavanery
'''

from abstract_redis_database import AbstractRedisdb
from surl.helpers.constants import URL_HASH
from surl.helpers.shared import root_url
from surl.model.url import URL


class URLDB(AbstractRedisdb):

    def __init__(self):
        super(URLDB, self).__init__()
        self.id_auto_inc_name = 'id_url_auto_increment'
        self.hash_name = URL_HASH

    def get(self, id):
        '''TODO: change the key to be just the hash'''
        return super(URLDB, self).get(
            self.hash_name,
            ('%s%s' % (root_url(), id))
        )

    def save(self, url, shorturl):
        url_id = self.next_id(self.id_auto_inc_name)
        return super(URLDB, self).save(
            self.hash_name,
            shorturl,
            URL(url_id, url, shorturl)
        )

    def increment_hits(self, id):
        url = self.get(id)
        update_hits = URL(
            url['id'],
            url['url'],
            url['shorturl'],
            url['hits']
        )
        update_hits.increment_hits()
        return super(URLDB, self).save(
            self.hash_name,
            url['shorturl'],
            update_hits
        )

    def keys(self):
        return super(URLDB, self).keys(
            self.hash_name
        )

    def exists(self, user_id):
        return super(URLDB, self).exists(
            self.hash_name,
            user_id
        )

    def values(self):
        return [
            super(URLDB, self).get(self.hash_name, key)
            for key in self.keys()
        ]

    def count(self):
        return len(self.keys())

    def list_sort_by_hits_desc(self, top=10):
        urls = self.values()
        shd = sorted(
            urls,
            key=lambda url: int(url['hits']),
            reverse=True
        )
        return shd[0:top]
