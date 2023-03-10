# coding: utf-8

"""
    Puupee API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
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

from openapi_client import schemas  # noqa: F401


class CreateOrUpdateAppReleaseDto(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            version = schemas.StrSchema
            notes = schemas.StrSchema
            platform = schemas.StrSchema
            key = schemas.StrSchema
            rapidCode = schemas.StrSchema
            size = schemas.Int64Schema
            md5 = schemas.StrSchema
            sliceMd5 = schemas.StrSchema
            productType = schemas.StrSchema
            isForceUpdate = schemas.BoolSchema
            appId = schemas.UUIDSchema
            isEnabled = schemas.BoolSchema
            channel = schemas.StrSchema
            environment = schemas.StrSchema
            __annotations__ = {
                "version": version,
                "notes": notes,
                "platform": platform,
                "key": key,
                "rapidCode": rapidCode,
                "size": size,
                "md5": md5,
                "sliceMd5": sliceMd5,
                "productType": productType,
                "isForceUpdate": isForceUpdate,
                "appId": appId,
                "isEnabled": isEnabled,
                "channel": channel,
                "environment": environment,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["version"]) -> MetaOapg.properties.version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notes"]) -> MetaOapg.properties.notes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["platform"]) -> MetaOapg.properties.platform: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["key"]) -> MetaOapg.properties.key: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rapidCode"]) -> MetaOapg.properties.rapidCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["size"]) -> MetaOapg.properties.size: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["md5"]) -> MetaOapg.properties.md5: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sliceMd5"]) -> MetaOapg.properties.sliceMd5: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["productType"]) -> MetaOapg.properties.productType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isForceUpdate"]) -> MetaOapg.properties.isForceUpdate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["appId"]) -> MetaOapg.properties.appId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isEnabled"]) -> MetaOapg.properties.isEnabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["channel"]) -> MetaOapg.properties.channel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["environment"]) -> MetaOapg.properties.environment: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["version", "notes", "platform", "key", "rapidCode", "size", "md5", "sliceMd5", "productType", "isForceUpdate", "appId", "isEnabled", "channel", "environment", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["version"]) -> typing.Union[MetaOapg.properties.version, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notes"]) -> typing.Union[MetaOapg.properties.notes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["platform"]) -> typing.Union[MetaOapg.properties.platform, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["key"]) -> typing.Union[MetaOapg.properties.key, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rapidCode"]) -> typing.Union[MetaOapg.properties.rapidCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["size"]) -> typing.Union[MetaOapg.properties.size, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["md5"]) -> typing.Union[MetaOapg.properties.md5, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sliceMd5"]) -> typing.Union[MetaOapg.properties.sliceMd5, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["productType"]) -> typing.Union[MetaOapg.properties.productType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isForceUpdate"]) -> typing.Union[MetaOapg.properties.isForceUpdate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["appId"]) -> typing.Union[MetaOapg.properties.appId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isEnabled"]) -> typing.Union[MetaOapg.properties.isEnabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["channel"]) -> typing.Union[MetaOapg.properties.channel, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["environment"]) -> typing.Union[MetaOapg.properties.environment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["version", "notes", "platform", "key", "rapidCode", "size", "md5", "sliceMd5", "productType", "isForceUpdate", "appId", "isEnabled", "channel", "environment", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        version: typing.Union[MetaOapg.properties.version, str, schemas.Unset] = schemas.unset,
        notes: typing.Union[MetaOapg.properties.notes, str, schemas.Unset] = schemas.unset,
        platform: typing.Union[MetaOapg.properties.platform, str, schemas.Unset] = schemas.unset,
        key: typing.Union[MetaOapg.properties.key, str, schemas.Unset] = schemas.unset,
        rapidCode: typing.Union[MetaOapg.properties.rapidCode, str, schemas.Unset] = schemas.unset,
        size: typing.Union[MetaOapg.properties.size, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        md5: typing.Union[MetaOapg.properties.md5, str, schemas.Unset] = schemas.unset,
        sliceMd5: typing.Union[MetaOapg.properties.sliceMd5, str, schemas.Unset] = schemas.unset,
        productType: typing.Union[MetaOapg.properties.productType, str, schemas.Unset] = schemas.unset,
        isForceUpdate: typing.Union[MetaOapg.properties.isForceUpdate, bool, schemas.Unset] = schemas.unset,
        appId: typing.Union[MetaOapg.properties.appId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        isEnabled: typing.Union[MetaOapg.properties.isEnabled, bool, schemas.Unset] = schemas.unset,
        channel: typing.Union[MetaOapg.properties.channel, str, schemas.Unset] = schemas.unset,
        environment: typing.Union[MetaOapg.properties.environment, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateOrUpdateAppReleaseDto':
        return super().__new__(
            cls,
            *args,
            version=version,
            notes=notes,
            platform=platform,
            key=key,
            rapidCode=rapidCode,
            size=size,
            md5=md5,
            sliceMd5=sliceMd5,
            productType=productType,
            isForceUpdate=isForceUpdate,
            appId=appId,
            isEnabled=isEnabled,
            channel=channel,
            environment=environment,
            _configuration=_configuration,
            **kwargs,
        )
