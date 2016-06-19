# -*- encoding: utf-8 -*-
'''
__author__ = "Larry_Pavanery
'''

import falcon
import surl.helpers.shared as utils

from base_response import BaseResponse
from surl.database.url_db import URLDB
from surl.database.user_db import UserDB


class ManagerURL(BaseResponse):
    def __init__(self):
        super(ManagerURL, self).__init__()
        self.user_db = UserDB()
        self.url_db = URLDB()

    def on_get(self, req, resp, id):
        """ GET /urls/:id """
        resp.set_header('Content-Type', 'text/html')

        url = self.url_db.get(id)
        if url:
            self.url_db.increment_hits(id)
            resp.status = falcon.HTTP_301
            resp.set_header('Location', url['url'])
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

        if not self.user_db.exists(user_id):
            raise falcon.HTTPError(
                falcon.HTTP_404,
                'User not found',
                'Request did not return any records'
            )

        if 'url' not in data:
            raise falcon.HTTPError(
                falcon.HTTP_400,
                'No identifier',
                'Could not decode the request body. The JSON was incorrect'
            )

        url = data['url']
        id_url = self.url_db.create_id_url()
        if self.user_db.user_has_url(user_id, id_url):
            raise falcon.HTTPError(
                falcon.HTTP_409,
                'The URL exists to the user',
                'Please try with another URL'
            )

        new_url = self.url_db.save(url, id_url)
        self.user_db.update_user(user_id, id_url)
        self.return_body(resp, new_url, falcon.HTTP_201)

    def _delete(self, resp, url_id):
        if not self.url_db.exists(url_id):
            raise falcon.HTTPError(
                falcon.HTTP_404,
                'Short URL not found',
                'Request did not return any records'
            )
        self.url_db.delete(url_id)
