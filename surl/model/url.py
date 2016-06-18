# -*- encoding: utf-8 -*-
'''
__author__ = "Larry_Pavanery
'''


class URL(object):
    def __init__(self, id, url, shorturl):
        self.id = id
        self.hits = 0
        self.url = url
        self.shorturl = shorturl
