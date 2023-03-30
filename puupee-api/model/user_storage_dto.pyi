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


class UserStorageDto(
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
            maxSize = schemas.Int64Schema
            currentSize = schemas.Int64Schema
            totalCount = schemas.Int32Schema
            singleFileMaxSize = schemas.Int64Schema
            
            
            class items(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['UserStorageItemDto']:
                        return UserStorageItemDto
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['UserStorageItemDto'], typing.List['UserStorageItemDto']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'items':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'UserStorageItemDto':
                    return super().__getitem__(i)
            __annotations__ = {
                "name": name,
                "displayName": displayName,
                "maxSize": maxSize,
                "currentSize": currentSize,
                "totalCount": totalCount,
                "singleFileMaxSize": singleFileMaxSize,
                "items": items,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["displayName"]) -> MetaOapg.properties.displayName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxSize"]) -> MetaOapg.properties.maxSize: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currentSize"]) -> MetaOapg.properties.currentSize: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalCount"]) -> MetaOapg.properties.totalCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["singleFileMaxSize"]) -> MetaOapg.properties.singleFileMaxSize: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["items"]) -> MetaOapg.properties.items: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "displayName", "maxSize", "currentSize", "totalCount", "singleFileMaxSize", "items", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["displayName"]) -> typing.Union[MetaOapg.properties.displayName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxSize"]) -> typing.Union[MetaOapg.properties.maxSize, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currentSize"]) -> typing.Union[MetaOapg.properties.currentSize, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalCount"]) -> typing.Union[MetaOapg.properties.totalCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["singleFileMaxSize"]) -> typing.Union[MetaOapg.properties.singleFileMaxSize, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["items"]) -> typing.Union[MetaOapg.properties.items, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "displayName", "maxSize", "currentSize", "totalCount", "singleFileMaxSize", "items", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        displayName: typing.Union[MetaOapg.properties.displayName, str, schemas.Unset] = schemas.unset,
        maxSize: typing.Union[MetaOapg.properties.maxSize, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        currentSize: typing.Union[MetaOapg.properties.currentSize, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        totalCount: typing.Union[MetaOapg.properties.totalCount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        singleFileMaxSize: typing.Union[MetaOapg.properties.singleFileMaxSize, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        items: typing.Union[MetaOapg.properties.items, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UserStorageDto':
        return super().__new__(
            cls,
            *args,
            name=name,
            displayName=displayName,
            maxSize=maxSize,
            currentSize=currentSize,
            totalCount=totalCount,
            singleFileMaxSize=singleFileMaxSize,
            items=items,
            _configuration=_configuration,
            **kwargs,
        )

from puupee-api.model.user_storage_item_dto import UserStorageItemDto
