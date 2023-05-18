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
from puupee-api.models.create_or_update_app_dto import CreateOrUpdateAppDto  # noqa: E501
from puupee-api.rest import ApiException

class TestCreateOrUpdateAppDto(unittest.TestCase):
    """CreateOrUpdateAppDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateOrUpdateAppDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = puupee-api.models.create_or_update_app_dto.CreateOrUpdateAppDto()  # noqa: E501
        if include_optional :
            return CreateOrUpdateAppDto(
                name = '', 
                display_name = '', 
                framework = '', 
                app_type = '', 
                description = '', 
                icon = '', 
                home_page = '', 
                sort_index = 56, 
                git_repository = '', 
                git_repository_type = '', 
                is_enabled = True, 
                webhook_url = '', 
                business_domain = '', 
                business_url = '', 
                subscription_platforms = '', 
                free_platforms = '', 
                spec_json_schema = '', 
                default_storage_size = 56, 
                default_single_file_max_size = 56, 
                is_published = True, 
                features = [
                    puupee-api.models.app_feature_dto.AppFeatureDto(
                        id = '', 
                        creation_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        creator_id = '', 
                        last_modification_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        last_modifier_id = '', 
                        is_deleted = True, 
                        deleter_id = '', 
                        deletion_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        name = '', 
                        display_name = '', 
                        description = '', 
                        details = '', 
                        screenshot_keys = '', )
                    ], 
                sdks = [
                    puupee-api.models.app_sdk_dto.AppSdkDto(
                        id = '', 
                        creation_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        creator_id = '', 
                        last_modification_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        last_modifier_id = '', 
                        is_deleted = True, 
                        deleter_id = '', 
                        deletion_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        name = '', 
                        description = '', 
                        privacy = '', 
                        privacy_url = '', 
                        home_page = '', )
                    ], 
                open_client = puupee-api.models.create_open_iddict_application_dto.CreateOpenIddictApplicationDto(
                    type = '', 
                    display_name = '', 
                    display_names = '', 
                    permissions = [
                        ''
                        ], 
                    post_logout_redirect_uris = '', 
                    properties = '', 
                    redirect_uris = '', 
                    requirements = '', 
                    client_uri = '', 
                    logo_uri = '', 
                    grant_types = [
                        ''
                        ], 
                    scopes = [
                        ''
                        ], )
            )
        else :
            return CreateOrUpdateAppDto(
        )

    def testCreateOrUpdateAppDto(self):
        """Test CreateOrUpdateAppDto"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()