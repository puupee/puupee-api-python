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


class UserData(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            id = schemas.UUIDSchema
            tenantId = schemas.UUIDSchema
            userName = schemas.StrSchema
            name = schemas.StrSchema
            surname = schemas.StrSchema
            isActive = schemas.BoolSchema
            email = schemas.StrSchema
            emailConfirmed = schemas.BoolSchema
            phoneNumber = schemas.StrSchema
            phoneNumberConfirmed = schemas.BoolSchema
            __annotations__ = {
                "id": id,
                "tenantId": tenantId,
                "userName": userName,
                "name": name,
                "surname": surname,
                "isActive": isActive,
                "email": email,
                "emailConfirmed": emailConfirmed,
                "phoneNumber": phoneNumber,
                "phoneNumberConfirmed": phoneNumberConfirmed,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tenantId"]) -> MetaOapg.properties.tenantId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userName"]) -> MetaOapg.properties.userName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["surname"]) -> MetaOapg.properties.surname: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isActive"]) -> MetaOapg.properties.isActive: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["emailConfirmed"]) -> MetaOapg.properties.emailConfirmed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phoneNumber"]) -> MetaOapg.properties.phoneNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phoneNumberConfirmed"]) -> MetaOapg.properties.phoneNumberConfirmed: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "tenantId", "userName", "name", "surname", "isActive", "email", "emailConfirmed", "phoneNumber", "phoneNumberConfirmed", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tenantId"]) -> typing.Union[MetaOapg.properties.tenantId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userName"]) -> typing.Union[MetaOapg.properties.userName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["surname"]) -> typing.Union[MetaOapg.properties.surname, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isActive"]) -> typing.Union[MetaOapg.properties.isActive, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["emailConfirmed"]) -> typing.Union[MetaOapg.properties.emailConfirmed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phoneNumber"]) -> typing.Union[MetaOapg.properties.phoneNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phoneNumberConfirmed"]) -> typing.Union[MetaOapg.properties.phoneNumberConfirmed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "tenantId", "userName", "name", "surname", "isActive", "email", "emailConfirmed", "phoneNumber", "phoneNumberConfirmed", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        tenantId: typing.Union[MetaOapg.properties.tenantId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        userName: typing.Union[MetaOapg.properties.userName, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        surname: typing.Union[MetaOapg.properties.surname, str, schemas.Unset] = schemas.unset,
        isActive: typing.Union[MetaOapg.properties.isActive, bool, schemas.Unset] = schemas.unset,
        email: typing.Union[MetaOapg.properties.email, str, schemas.Unset] = schemas.unset,
        emailConfirmed: typing.Union[MetaOapg.properties.emailConfirmed, bool, schemas.Unset] = schemas.unset,
        phoneNumber: typing.Union[MetaOapg.properties.phoneNumber, str, schemas.Unset] = schemas.unset,
        phoneNumberConfirmed: typing.Union[MetaOapg.properties.phoneNumberConfirmed, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UserData':
        return super().__new__(
            cls,
            *args,
            id=id,
            tenantId=tenantId,
            userName=userName,
            name=name,
            surname=surname,
            isActive=isActive,
            email=email,
            emailConfirmed=emailConfirmed,
            phoneNumber=phoneNumber,
            phoneNumberConfirmed=phoneNumberConfirmed,
            _configuration=_configuration,
            **kwargs,
        )
