# -*- encoding: utf-8 -*-
'''
__author__ = "Larry_Pavanery
'''


class User(object):
    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return '{\'id\': %s}' % (self.id)
