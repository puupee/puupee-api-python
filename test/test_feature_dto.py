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
from puupee-api.models.feature_dto import FeatureDto  # noqa: E501
from puupee-api.rest import ApiException

class TestFeatureDto(unittest.TestCase):
    """FeatureDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FeatureDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = puupee-api.models.feature_dto.FeatureDto()  # noqa: E501
        if include_optional :
            return FeatureDto(
                name = '', 
                display_name = '', 
                value = '', 
                provider = puupee-api.models.feature_provider_dto.FeatureProviderDto(
                    name = '', 
                    key = '', ), 
                description = '', 
                value_type = puupee-api.models.i_string_value_type.IStringValueType(
                    name = '', 
                    properties = {
                        'key' : null
                        }, 
                    validator = puupee-api.models.i_value_validator.IValueValidator(
                        name = '', ), ), 
                depth = 56, 
                parent_name = ''
            )
        else :
            return FeatureDto(
        )

    def testFeatureDto(self):
        """Test FeatureDto"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
