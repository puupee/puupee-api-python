# coding: utf-8

"""
    Puupee API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
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


class SendPasswordResetCodeDto(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "appName",
            "email",
        }
        
        class properties:
            
            
            class email(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    format = 'email'
                    max_length = 256
                    min_length = 0
            appName = schemas.StrSchema
            returnUrl = schemas.StrSchema
            returnUrlHash = schemas.StrSchema
            __annotations__ = {
                "email": email,
                "appName": appName,
                "returnUrl": returnUrl,
                "returnUrlHash": returnUrlHash,
            }
    
    appName: MetaOapg.properties.appName
    email: MetaOapg.properties.email
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["appName"]) -> MetaOapg.properties.appName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["returnUrl"]) -> MetaOapg.properties.returnUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["returnUrlHash"]) -> MetaOapg.properties.returnUrlHash: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["email", "appName", "returnUrl", "returnUrlHash", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["appName"]) -> MetaOapg.properties.appName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["returnUrl"]) -> typing.Union[MetaOapg.properties.returnUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["returnUrlHash"]) -> typing.Union[MetaOapg.properties.returnUrlHash, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["email", "appName", "returnUrl", "returnUrlHash", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        appName: typing.Union[MetaOapg.properties.appName, str, ],
        email: typing.Union[MetaOapg.properties.email, str, ],
        returnUrl: typing.Union[MetaOapg.properties.returnUrl, str, schemas.Unset] = schemas.unset,
        returnUrlHash: typing.Union[MetaOapg.properties.returnUrlHash, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SendPasswordResetCodeDto':
        return super().__new__(
            cls,
            *args,
            appName=appName,
            email=email,
            returnUrl=returnUrl,
            returnUrlHash=returnUrlHash,
            _configuration=_configuration,
            **kwargs,
        )
