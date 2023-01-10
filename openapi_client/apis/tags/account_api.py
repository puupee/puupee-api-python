# coding: utf-8

"""
    Puupee API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""

from openapi_client.paths.api_account_register.post import ApiAccountRegisterPost
from openapi_client.paths.api_account_reset_password.post import ApiAccountResetPasswordPost
from openapi_client.paths.api_account_send_password_reset_code.post import ApiAccountSendPasswordResetCodePost
from openapi_client.paths.api_account_verify_password_reset_token.post import ApiAccountVerifyPasswordResetTokenPost


class AccountApi(
    ApiAccountRegisterPost,
    ApiAccountResetPasswordPost,
    ApiAccountSendPasswordResetCodePost,
    ApiAccountVerifyPasswordResetTokenPost,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
