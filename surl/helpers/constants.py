# -*- encoding: utf-8 -*-
'''
__author__ = "Larry_Pavanery
'''

import string

API_VERSION = 'api_v1'

USER_HASH = 'USER#'

URL_HASH = 'URL#'

INDEX_HASH = 'INDEXS#'

KEY_HASH_INDEXS = 'COMBINATIONS_ID'

UNIVERSE_COMBINATIONS = '%s%s%s' % (
    string.ascii_lowercase,
    string.ascii_uppercase,
    string.digits
)
