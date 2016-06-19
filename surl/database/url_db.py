# -*- encoding: utf-8 -*-
'''
__author__ = "Larry_Pavanery
'''

from abstract_redis_database import AbstractRedisdb
from surl.model.url import URL

from surl.helpers.shared import get_index_id_url
from surl.helpers.shared import length_id_url
from surl.helpers.shared import root_url

from surl.helpers.constants import UNIVERSE_COMBINATIONS
from surl.helpers.constants import KEY_HASH_INDEXS
from surl.helpers.constants import INDEX_HASH
from surl.helpers.constants import URL_HASH


class URLDB(AbstractRedisdb):

    def __init__(self):
        super(URLDB, self).__init__()
        self.id_auto_inc_name = 'id_url_auto_increment'
        self.hash_name = URL_HASH

    def get(self, id_url):
        return super(URLDB, self).get(
            self.hash_name,
            id_url
        )

    def save(self, url, id_url):
        id = self.next_id(self.id_auto_inc_name)
        shorturl = '%s%s' % (root_url(), id_url)
        return super(URLDB, self).save(
            self.hash_name,
            id_url,
            URL(id, url, shorturl)
        )

    def increment_hits(self, id_url):
        url = self.get(id_url)
        update_hits = URL(
            url['id'],
            url['url'],
            url['shorturl'],
            url['hits']
        )
        update_hits.increment_hits()
        return super(URLDB, self).save(
            self.hash_name,
            id_url,
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

    def create_id_url(self):
        return ''.join([
            UNIVERSE_COMBINATIONS[index]
            for index in self._create_id_url()
        ])

    def _create_id_url(self):
        indexs = super(URLDB, self).get(
            INDEX_HASH,
            KEY_HASH_INDEXS,
        )

        if indexs:
            new_indexs = get_index_id_url(indexs)
        else:
            new_indexs = [0 for i in range(length_id_url())]

        super(URLDB, self).save(
            INDEX_HASH,
            KEY_HASH_INDEXS,
            new_indexs
        )

        return new_indexs
