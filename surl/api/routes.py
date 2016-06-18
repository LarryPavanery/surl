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

        '''stats'''
        _system_stats = simport.load(_refs['api_v1_system_stats'])()
        _user_stats = simport.load(_refs['api_v1_user_stats'])()
        _url_stats = simport.load(_refs['api_v1_url_stats'])()

        self.map_resources = {
            "/": _base,
            '/users': _manager_user,
            '/user/{userId}': _manager_user,
            '/urls/{id}': _manager_url,
            '/users/{userId}/urls': _manager_url,
            '/stats': _system_stats,
            '/stats/{id}': _url_stats,
            '/users/{userId}/stats': _user_stats
        }

    def get(self):
        return self.map_resources.items()
