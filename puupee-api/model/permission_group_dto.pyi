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


class PermissionGroupDto(
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
            displayNameKey = schemas.StrSchema
            displayNameResource = schemas.StrSchema
            
            
            class permissions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['PermissionGrantInfoDto']:
                        return PermissionGrantInfoDto
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['PermissionGrantInfoDto'], typing.List['PermissionGrantInfoDto']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'permissions':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'PermissionGrantInfoDto':
                    return super().__getitem__(i)
            __annotations__ = {
                "name": name,
                "displayName": displayName,
                "displayNameKey": displayNameKey,
                "displayNameResource": displayNameResource,
                "permissions": permissions,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["displayName"]) -> MetaOapg.properties.displayName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["displayNameKey"]) -> MetaOapg.properties.displayNameKey: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["displayNameResource"]) -> MetaOapg.properties.displayNameResource: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["permissions"]) -> MetaOapg.properties.permissions: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "displayName", "displayNameKey", "displayNameResource", "permissions", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["displayName"]) -> typing.Union[MetaOapg.properties.displayName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["displayNameKey"]) -> typing.Union[MetaOapg.properties.displayNameKey, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["displayNameResource"]) -> typing.Union[MetaOapg.properties.displayNameResource, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["permissions"]) -> typing.Union[MetaOapg.properties.permissions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "displayName", "displayNameKey", "displayNameResource", "permissions", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        displayName: typing.Union[MetaOapg.properties.displayName, str, schemas.Unset] = schemas.unset,
        displayNameKey: typing.Union[MetaOapg.properties.displayNameKey, str, schemas.Unset] = schemas.unset,
        displayNameResource: typing.Union[MetaOapg.properties.displayNameResource, str, schemas.Unset] = schemas.unset,
        permissions: typing.Union[MetaOapg.properties.permissions, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PermissionGroupDto':
        return super().__new__(
            cls,
            *args,
            name=name,
            displayName=displayName,
            displayNameKey=displayNameKey,
            displayNameResource=displayNameResource,
            permissions=permissions,
            _configuration=_configuration,
            **kwargs,
        )

from puupee-api.model.permission_grant_info_dto import PermissionGrantInfoDto
