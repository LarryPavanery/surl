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

    def __repr__(self):
        return '{\'id\': %s, \'hits\': %s, \'url\': %s, \'shorturl\': %s}' % (self.id, self.hits, self.url, self.shorturl)
