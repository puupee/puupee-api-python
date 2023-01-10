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


class IdentityUserDto(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class extraProperties(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    additional_properties = schemas.DictSchema
                
                def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, ],
                ) -> 'extraProperties':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            id = schemas.UUIDSchema
            creationTime = schemas.DateTimeSchema
            creatorId = schemas.UUIDSchema
            lastModificationTime = schemas.DateTimeSchema
            lastModifierId = schemas.UUIDSchema
            isDeleted = schemas.BoolSchema
            deleterId = schemas.UUIDSchema
            deletionTime = schemas.DateTimeSchema
            tenantId = schemas.UUIDSchema
            userName = schemas.StrSchema
            name = schemas.StrSchema
            surname = schemas.StrSchema
            email = schemas.StrSchema
            emailConfirmed = schemas.BoolSchema
            phoneNumber = schemas.StrSchema
            phoneNumberConfirmed = schemas.BoolSchema
            isActive = schemas.BoolSchema
            lockoutEnabled = schemas.BoolSchema
            lockoutEnd = schemas.DateTimeSchema
            concurrencyStamp = schemas.StrSchema
            __annotations__ = {
                "extraProperties": extraProperties,
                "id": id,
                "creationTime": creationTime,
                "creatorId": creatorId,
                "lastModificationTime": lastModificationTime,
                "lastModifierId": lastModifierId,
                "isDeleted": isDeleted,
                "deleterId": deleterId,
                "deletionTime": deletionTime,
                "tenantId": tenantId,
                "userName": userName,
                "name": name,
                "surname": surname,
                "email": email,
                "emailConfirmed": emailConfirmed,
                "phoneNumber": phoneNumber,
                "phoneNumberConfirmed": phoneNumberConfirmed,
                "isActive": isActive,
                "lockoutEnabled": lockoutEnabled,
                "lockoutEnd": lockoutEnd,
                "concurrencyStamp": concurrencyStamp,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["extraProperties"]) -> MetaOapg.properties.extraProperties: ...
    
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
    def __getitem__(self, name: typing_extensions.Literal["tenantId"]) -> MetaOapg.properties.tenantId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userName"]) -> MetaOapg.properties.userName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["surname"]) -> MetaOapg.properties.surname: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["emailConfirmed"]) -> MetaOapg.properties.emailConfirmed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phoneNumber"]) -> MetaOapg.properties.phoneNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phoneNumberConfirmed"]) -> MetaOapg.properties.phoneNumberConfirmed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isActive"]) -> MetaOapg.properties.isActive: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lockoutEnabled"]) -> MetaOapg.properties.lockoutEnabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lockoutEnd"]) -> MetaOapg.properties.lockoutEnd: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["concurrencyStamp"]) -> MetaOapg.properties.concurrencyStamp: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["extraProperties", "id", "creationTime", "creatorId", "lastModificationTime", "lastModifierId", "isDeleted", "deleterId", "deletionTime", "tenantId", "userName", "name", "surname", "email", "emailConfirmed", "phoneNumber", "phoneNumberConfirmed", "isActive", "lockoutEnabled", "lockoutEnd", "concurrencyStamp", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["extraProperties"]) -> typing.Union[MetaOapg.properties.extraProperties, schemas.Unset]: ...
    
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
    def get_item_oapg(self, name: typing_extensions.Literal["tenantId"]) -> typing.Union[MetaOapg.properties.tenantId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userName"]) -> typing.Union[MetaOapg.properties.userName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["surname"]) -> typing.Union[MetaOapg.properties.surname, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["emailConfirmed"]) -> typing.Union[MetaOapg.properties.emailConfirmed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phoneNumber"]) -> typing.Union[MetaOapg.properties.phoneNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phoneNumberConfirmed"]) -> typing.Union[MetaOapg.properties.phoneNumberConfirmed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isActive"]) -> typing.Union[MetaOapg.properties.isActive, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lockoutEnabled"]) -> typing.Union[MetaOapg.properties.lockoutEnabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lockoutEnd"]) -> typing.Union[MetaOapg.properties.lockoutEnd, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["concurrencyStamp"]) -> typing.Union[MetaOapg.properties.concurrencyStamp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["extraProperties", "id", "creationTime", "creatorId", "lastModificationTime", "lastModifierId", "isDeleted", "deleterId", "deletionTime", "tenantId", "userName", "name", "surname", "email", "emailConfirmed", "phoneNumber", "phoneNumberConfirmed", "isActive", "lockoutEnabled", "lockoutEnd", "concurrencyStamp", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        extraProperties: typing.Union[MetaOapg.properties.extraProperties, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        creationTime: typing.Union[MetaOapg.properties.creationTime, str, datetime, schemas.Unset] = schemas.unset,
        creatorId: typing.Union[MetaOapg.properties.creatorId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        lastModificationTime: typing.Union[MetaOapg.properties.lastModificationTime, str, datetime, schemas.Unset] = schemas.unset,
        lastModifierId: typing.Union[MetaOapg.properties.lastModifierId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        isDeleted: typing.Union[MetaOapg.properties.isDeleted, bool, schemas.Unset] = schemas.unset,
        deleterId: typing.Union[MetaOapg.properties.deleterId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        deletionTime: typing.Union[MetaOapg.properties.deletionTime, str, datetime, schemas.Unset] = schemas.unset,
        tenantId: typing.Union[MetaOapg.properties.tenantId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        userName: typing.Union[MetaOapg.properties.userName, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        surname: typing.Union[MetaOapg.properties.surname, str, schemas.Unset] = schemas.unset,
        email: typing.Union[MetaOapg.properties.email, str, schemas.Unset] = schemas.unset,
        emailConfirmed: typing.Union[MetaOapg.properties.emailConfirmed, bool, schemas.Unset] = schemas.unset,
        phoneNumber: typing.Union[MetaOapg.properties.phoneNumber, str, schemas.Unset] = schemas.unset,
        phoneNumberConfirmed: typing.Union[MetaOapg.properties.phoneNumberConfirmed, bool, schemas.Unset] = schemas.unset,
        isActive: typing.Union[MetaOapg.properties.isActive, bool, schemas.Unset] = schemas.unset,
        lockoutEnabled: typing.Union[MetaOapg.properties.lockoutEnabled, bool, schemas.Unset] = schemas.unset,
        lockoutEnd: typing.Union[MetaOapg.properties.lockoutEnd, str, datetime, schemas.Unset] = schemas.unset,
        concurrencyStamp: typing.Union[MetaOapg.properties.concurrencyStamp, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'IdentityUserDto':
        return super().__new__(
            cls,
            *args,
            extraProperties=extraProperties,
            id=id,
            creationTime=creationTime,
            creatorId=creatorId,
            lastModificationTime=lastModificationTime,
            lastModifierId=lastModifierId,
            isDeleted=isDeleted,
            deleterId=deleterId,
            deletionTime=deletionTime,
            tenantId=tenantId,
            userName=userName,
            name=name,
            surname=surname,
            email=email,
            emailConfirmed=emailConfirmed,
            phoneNumber=phoneNumber,
            phoneNumberConfirmed=phoneNumberConfirmed,
            isActive=isActive,
            lockoutEnabled=lockoutEnabled,
            lockoutEnd=lockoutEnd,
            concurrencyStamp=concurrencyStamp,
            _configuration=_configuration,
            **kwargs,
        )
