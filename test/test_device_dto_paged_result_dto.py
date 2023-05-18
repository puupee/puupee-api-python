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
from puupee-api.models.device_dto_paged_result_dto import DeviceDtoPagedResultDto  # noqa: E501
from puupee-api.rest import ApiException

class TestDeviceDtoPagedResultDto(unittest.TestCase):
    """DeviceDtoPagedResultDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DeviceDtoPagedResultDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = puupee-api.models.device_dto_paged_result_dto.DeviceDtoPagedResultDto()  # noqa: E501
        if include_optional :
            return DeviceDtoPagedResultDto(
                items = [
                    puupee-api.models.device_dto.DeviceDto(
                        id = '', 
                        creation_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        creator_id = '', 
                        last_modification_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        last_modifier_id = '', 
                        is_deleted = True, 
                        deleter_id = '', 
                        deletion_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        token = '', 
                        tpns_token = '', 
                        is_physical_device = True, 
                        name = '', 
                        platform = '', 
                        brand = '', 
                        system_version = '', )
                    ], 
                total_count = 56
            )
        else :
            return DeviceDtoPagedResultDto(
        )

    def testDeviceDtoPagedResultDto(self):
        """Test DeviceDtoPagedResultDto"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
