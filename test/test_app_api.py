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
from puupee-api.api.app_api import AppApi  # noqa: E501
from puupee-api.rest import ApiException


class TestAppApi(unittest.TestCase):
    """AppApi unit test stubs"""

    def setUp(self):
        self.api = puupee-api.api.app_api.AppApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_app_app_by_developer_all_get(self):
        """Test case for api_app_app_by_developer_all_get

        """
        pass

    def test_api_app_app_by_name_get(self):
        """Test case for api_app_app_by_name_get

        """
        pass

    def test_api_app_app_get(self):
        """Test case for api_app_app_get

        """
        pass

    def test_api_app_app_id_delete(self):
        """Test case for api_app_app_id_delete

        """
        pass

    def test_api_app_app_id_get(self):
        """Test case for api_app_app_id_get

        """
        pass

    def test_api_app_app_id_put(self):
        """Test case for api_app_app_id_put

        """
        pass

    def test_api_app_app_id_run_state_put(self):
        """Test case for api_app_app_id_run_state_put

        """
        pass

    def test_api_app_app_id_with_user_get(self):
        """Test case for api_app_app_id_with_user_get

        """
        pass

    def test_api_app_app_post(self):
        """Test case for api_app_app_post

        """
        pass

    def test_api_app_app_public_get(self):
        """Test case for api_app_app_public_get

        """
        pass

    def test_api_app_app_run_post(self):
        """Test case for api_app_app_run_post

        """
        pass

    def test_api_app_app_upload_credentials_get(self):
        """Test case for api_app_app_upload_credentials_get

        """
        pass

    def test_api_app_app_with_user_get(self):
        """Test case for api_app_app_with_user_get

        """
        pass


if __name__ == '__main__':
    unittest.main()