# coding: utf-8

"""
    Puupee API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0.0
    Generated by: https://openapi-generator.tech
"""

from puupee-api.paths.api_app_app_pricing_item.get import ApiAppAppPricingItemGet
from puupee-api.paths.api_app_app_pricing_item_id.delete import ApiAppAppPricingItemIdDelete
from puupee-api.paths.api_app_app_pricing_item_id.get import ApiAppAppPricingItemIdGet
from puupee-api.paths.api_app_app_pricing_item_id.put import ApiAppAppPricingItemIdPut
from puupee-api.paths.api_app_app_pricing_item.post import ApiAppAppPricingItemPost


class AppPricingItemApi(
    ApiAppAppPricingItemGet,
    ApiAppAppPricingItemIdDelete,
    ApiAppAppPricingItemIdGet,
    ApiAppAppPricingItemIdPut,
    ApiAppAppPricingItemPost,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
