# -*- encoding: utf-8 -*-
'''
__author__ = "Larry_Pavanery
'''

from base_response import BaseResponse
from surl.database.url_db import URLDB

import falcon


class URLStatistics(BaseResponse):
    def __init__(self):
        super(URLStatistics, self).__init__()
        self.url_db = URLDB()

    def on_get(self, req, resp, id):
        """ GET /stats/:id """

        url = self.url_db.get(id)
        if url:
            self.return_body(resp, url, falcon.HTTP_200)
        else:
            resp.status = falcon.HTTP_404
