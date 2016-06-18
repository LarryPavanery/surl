# -*- encoding: utf-8 -*-
'''
__author__ = "Larry_Pavanery
'''


class URL(object):
    def __init__(self, id, url, shorturl, hits=0):
        self.id = id
        self.hits = hits
        self.url = url
        self.shorturl = shorturl

    def increment_hits(self):
        self.hits += 1
