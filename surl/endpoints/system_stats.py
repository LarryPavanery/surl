# -*- encoding: utf-8 -*-
'''
__author__ = "Larry_Pavanery
'''

from base_response import BaseResponse
from surl.database.url_db import URLDB
from surl.helpers.shared import size_top_urls
import falcon


class SystemStats(BaseResponse):

    def __init__(self):
        super(SystemStats, self).__init__()
        self.url_db = URLDB()

    def on_get(self, req, resp):
        """ GET /stats """
        self.process_stats(resp)

    def process_stats(self, resp):
        sz_top = size_top_urls()
        self.return_body(
            resp,
            {
                'hits': self.calc_hits_sum(),
                'urlCount': self.url_db.count(),
                'topUrls': self.url_db.list_sort_by_hits_desc(sz_top)
            },
            falcon.HTTP_200
        )

    def calc_hits_sum(self):
        hits_sum = 0
        for url in self.url_db.values():
            hits_sum += int(url['hits'])
        return hits_sum
