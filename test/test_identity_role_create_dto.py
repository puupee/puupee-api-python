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
from puupee-api.models.identity_role_create_dto import IdentityRoleCreateDto  # noqa: E501
from puupee-api.rest import ApiException

class TestIdentityRoleCreateDto(unittest.TestCase):
    """IdentityRoleCreateDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IdentityRoleCreateDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = puupee-api.models.identity_role_create_dto.IdentityRoleCreateDto()  # noqa: E501
        if include_optional :
            return IdentityRoleCreateDto(
                extra_properties = {
                    'key' : null
                    }, 
                name = '', 
                is_default = True, 
                is_public = True
            )
        else :
            return IdentityRoleCreateDto(
                name = '',
        )

    def testIdentityRoleCreateDto(self):
        """Test IdentityRoleCreateDto"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
