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


class CreateOrUpdateAppSdkDto(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            name = schemas.StrSchema
            description = schemas.StrSchema
            privacy = schemas.StrSchema
            privacyUrl = schemas.StrSchema
            homePage = schemas.StrSchema
            __annotations__ = {
                "name": name,
                "description": description,
                "privacy": privacy,
                "privacyUrl": privacyUrl,
                "homePage": homePage,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["privacy"]) -> MetaOapg.properties.privacy: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["privacyUrl"]) -> MetaOapg.properties.privacyUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["homePage"]) -> MetaOapg.properties.homePage: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "description", "privacy", "privacyUrl", "homePage", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["privacy"]) -> typing.Union[MetaOapg.properties.privacy, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["privacyUrl"]) -> typing.Union[MetaOapg.properties.privacyUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["homePage"]) -> typing.Union[MetaOapg.properties.homePage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "description", "privacy", "privacyUrl", "homePage", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        privacy: typing.Union[MetaOapg.properties.privacy, str, schemas.Unset] = schemas.unset,
        privacyUrl: typing.Union[MetaOapg.properties.privacyUrl, str, schemas.Unset] = schemas.unset,
        homePage: typing.Union[MetaOapg.properties.homePage, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateOrUpdateAppSdkDto':
        return super().__new__(
            cls,
            *args,
            name=name,
            description=description,
            privacy=privacy,
            privacyUrl=privacyUrl,
            homePage=homePage,
            _configuration=_configuration,
            **kwargs,
        )
