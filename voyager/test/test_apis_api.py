# coding: utf-8

"""
    Voyager

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v6.0.0
    Contact: hello@appscode.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import client
from client.rest import ApiException
from client.apis.apis_api import ApisApi


class TestApisApi(unittest.TestCase):
    """ ApisApi unit test stubs """

    def setUp(self):
        self.api = client.apis.apis_api.ApisApi()

    def tearDown(self):
        pass

    def test_get_api_versions(self):
        """
        Test case for get_api_versions

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
