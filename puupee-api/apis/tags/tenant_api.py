# coding: utf-8

"""
    Puupee API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0.0
    Generated by: https://openapi-generator.tech
"""

from puupee-api.paths.api_multi_tenancy_tenants.get import ApiMultiTenancyTenantsGet
from puupee-api.paths.api_multi_tenancy_tenants_id_default_connection_string.delete import ApiMultiTenancyTenantsIdDefaultConnectionStringDelete
from puupee-api.paths.api_multi_tenancy_tenants_id_default_connection_string.get import ApiMultiTenancyTenantsIdDefaultConnectionStringGet
from puupee-api.paths.api_multi_tenancy_tenants_id_default_connection_string.put import ApiMultiTenancyTenantsIdDefaultConnectionStringPut
from puupee-api.paths.api_multi_tenancy_tenants_id.delete import ApiMultiTenancyTenantsIdDelete
from puupee-api.paths.api_multi_tenancy_tenants_id.get import ApiMultiTenancyTenantsIdGet
from puupee-api.paths.api_multi_tenancy_tenants_id.put import ApiMultiTenancyTenantsIdPut
from puupee-api.paths.api_multi_tenancy_tenants.post import ApiMultiTenancyTenantsPost


class TenantApi(
    ApiMultiTenancyTenantsGet,
    ApiMultiTenancyTenantsIdDefaultConnectionStringDelete,
    ApiMultiTenancyTenantsIdDefaultConnectionStringGet,
    ApiMultiTenancyTenantsIdDefaultConnectionStringPut,
    ApiMultiTenancyTenantsIdDelete,
    ApiMultiTenancyTenantsIdGet,
    ApiMultiTenancyTenantsIdPut,
    ApiMultiTenancyTenantsPost,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
