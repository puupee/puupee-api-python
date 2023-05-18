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
from puupee-api.models.current_culture_dto import CurrentCultureDto  # noqa: E501
from puupee-api.rest import ApiException

class TestCurrentCultureDto(unittest.TestCase):
    """CurrentCultureDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CurrentCultureDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = puupee-api.models.current_culture_dto.CurrentCultureDto()  # noqa: E501
        if include_optional :
            return CurrentCultureDto(
                display_name = '', 
                english_name = '', 
                three_letter_iso_language_name = '', 
                two_letter_iso_language_name = '', 
                is_right_to_left = True, 
                culture_name = '', 
                name = '', 
                native_name = '', 
                date_time_format = puupee-api.models.date_time_format_dto.DateTimeFormatDto(
                    calendar_algorithm_type = '', 
                    date_time_format_long = '', 
                    short_date_pattern = '', 
                    full_date_time_pattern = '', 
                    date_separator = '', 
                    short_time_pattern = '', 
                    long_time_pattern = '', )
            )
        else :
            return CurrentCultureDto(
        )

    def testCurrentCultureDto(self):
        """Test CurrentCultureDto"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
