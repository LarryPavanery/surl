# -*- encoding: utf-8 -*-
'''
__author__ = "Larry_Pavanery
'''

import surl.helpers.shared as util
import simport


class Routes(object):
    def __init__(self):
        _refs = util.load_references()

        '''base'''
        _base = simport.load(_refs['api_v1_base'])()

        '''managers'''
        _manager_user = simport.load(_refs['api_v1_manager_user'])()
        _manager_url = simport.load(_refs['api_v1_manager_url'])()

        '''statistics'''
        _system_statistics = simport.load(_refs['api_v1_system_statistics'])()
        _user_statistics = simport.load(_refs['api_v1_user_statistics'])()
        _url_statistics = simport.load(_refs['api_v1_url_statistics'])()

        self.map_resources = {
            "/": _base,
            '/users': _manager_user,
            '/user/{userId}': _manager_user,
            '/urls/{id}': _manager_url,
            '/users/{userId}/urls': _manager_url,
            '/stats': _system_statistics,
            '/stats/{id}': _url_statistics,
            '/users/{userId}/stats': _user_statistics
        }

    def get(self):
        return self.map_resources.items()
