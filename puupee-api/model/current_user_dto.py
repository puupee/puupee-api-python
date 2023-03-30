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


class CurrentUserDto(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            isAuthenticated = schemas.BoolSchema
            id = schemas.UUIDSchema
            tenantId = schemas.UUIDSchema
            impersonatorUserId = schemas.UUIDSchema
            impersonatorTenantId = schemas.UUIDSchema
            impersonatorUserName = schemas.StrSchema
            impersonatorTenantName = schemas.StrSchema
            userName = schemas.StrSchema
            name = schemas.StrSchema
            surName = schemas.StrSchema
            email = schemas.StrSchema
            emailVerified = schemas.BoolSchema
            phoneNumber = schemas.StrSchema
            phoneNumberVerified = schemas.BoolSchema
            
            
            class roles(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'roles':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "isAuthenticated": isAuthenticated,
                "id": id,
                "tenantId": tenantId,
                "impersonatorUserId": impersonatorUserId,
                "impersonatorTenantId": impersonatorTenantId,
                "impersonatorUserName": impersonatorUserName,
                "impersonatorTenantName": impersonatorTenantName,
                "userName": userName,
                "name": name,
                "surName": surName,
                "email": email,
                "emailVerified": emailVerified,
                "phoneNumber": phoneNumber,
                "phoneNumberVerified": phoneNumberVerified,
                "roles": roles,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isAuthenticated"]) -> MetaOapg.properties.isAuthenticated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tenantId"]) -> MetaOapg.properties.tenantId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["impersonatorUserId"]) -> MetaOapg.properties.impersonatorUserId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["impersonatorTenantId"]) -> MetaOapg.properties.impersonatorTenantId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["impersonatorUserName"]) -> MetaOapg.properties.impersonatorUserName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["impersonatorTenantName"]) -> MetaOapg.properties.impersonatorTenantName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userName"]) -> MetaOapg.properties.userName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["surName"]) -> MetaOapg.properties.surName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["emailVerified"]) -> MetaOapg.properties.emailVerified: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phoneNumber"]) -> MetaOapg.properties.phoneNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phoneNumberVerified"]) -> MetaOapg.properties.phoneNumberVerified: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["roles"]) -> MetaOapg.properties.roles: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["isAuthenticated", "id", "tenantId", "impersonatorUserId", "impersonatorTenantId", "impersonatorUserName", "impersonatorTenantName", "userName", "name", "surName", "email", "emailVerified", "phoneNumber", "phoneNumberVerified", "roles", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isAuthenticated"]) -> typing.Union[MetaOapg.properties.isAuthenticated, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tenantId"]) -> typing.Union[MetaOapg.properties.tenantId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["impersonatorUserId"]) -> typing.Union[MetaOapg.properties.impersonatorUserId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["impersonatorTenantId"]) -> typing.Union[MetaOapg.properties.impersonatorTenantId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["impersonatorUserName"]) -> typing.Union[MetaOapg.properties.impersonatorUserName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["impersonatorTenantName"]) -> typing.Union[MetaOapg.properties.impersonatorTenantName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userName"]) -> typing.Union[MetaOapg.properties.userName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["surName"]) -> typing.Union[MetaOapg.properties.surName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["emailVerified"]) -> typing.Union[MetaOapg.properties.emailVerified, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phoneNumber"]) -> typing.Union[MetaOapg.properties.phoneNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phoneNumberVerified"]) -> typing.Union[MetaOapg.properties.phoneNumberVerified, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["roles"]) -> typing.Union[MetaOapg.properties.roles, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["isAuthenticated", "id", "tenantId", "impersonatorUserId", "impersonatorTenantId", "impersonatorUserName", "impersonatorTenantName", "userName", "name", "surName", "email", "emailVerified", "phoneNumber", "phoneNumberVerified", "roles", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        isAuthenticated: typing.Union[MetaOapg.properties.isAuthenticated, bool, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        tenantId: typing.Union[MetaOapg.properties.tenantId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        impersonatorUserId: typing.Union[MetaOapg.properties.impersonatorUserId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        impersonatorTenantId: typing.Union[MetaOapg.properties.impersonatorTenantId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        impersonatorUserName: typing.Union[MetaOapg.properties.impersonatorUserName, str, schemas.Unset] = schemas.unset,
        impersonatorTenantName: typing.Union[MetaOapg.properties.impersonatorTenantName, str, schemas.Unset] = schemas.unset,
        userName: typing.Union[MetaOapg.properties.userName, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        surName: typing.Union[MetaOapg.properties.surName, str, schemas.Unset] = schemas.unset,
        email: typing.Union[MetaOapg.properties.email, str, schemas.Unset] = schemas.unset,
        emailVerified: typing.Union[MetaOapg.properties.emailVerified, bool, schemas.Unset] = schemas.unset,
        phoneNumber: typing.Union[MetaOapg.properties.phoneNumber, str, schemas.Unset] = schemas.unset,
        phoneNumberVerified: typing.Union[MetaOapg.properties.phoneNumberVerified, bool, schemas.Unset] = schemas.unset,
        roles: typing.Union[MetaOapg.properties.roles, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CurrentUserDto':
        return super().__new__(
            cls,
            *args,
            isAuthenticated=isAuthenticated,
            id=id,
            tenantId=tenantId,
            impersonatorUserId=impersonatorUserId,
            impersonatorTenantId=impersonatorTenantId,
            impersonatorUserName=impersonatorUserName,
            impersonatorTenantName=impersonatorTenantName,
            userName=userName,
            name=name,
            surName=surName,
            email=email,
            emailVerified=emailVerified,
            phoneNumber=phoneNumber,
            phoneNumberVerified=phoneNumberVerified,
            roles=roles,
            _configuration=_configuration,
            **kwargs,
        )
