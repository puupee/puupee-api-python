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
from puupee-api.models.in_app import InApp  # noqa: E501
from puupee-api.rest import ApiException

class TestInApp(unittest.TestCase):
    """InApp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InApp
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = puupee-api.models.in_app.InApp()  # noqa: E501
        if include_optional :
            return InApp(
                quantity = '', 
                product_id = '', 
                transaction_id = '', 
                original_transaction_id = '', 
                purchase_date = '', 
                purchase_date_ms = '', 
                purchase_date_pst = '', 
                original_purchase_date = '', 
                original_purchase_date_ms = '', 
                original_purchase_date_pst = '', 
                expires_date = '', 
                expires_date_ms = '', 
                expires_date_pst = '', 
                web_order_line_item_id = '', 
                is_trial_period = '', 
                is_in_intro_offer_period = ''
            )
        else :
            return InApp(
        )

    def testInApp(self):
        """Test InApp"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
