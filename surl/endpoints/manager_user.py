# -*- encoding: utf-8 -*-
'''
__author__ = "Larry_Pavanery
'''

import falcon
from surl.helpers.shared import decode_obj
from base_response import BaseResponse
from surl.database.user_db import UserDB


class ManagerUser(BaseResponse):
    def __init__(self):
        super(ManagerUser, self).__init__()
        self.db = UserDB()

    def on_post(self, req, resp):
        """ POST /users """
        self._save(resp, req)

    def on_delete(self, req, resp, userId):
        """ DELETE /user/:userId """
        self._delete(resp, userId)

    def _save(self, resp, req):
        data = decode_obj(req.stream.read())

        if 'id' in data:
            user_id = data['id']
            if not self.db.exists(user_id):
                user = self.db.create(user_id)
                if user:
                    self.return_body(resp, user, falcon.HTTP_201)
                else:
                    raise falcon.HTTPError(falcon.HTTP_400, 'User not created',
                                    'Please try again or contact support')
            else:
                resp.status = falcon.HTTP_409
        else:
            raise falcon.HTTPError(falcon.HTTP_400, 'No identifier',
                            'Could not decode the request body. The JSON was incorrect')

    def _delete(self, resp, user_id):
        if self.db.exists(user_id):
            self.db.delete(user_id)
        else:
            raise falcon.HTTPError(falcon.HTTP_404, 'User not found', 'Request did not return any records')
