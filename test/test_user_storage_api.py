# coding: utf-8

"""
    Puupee API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import puupee-api
from puupee-api.api.user_storage_api import UserStorageApi  # noqa: E501
from puupee-api.rest import ApiException


class TestUserStorageApi(unittest.TestCase):
    """UserStorageApi unit test stubs"""

    def setUp(self):
        self.api = puupee-api.api.user_storage_api.UserStorageApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_app_user_storage_get(self):
        """Test case for api_app_user_storage_get

        """
        pass


if __name__ == '__main__':
    unittest.main()
