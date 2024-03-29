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
from puupee-api.models.message_source_dto import MessageSourceDto  # noqa: E501
from puupee-api.rest import ApiException

class TestMessageSourceDto(unittest.TestCase):
    """MessageSourceDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MessageSourceDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = puupee-api.models.message_source_dto.MessageSourceDto()  # noqa: E501
        if include_optional :
            return MessageSourceDto(
                name = '', 
                description = '', 
                is_published = True, 
                icon_url = '', 
                routes = [
                    puupee-api.models.message_source_route_sub_dto.MessageSourceRouteSubDto(
                        route_id = '', 
                        path = '', 
                        values = null, )
                    ]
            )
        else :
            return MessageSourceDto(
        )

    def testMessageSourceDto(self):
        """Test MessageSourceDto"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
