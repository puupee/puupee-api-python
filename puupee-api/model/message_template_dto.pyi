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


class MessageTemplateDto(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            id = schemas.UUIDSchema
            creationTime = schemas.DateTimeSchema
            creatorId = schemas.UUIDSchema
            lastModificationTime = schemas.DateTimeSchema
            lastModifierId = schemas.UUIDSchema
            isDeleted = schemas.BoolSchema
            deleterId = schemas.UUIDSchema
            deletionTime = schemas.DateTimeSchema
            name = schemas.StrSchema
            description = schemas.StrSchema
            latestVersion = schemas.Int32Schema
            __annotations__ = {
                "id": id,
                "creationTime": creationTime,
                "creatorId": creatorId,
                "lastModificationTime": lastModificationTime,
                "lastModifierId": lastModifierId,
                "isDeleted": isDeleted,
                "deleterId": deleterId,
                "deletionTime": deletionTime,
                "name": name,
                "description": description,
                "latestVersion": latestVersion,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["creationTime"]) -> MetaOapg.properties.creationTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["creatorId"]) -> MetaOapg.properties.creatorId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastModificationTime"]) -> MetaOapg.properties.lastModificationTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastModifierId"]) -> MetaOapg.properties.lastModifierId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isDeleted"]) -> MetaOapg.properties.isDeleted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deleterId"]) -> MetaOapg.properties.deleterId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deletionTime"]) -> MetaOapg.properties.deletionTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["latestVersion"]) -> MetaOapg.properties.latestVersion: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "creationTime", "creatorId", "lastModificationTime", "lastModifierId", "isDeleted", "deleterId", "deletionTime", "name", "description", "latestVersion", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["creationTime"]) -> typing.Union[MetaOapg.properties.creationTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["creatorId"]) -> typing.Union[MetaOapg.properties.creatorId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastModificationTime"]) -> typing.Union[MetaOapg.properties.lastModificationTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastModifierId"]) -> typing.Union[MetaOapg.properties.lastModifierId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isDeleted"]) -> typing.Union[MetaOapg.properties.isDeleted, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deleterId"]) -> typing.Union[MetaOapg.properties.deleterId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deletionTime"]) -> typing.Union[MetaOapg.properties.deletionTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["latestVersion"]) -> typing.Union[MetaOapg.properties.latestVersion, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "creationTime", "creatorId", "lastModificationTime", "lastModifierId", "isDeleted", "deleterId", "deletionTime", "name", "description", "latestVersion", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        creationTime: typing.Union[MetaOapg.properties.creationTime, str, datetime, schemas.Unset] = schemas.unset,
        creatorId: typing.Union[MetaOapg.properties.creatorId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        lastModificationTime: typing.Union[MetaOapg.properties.lastModificationTime, str, datetime, schemas.Unset] = schemas.unset,
        lastModifierId: typing.Union[MetaOapg.properties.lastModifierId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        isDeleted: typing.Union[MetaOapg.properties.isDeleted, bool, schemas.Unset] = schemas.unset,
        deleterId: typing.Union[MetaOapg.properties.deleterId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        deletionTime: typing.Union[MetaOapg.properties.deletionTime, str, datetime, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        latestVersion: typing.Union[MetaOapg.properties.latestVersion, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MessageTemplateDto':
        return super().__new__(
            cls,
            *args,
            id=id,
            creationTime=creationTime,
            creatorId=creatorId,
            lastModificationTime=lastModificationTime,
            lastModifierId=lastModifierId,
            isDeleted=isDeleted,
            deleterId=deleterId,
            deletionTime=deletionTime,
            name=name,
            description=description,
            latestVersion=latestVersion,
            _configuration=_configuration,
            **kwargs,
        )
