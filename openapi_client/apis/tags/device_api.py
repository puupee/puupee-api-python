# coding: utf-8

"""
    Puupee API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""

from openapi_client.paths.api_app_device_bind.post import ApiAppDeviceBindPost
from openapi_client.paths.api_app_device.delete import ApiAppDeviceDelete
from openapi_client.paths.api_app_device.get import ApiAppDeviceGet
from openapi_client.paths.api_app_device_refresh.post import ApiAppDeviceRefreshPost


class DeviceApi(
    ApiAppDeviceBindPost,
    ApiAppDeviceDelete,
    ApiAppDeviceGet,
    ApiAppDeviceRefreshPost,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
