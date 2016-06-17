# -*- encoding: utf-8 -*-
'''
__author__ = "Larry_Pavanery
'''

import falcon
import surl.helpers.shared as utils

from base_response import BaseResponse
from surl.database.url_db import URLDB

class ManagerURL(BaseResponse):
    def __init__(self):
        super(ManagerURL, self).__init__()
        self.db = URLDB()
        
    def on_get(self, req, resp, id):
        """ GET /urls/:id """
        resp.set_header('Content-Type', 'text/html')
        
        url = self.db.get(id)
        if url:
            resp.status = falcon.HTTP_301
            resp.set_header('Location', url.url)
        else:
            resp.status = falcon.HTTP_404

    def on_post(self, req, resp, userId):
        """ POST /users/:userid/urls """
        self._save(resp, req, userId)

    def on_delete(self, req, resp, id):
        """ DELETE /urls/:id """
        self._delete(resp, id)
        
    def _save(self, resp, req, user_id):
        data = utils.decode_obj(req.stream.read())

        if 'url' in data:
            url = data['url']
            shorturl = utils.shorturl(url)
            if not self.db.exists(shorturl):
                new_url = self.db.create(1, url, shorturl)
                if new_url:
                    self.return_body(resp, new_url, falcon.HTTP_201)
                else:
                    raise falcon.HTTPError(falcon.HTTP_400, 'Short URL not created',
                                    'Please try again or contact support')
            else:
                resp.status = falcon.HTTP_409
        else:
            raise falcon.HTTPError(falcon.HTTP_400, 'No identifier',
                            'Could not decode the request body. The JSON was incorrect')

    def _delete(self, resp, url_id):
        id = utils.root_url() + url_id
        if self.db.exists(id):
            self.db.delete(id)
        else:
            raise falcon.HTTPError(falcon.HTTP_404, 'Short URL not found', 'Request did not return any records')