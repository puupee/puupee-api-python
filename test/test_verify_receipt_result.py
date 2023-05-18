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
from puupee-api.models.verify_receipt_result import VerifyReceiptResult  # noqa: E501
from puupee-api.rest import ApiException

class TestVerifyReceiptResult(unittest.TestCase):
    """VerifyReceiptResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test VerifyReceiptResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = puupee-api.models.verify_receipt_result.VerifyReceiptResult()  # noqa: E501
        if include_optional :
            return VerifyReceiptResult(
                id = '', 
                creation_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                creator_id = '', 
                last_modification_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                last_modifier_id = '', 
                is_deleted = True, 
                deleter_id = '', 
                deletion_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                deleter = puupee-api.models.identity_user.IdentityUser(
                    id = '', 
                    extra_properties = {
                        'key' : null
                        }, 
                    concurrency_stamp = '', 
                    creation_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    creator_id = '', 
                    last_modification_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    last_modifier_id = '', 
                    is_deleted = True, 
                    deleter_id = '', 
                    deletion_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    tenant_id = '', 
                    user_name = '', 
                    normalized_user_name = '', 
                    name = '', 
                    surname = '', 
                    email = '', 
                    normalized_email = '', 
                    email_confirmed = True, 
                    password_hash = '', 
                    security_stamp = '', 
                    is_external = True, 
                    phone_number = '', 
                    phone_number_confirmed = True, 
                    is_active = True, 
                    two_factor_enabled = True, 
                    lockout_end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    lockout_enabled = True, 
                    access_failed_count = 56, 
                    should_change_password_on_next_login = True, 
                    entity_version = 56, 
                    last_password_change_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    roles = [
                        puupee-api.models.identity_user_role.IdentityUserRole(
                            tenant_id = '', 
                            user_id = '', 
                            role_id = '', )
                        ], 
                    claims = [
                        puupee-api.models.identity_user_claim.IdentityUserClaim(
                            id = '', 
                            tenant_id = '', 
                            claim_type = '', 
                            claim_value = '', 
                            user_id = '', )
                        ], 
                    logins = [
                        puupee-api.models.identity_user_login.IdentityUserLogin(
                            tenant_id = '', 
                            user_id = '', 
                            login_provider = '', 
                            provider_key = '', 
                            provider_display_name = '', )
                        ], 
                    tokens = [
                        puupee-api.models.identity_user_token.IdentityUserToken(
                            tenant_id = '', 
                            user_id = '', 
                            login_provider = '', 
                            name = '', 
                            value = '', )
                        ], 
                    organization_units = [
                        puupee-api.models.identity_user_organization_unit.IdentityUserOrganizationUnit(
                            creation_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            creator_id = '', 
                            tenant_id = '', 
                            user_id = '', 
                            organization_unit_id = '', )
                        ], ), 
                creator = puupee-api.models.identity_user.IdentityUser(
                    id = '', 
                    extra_properties = {
                        'key' : null
                        }, 
                    concurrency_stamp = '', 
                    creation_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    creator_id = '', 
                    last_modification_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    last_modifier_id = '', 
                    is_deleted = True, 
                    deleter_id = '', 
                    deletion_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    tenant_id = '', 
                    user_name = '', 
                    normalized_user_name = '', 
                    name = '', 
                    surname = '', 
                    email = '', 
                    normalized_email = '', 
                    email_confirmed = True, 
                    password_hash = '', 
                    security_stamp = '', 
                    is_external = True, 
                    phone_number = '', 
                    phone_number_confirmed = True, 
                    is_active = True, 
                    two_factor_enabled = True, 
                    lockout_end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    lockout_enabled = True, 
                    access_failed_count = 56, 
                    should_change_password_on_next_login = True, 
                    entity_version = 56, 
                    last_password_change_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    roles = [
                        puupee-api.models.identity_user_role.IdentityUserRole(
                            tenant_id = '', 
                            user_id = '', 
                            role_id = '', )
                        ], 
                    claims = [
                        puupee-api.models.identity_user_claim.IdentityUserClaim(
                            id = '', 
                            tenant_id = '', 
                            claim_type = '', 
                            claim_value = '', 
                            user_id = '', )
                        ], 
                    logins = [
                        puupee-api.models.identity_user_login.IdentityUserLogin(
                            tenant_id = '', 
                            user_id = '', 
                            login_provider = '', 
                            provider_key = '', 
                            provider_display_name = '', )
                        ], 
                    tokens = [
                        puupee-api.models.identity_user_token.IdentityUserToken(
                            tenant_id = '', 
                            user_id = '', 
                            login_provider = '', 
                            name = '', 
                            value = '', )
                        ], 
                    organization_units = [
                        puupee-api.models.identity_user_organization_unit.IdentityUserOrganizationUnit(
                            creation_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            creator_id = '', 
                            tenant_id = '', 
                            user_id = '', 
                            organization_unit_id = '', )
                        ], ), 
                last_modifier = puupee-api.models.identity_user.IdentityUser(
                    id = '', 
                    extra_properties = {
                        'key' : null
                        }, 
                    concurrency_stamp = '', 
                    creation_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    creator_id = '', 
                    last_modification_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    last_modifier_id = '', 
                    is_deleted = True, 
                    deleter_id = '', 
                    deletion_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    tenant_id = '', 
                    user_name = '', 
                    normalized_user_name = '', 
                    name = '', 
                    surname = '', 
                    email = '', 
                    normalized_email = '', 
                    email_confirmed = True, 
                    password_hash = '', 
                    security_stamp = '', 
                    is_external = True, 
                    phone_number = '', 
                    phone_number_confirmed = True, 
                    is_active = True, 
                    two_factor_enabled = True, 
                    lockout_end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    lockout_enabled = True, 
                    access_failed_count = 56, 
                    should_change_password_on_next_login = True, 
                    entity_version = 56, 
                    last_password_change_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    roles = [
                        puupee-api.models.identity_user_role.IdentityUserRole(
                            tenant_id = '', 
                            user_id = '', 
                            role_id = '', )
                        ], 
                    claims = [
                        puupee-api.models.identity_user_claim.IdentityUserClaim(
                            id = '', 
                            tenant_id = '', 
                            claim_type = '', 
                            claim_value = '', 
                            user_id = '', )
                        ], 
                    logins = [
                        puupee-api.models.identity_user_login.IdentityUserLogin(
                            tenant_id = '', 
                            user_id = '', 
                            login_provider = '', 
                            provider_key = '', 
                            provider_display_name = '', )
                        ], 
                    tokens = [
                        puupee-api.models.identity_user_token.IdentityUserToken(
                            tenant_id = '', 
                            user_id = '', 
                            login_provider = '', 
                            name = '', 
                            value = '', )
                        ], 
                    organization_units = [
                        puupee-api.models.identity_user_organization_unit.IdentityUserOrganizationUnit(
                            creation_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            creator_id = '', 
                            tenant_id = '', 
                            user_id = '', 
                            organization_unit_id = '', )
                        ], ), 
                order_id = '', 
                receipt_data = '', 
                platform = '', 
                device_token = '', 
                ok = True, 
                status_code = '', 
                message = '', 
                result_data = '', 
                record_id = '', 
                apple_verify_receipt_result = puupee-api.models.apple_verify_receipt_result.AppleVerifyReceiptResult(
                    environment = '', 
                    is_retryable = True, 
                    status = puupee-api.models.apple_verify_recceipt_status.AppleVerifyRecceiptStatus(
                        name = '', 
                        value = 56, ), 
                    latest_receipt_info = [
                        puupee-api.models.latest_receipt_info.LatestReceiptInfo(
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
                            is_in_intro_offer_period = '', )
                        ], 
                    latest_receipt = '', 
                    pending_renewal_info = [
                        puupee-api.models.pending_renewal_info.PendingRenewalInfo(
                            auto_renew_product_id = '', 
                            auto_renew_status = '', 
                            is_in_billing_retry_period = '', 
                            original_transaction_id = '', 
                            product_id = '', 
                            expiration_intent = '', 
                            price_consent_status = '', 
                            grace_period_expires_date = '', 
                            grace_period_expires_date_ms = '', 
                            grace_period_expires_date_pst = '', )
                        ], 
                    receipt = puupee-api.models.receipt.Receipt(
                        receipt_type = '', 
                        adam_id = 56, 
                        app_item_id = 56, 
                        bundle_id = '', 
                        application_version = '', 
                        download_id = 56, 
                        version_external_identifier = 56, 
                        receipt_creation_date = '', 
                        receipt_creation_date_ms = '', 
                        receipt_creation_date_pst = '', 
                        request_date = '', 
                        request_date_ms = '', 
                        request_date_pst = '', 
                        original_purchase_date = '', 
                        original_purchase_date_ms = '', 
                        original_purchase_date_pst = '', 
                        original_application_version = '', 
                        in_app = [
                            puupee-api.models.in_app.InApp(
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
                                is_in_intro_offer_period = '', )
                            ], ), )
            )
        else :
            return VerifyReceiptResult(
        )

    def testVerifyReceiptResult(self):
        """Test VerifyReceiptResult"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()