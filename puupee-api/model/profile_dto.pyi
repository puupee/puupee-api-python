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


class ProfileDto(
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
            userName = schemas.StrSchema
            email = schemas.StrSchema
            name = schemas.StrSchema
            surname = schemas.StrSchema
            phoneNumber = schemas.StrSchema
            isExternal = schemas.BoolSchema
            hasPassword = schemas.BoolSchema
            concurrencyStamp = schemas.StrSchema
            __annotations__ = {
                "extraProperties": extraProperties,
                "userName": userName,
                "email": email,
                "name": name,
                "surname": surname,
                "phoneNumber": phoneNumber,
                "isExternal": isExternal,
                "hasPassword": hasPassword,
                "concurrencyStamp": concurrencyStamp,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["extraProperties"]) -> MetaOapg.properties.extraProperties: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userName"]) -> MetaOapg.properties.userName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["surname"]) -> MetaOapg.properties.surname: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phoneNumber"]) -> MetaOapg.properties.phoneNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isExternal"]) -> MetaOapg.properties.isExternal: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hasPassword"]) -> MetaOapg.properties.hasPassword: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["concurrencyStamp"]) -> MetaOapg.properties.concurrencyStamp: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["extraProperties", "userName", "email", "name", "surname", "phoneNumber", "isExternal", "hasPassword", "concurrencyStamp", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["extraProperties"]) -> typing.Union[MetaOapg.properties.extraProperties, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userName"]) -> typing.Union[MetaOapg.properties.userName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["surname"]) -> typing.Union[MetaOapg.properties.surname, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phoneNumber"]) -> typing.Union[MetaOapg.properties.phoneNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isExternal"]) -> typing.Union[MetaOapg.properties.isExternal, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hasPassword"]) -> typing.Union[MetaOapg.properties.hasPassword, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["concurrencyStamp"]) -> typing.Union[MetaOapg.properties.concurrencyStamp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["extraProperties", "userName", "email", "name", "surname", "phoneNumber", "isExternal", "hasPassword", "concurrencyStamp", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        extraProperties: typing.Union[MetaOapg.properties.extraProperties, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        userName: typing.Union[MetaOapg.properties.userName, str, schemas.Unset] = schemas.unset,
        email: typing.Union[MetaOapg.properties.email, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        surname: typing.Union[MetaOapg.properties.surname, str, schemas.Unset] = schemas.unset,
        phoneNumber: typing.Union[MetaOapg.properties.phoneNumber, str, schemas.Unset] = schemas.unset,
        isExternal: typing.Union[MetaOapg.properties.isExternal, bool, schemas.Unset] = schemas.unset,
        hasPassword: typing.Union[MetaOapg.properties.hasPassword, bool, schemas.Unset] = schemas.unset,
        concurrencyStamp: typing.Union[MetaOapg.properties.concurrencyStamp, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ProfileDto':
        return super().__new__(
            cls,
            *args,
            extraProperties=extraProperties,
            userName=userName,
            email=email,
            name=name,
            surname=surname,
            phoneNumber=phoneNumber,
            isExternal=isExternal,
            hasPassword=hasPassword,
            concurrencyStamp=concurrencyStamp,
            _configuration=_configuration,
            **kwargs,
        )
