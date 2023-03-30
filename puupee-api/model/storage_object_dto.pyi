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


class StorageObjectDto(
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
            key = schemas.StrSchema
            url = schemas.StrSchema
            size = schemas.Int64Schema
            md5 = schemas.StrSchema
            sliceMd5 = schemas.StrSchema
            rapidCode = schemas.StrSchema
            contentType = schemas.StrSchema
            extension = schemas.StrSchema
            storageClass = schemas.StrSchema
            storageObjectCreatedAt = schemas.DateTimeSchema
            storageObjectUpdatedAt = schemas.DateTimeSchema
            syncVersion = schemas.Int64Schema
            password = schemas.StrSchema
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
                "key": key,
                "url": url,
                "size": size,
                "md5": md5,
                "sliceMd5": sliceMd5,
                "rapidCode": rapidCode,
                "contentType": contentType,
                "extension": extension,
                "storageClass": storageClass,
                "storageObjectCreatedAt": storageObjectCreatedAt,
                "storageObjectUpdatedAt": storageObjectUpdatedAt,
                "syncVersion": syncVersion,
                "password": password,
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
    def __getitem__(self, name: typing_extensions.Literal["key"]) -> MetaOapg.properties.key: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["size"]) -> MetaOapg.properties.size: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["md5"]) -> MetaOapg.properties.md5: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sliceMd5"]) -> MetaOapg.properties.sliceMd5: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rapidCode"]) -> MetaOapg.properties.rapidCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contentType"]) -> MetaOapg.properties.contentType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["extension"]) -> MetaOapg.properties.extension: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["storageClass"]) -> MetaOapg.properties.storageClass: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["storageObjectCreatedAt"]) -> MetaOapg.properties.storageObjectCreatedAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["storageObjectUpdatedAt"]) -> MetaOapg.properties.storageObjectUpdatedAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["syncVersion"]) -> MetaOapg.properties.syncVersion: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["password"]) -> MetaOapg.properties.password: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "creationTime", "creatorId", "lastModificationTime", "lastModifierId", "isDeleted", "deleterId", "deletionTime", "name", "key", "url", "size", "md5", "sliceMd5", "rapidCode", "contentType", "extension", "storageClass", "storageObjectCreatedAt", "storageObjectUpdatedAt", "syncVersion", "password", ], str]):
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
    def get_item_oapg(self, name: typing_extensions.Literal["key"]) -> typing.Union[MetaOapg.properties.key, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> typing.Union[MetaOapg.properties.url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["size"]) -> typing.Union[MetaOapg.properties.size, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["md5"]) -> typing.Union[MetaOapg.properties.md5, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sliceMd5"]) -> typing.Union[MetaOapg.properties.sliceMd5, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rapidCode"]) -> typing.Union[MetaOapg.properties.rapidCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contentType"]) -> typing.Union[MetaOapg.properties.contentType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["extension"]) -> typing.Union[MetaOapg.properties.extension, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["storageClass"]) -> typing.Union[MetaOapg.properties.storageClass, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["storageObjectCreatedAt"]) -> typing.Union[MetaOapg.properties.storageObjectCreatedAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["storageObjectUpdatedAt"]) -> typing.Union[MetaOapg.properties.storageObjectUpdatedAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["syncVersion"]) -> typing.Union[MetaOapg.properties.syncVersion, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["password"]) -> typing.Union[MetaOapg.properties.password, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "creationTime", "creatorId", "lastModificationTime", "lastModifierId", "isDeleted", "deleterId", "deletionTime", "name", "key", "url", "size", "md5", "sliceMd5", "rapidCode", "contentType", "extension", "storageClass", "storageObjectCreatedAt", "storageObjectUpdatedAt", "syncVersion", "password", ], str]):
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
        key: typing.Union[MetaOapg.properties.key, str, schemas.Unset] = schemas.unset,
        url: typing.Union[MetaOapg.properties.url, str, schemas.Unset] = schemas.unset,
        size: typing.Union[MetaOapg.properties.size, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        md5: typing.Union[MetaOapg.properties.md5, str, schemas.Unset] = schemas.unset,
        sliceMd5: typing.Union[MetaOapg.properties.sliceMd5, str, schemas.Unset] = schemas.unset,
        rapidCode: typing.Union[MetaOapg.properties.rapidCode, str, schemas.Unset] = schemas.unset,
        contentType: typing.Union[MetaOapg.properties.contentType, str, schemas.Unset] = schemas.unset,
        extension: typing.Union[MetaOapg.properties.extension, str, schemas.Unset] = schemas.unset,
        storageClass: typing.Union[MetaOapg.properties.storageClass, str, schemas.Unset] = schemas.unset,
        storageObjectCreatedAt: typing.Union[MetaOapg.properties.storageObjectCreatedAt, str, datetime, schemas.Unset] = schemas.unset,
        storageObjectUpdatedAt: typing.Union[MetaOapg.properties.storageObjectUpdatedAt, str, datetime, schemas.Unset] = schemas.unset,
        syncVersion: typing.Union[MetaOapg.properties.syncVersion, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        password: typing.Union[MetaOapg.properties.password, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'StorageObjectDto':
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
            key=key,
            url=url,
            size=size,
            md5=md5,
            sliceMd5=sliceMd5,
            rapidCode=rapidCode,
            contentType=contentType,
            extension=extension,
            storageClass=storageClass,
            storageObjectCreatedAt=storageObjectCreatedAt,
            storageObjectUpdatedAt=storageObjectUpdatedAt,
            syncVersion=syncVersion,
            password=password,
            _configuration=_configuration,
            **kwargs,
        )
