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
from puupee-api.api.email_settings_api import EmailSettingsApi  # noqa: E501
from puupee-api.rest import ApiException


class TestEmailSettingsApi(unittest.TestCase):
    """EmailSettingsApi unit test stubs"""

    def setUp(self):
        self.api = puupee-api.api.email_settings_api.EmailSettingsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_setting_management_emailing_get(self):
        """Test case for api_setting_management_emailing_get

        """
        pass

    def test_api_setting_management_emailing_post(self):
        """Test case for api_setting_management_emailing_post

        """
        pass

    def test_api_setting_management_emailing_send_test_email_post(self):
        """Test case for api_setting_management_emailing_send_test_email_post

        """
        pass


if __name__ == '__main__':
    unittest.main()
