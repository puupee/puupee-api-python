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


class ChangePasswordInput(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "newPassword",
        }
        
        class properties:
            
            
            class newPassword(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 128
                    min_length = 0
            
            
            class currentPassword(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 128
                    min_length = 0
            __annotations__ = {
                "newPassword": newPassword,
                "currentPassword": currentPassword,
            }
    
    newPassword: MetaOapg.properties.newPassword
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["newPassword"]) -> MetaOapg.properties.newPassword: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currentPassword"]) -> MetaOapg.properties.currentPassword: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["newPassword", "currentPassword", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["newPassword"]) -> MetaOapg.properties.newPassword: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currentPassword"]) -> typing.Union[MetaOapg.properties.currentPassword, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["newPassword", "currentPassword", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        newPassword: typing.Union[MetaOapg.properties.newPassword, str, ],
        currentPassword: typing.Union[MetaOapg.properties.currentPassword, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ChangePasswordInput':
        return super().__new__(
            cls,
            *args,
            newPassword=newPassword,
            currentPassword=currentPassword,
            _configuration=_configuration,
            **kwargs,
        )
