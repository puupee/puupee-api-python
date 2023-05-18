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
from puupee-api.models.app_pricing_dto import AppPricingDto  # noqa: E501
from puupee-api.rest import ApiException

class TestAppPricingDto(unittest.TestCase):
    """AppPricingDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AppPricingDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = puupee-api.models.app_pricing_dto.AppPricingDto()  # noqa: E501
        if include_optional :
            return AppPricingDto(
                id = '', 
                creation_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                creator_id = '', 
                last_modification_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                last_modifier_id = '', 
                is_deleted = True, 
                deleter_id = '', 
                deletion_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                naming = '', 
                month_product_id = '', 
                year_product_id = '', 
                description = '', 
                app_id = '', 
                month_price = 1.337, 
                month_discount = 1.337, 
                month_discount_price = 1.337, 
                month_discount_start_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                month_discount_end_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                year_price = 1.337, 
                year_discount = 1.337, 
                year_discount_price = 1.337, 
                year_discount_start_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                year_discount_end_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                sort_index = 56, 
                items = [
                    puupee-api.models.app_pricing_item_dto.AppPricingItemDto(
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
                        link_url = '', 
                        display = '', 
                        values = [
                            ''
                            ], 
                        app_id = '', 
                        is_available = True, 
                        has_value = True, 
                        sort_index = 56, )
                    ]
            )
        else :
            return AppPricingDto(
        )

    def testAppPricingDto(self):
        """Test AppPricingDto"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()