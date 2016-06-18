# -*- encoding: utf-8 -*-
'''
__author__ = "Larry_Pavanery
'''

from surl.helpers.constants import API_VERSION
import unittest


class TestConstants(unittest.TestCase):

    def test_api_version(self):
        self.assertEqual(API_VERSION, 'api_v1')

