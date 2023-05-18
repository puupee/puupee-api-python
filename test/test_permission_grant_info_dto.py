# coding: utf-8

"""
    Puupee API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import puupee-api
from puupee-api.models.permission_grant_info_dto import PermissionGrantInfoDto  # noqa: E501
from puupee-api.rest import ApiException

class TestPermissionGrantInfoDto(unittest.TestCase):
    """PermissionGrantInfoDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PermissionGrantInfoDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = puupee-api.models.permission_grant_info_dto.PermissionGrantInfoDto()  # noqa: E501
        if include_optional :
            return PermissionGrantInfoDto(
                name = '', 
                display_name = '', 
                parent_name = '', 
                is_granted = True, 
                allowed_providers = [
                    ''
                    ], 
                granted_providers = [
                    puupee-api.models.provider_info_dto.ProviderInfoDto(
                        provider_name = '', 
                        provider_key = '', )
                    ]
            )
        else :
            return PermissionGrantInfoDto(
        )

    def testPermissionGrantInfoDto(self):
        """Test PermissionGrantInfoDto"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
