# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import puupee-api
from puupee-api.paths.api_app_storage_object_pre_sign_url import post  # noqa: E501
from puupee-api import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApiAppStorageObjectPreSignUrl(ApiTestMixin, unittest.TestCase):
    """
    ApiAppStorageObjectPreSignUrl unit test stubs
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200








if __name__ == '__main__':
    unittest.main()
