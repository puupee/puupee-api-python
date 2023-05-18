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
from puupee-api.models.application_api_description_model import ApplicationApiDescriptionModel  # noqa: E501
from puupee-api.rest import ApiException

class TestApplicationApiDescriptionModel(unittest.TestCase):
    """ApplicationApiDescriptionModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ApplicationApiDescriptionModel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = puupee-api.models.application_api_description_model.ApplicationApiDescriptionModel()  # noqa: E501
        if include_optional :
            return ApplicationApiDescriptionModel(
                modules = {
                    'key' : puupee-api.models.module_api_description_model.ModuleApiDescriptionModel(
                        root_path = '', 
                        remote_service_name = '', 
                        controllers = {
                            'key' : puupee-api.models.controller_api_description_model.ControllerApiDescriptionModel(
                                controller_name = '', 
                                controller_group_name = '', 
                                is_remote_service = True, 
                                is_integration_service = True, 
                                api_version = '', 
                                type = '', 
                                interfaces = [
                                    puupee-api.models.controller_interface_api_description_model.ControllerInterfaceApiDescriptionModel(
                                        type = '', 
                                        name = '', 
                                        methods = [
                                            puupee-api.models.interface_method_api_description_model.InterfaceMethodApiDescriptionModel(
                                                name = '', 
                                                parameters_on_method = [
                                                    puupee-api.models.method_parameter_api_description_model.MethodParameterApiDescriptionModel(
                                                        name = '', 
                                                        type_as_string = '', 
                                                        type = '', 
                                                        type_simple = '', 
                                                        is_optional = True, 
                                                        default_value = null, )
                                                    ], 
                                                return_value = puupee-api.models.return_value_api_description_model.ReturnValueApiDescriptionModel(
                                                    type = '', 
                                                    type_simple = '', ), )
                                            ], )
                                    ], 
                                actions = {
                                    'key' : puupee-api.models.action_api_description_model.ActionApiDescriptionModel(
                                        unique_name = '', 
                                        name = '', 
                                        http_method = '', 
                                        url = '', 
                                        supported_versions = [
                                            ''
                                            ], 
                                        parameters = [
                                            puupee-api.models.parameter_api_description_model.ParameterApiDescriptionModel(
                                                name_on_method = '', 
                                                name = '', 
                                                json_name = '', 
                                                type = '', 
                                                type_simple = '', 
                                                is_optional = True, 
                                                default_value = null, 
                                                constraint_types = [
                                                    ''
                                                    ], 
                                                binding_source_id = '', 
                                                descriptor_name = '', )
                                            ], 
                                        allow_anonymous = True, 
                                        implement_from = '', )
                                    }, )
                            }, )
                    }, 
                types = {
                    'key' : puupee-api.models.type_api_description_model.TypeApiDescriptionModel(
                        base_type = '', 
                        is_enum = True, 
                        enum_names = [
                            ''
                            ], 
                        enum_values = [
                            null
                            ], 
                        generic_arguments = [
                            ''
                            ], 
                        properties = [
                            puupee-api.models.property_api_description_model.PropertyApiDescriptionModel(
                                name = '', 
                                json_name = '', 
                                type = '', 
                                type_simple = '', 
                                is_required = True, 
                                min_length = 56, 
                                max_length = 56, 
                                minimum = '', 
                                maximum = '', 
                                regex = '', )
                            ], )
                    }
            )
        else :
            return ApplicationApiDescriptionModel(
        )

    def testApplicationApiDescriptionModel(self):
        """Test ApplicationApiDescriptionModel"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
