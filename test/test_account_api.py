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
from puupee-api.api.account_api import AccountApi  # noqa: E501
from puupee-api.rest import ApiException


class TestAccountApi(unittest.TestCase):
    """AccountApi unit test stubs"""

    def setUp(self):
        self.api = puupee-api.api.account_api.AccountApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_account_register_post(self):
        """Test case for api_account_register_post

        """
        pass

    def test_api_account_reset_password_post(self):
        """Test case for api_account_reset_password_post

        """
        pass

    def test_api_account_send_password_reset_code_post(self):
        """Test case for api_account_send_password_reset_code_post

        """
        pass

    def test_api_account_verify_password_reset_token_post(self):
        """Test case for api_account_verify_password_reset_token_post

        """
        pass

    def test_api_app_account_delete(self):
        """Test case for api_app_account_delete

        """
        pass


if __name__ == '__main__':
    unittest.main()
