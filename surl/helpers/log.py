# -*- encoding: utf-8 -*-
'''
__author__ = "Larry_Pavanery
'''

from datetime import datetime as dt
import surl.helpers.shared as util


class Log(object):
    def __init__(self, class_name):
        self.log_enable = util.log_enable()
        self.class_name = class_name

    def _print(self, level, content):
        if self.log_enable:
            print('[!][{}] [{}] {} - {}'.format(dt.now(), self.class_name.upper(), level, content))

    def info(self, content):
        self._print('INFO', content)

    def warn(self, content):
        self._print('WARN', content)

    def debug(self, content):
        self._print('DEBUG', content)
