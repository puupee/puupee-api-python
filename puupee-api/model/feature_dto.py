# coding: utf-8

"""
    Puupee API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from puupee-api import schemas  # noqa: F401


class FeatureDto(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            name = schemas.StrSchema
            displayName = schemas.StrSchema
            value = schemas.StrSchema
        
            @staticmethod
            def provider() -> typing.Type['FeatureProviderDto']:
                return FeatureProviderDto
            description = schemas.StrSchema
        
            @staticmethod
            def valueType() -> typing.Type['IStringValueType']:
                return IStringValueType
            depth = schemas.Int32Schema
            parentName = schemas.StrSchema
            __annotations__ = {
                "name": name,
                "displayName": displayName,
                "value": value,
                "provider": provider,
                "description": description,
                "valueType": valueType,
                "depth": depth,
                "parentName": parentName,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["displayName"]) -> MetaOapg.properties.displayName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["provider"]) -> 'FeatureProviderDto': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["valueType"]) -> 'IStringValueType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["depth"]) -> MetaOapg.properties.depth: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parentName"]) -> MetaOapg.properties.parentName: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "displayName", "value", "provider", "description", "valueType", "depth", "parentName", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["displayName"]) -> typing.Union[MetaOapg.properties.displayName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> typing.Union[MetaOapg.properties.value, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["provider"]) -> typing.Union['FeatureProviderDto', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["valueType"]) -> typing.Union['IStringValueType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["depth"]) -> typing.Union[MetaOapg.properties.depth, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parentName"]) -> typing.Union[MetaOapg.properties.parentName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "displayName", "value", "provider", "description", "valueType", "depth", "parentName", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        displayName: typing.Union[MetaOapg.properties.displayName, str, schemas.Unset] = schemas.unset,
        value: typing.Union[MetaOapg.properties.value, str, schemas.Unset] = schemas.unset,
        provider: typing.Union['FeatureProviderDto', schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        valueType: typing.Union['IStringValueType', schemas.Unset] = schemas.unset,
        depth: typing.Union[MetaOapg.properties.depth, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        parentName: typing.Union[MetaOapg.properties.parentName, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FeatureDto':
        return super().__new__(
            cls,
            *args,
            name=name,
            displayName=displayName,
            value=value,
            provider=provider,
            description=description,
            valueType=valueType,
            depth=depth,
            parentName=parentName,
            _configuration=_configuration,
            **kwargs,
        )

from puupee-api.model.feature_provider_dto import FeatureProviderDto
from puupee-api.model.i_string_value_type import IStringValueType
