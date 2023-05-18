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
from puupee-api.models.update_email_settings_dto import UpdateEmailSettingsDto  # noqa: E501
from puupee-api.rest import ApiException

class TestUpdateEmailSettingsDto(unittest.TestCase):
    """UpdateEmailSettingsDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UpdateEmailSettingsDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = puupee-api.models.update_email_settings_dto.UpdateEmailSettingsDto()  # noqa: E501
        if include_optional :
            return UpdateEmailSettingsDto(
                smtp_host = '', 
                smtp_port = 1, 
                smtp_user_name = '', 
                smtp_password = '', 
                smtp_domain = '', 
                smtp_enable_ssl = True, 
                smtp_use_default_credentials = True, 
                default_from_address = '', 
                default_from_display_name = ''
            )
        else :
            return UpdateEmailSettingsDto(
                default_from_address = '',
                default_from_display_name = '',
        )

    def testUpdateEmailSettingsDto(self):
        """Test UpdateEmailSettingsDto"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()