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


class MethodParameterApiDescriptionModel(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            name = schemas.StrSchema
            typeAsString = schemas.StrSchema
            type = schemas.StrSchema
            typeSimple = schemas.StrSchema
            isOptional = schemas.BoolSchema
            defaultValue = schemas.DictSchema
            __annotations__ = {
                "name": name,
                "typeAsString": typeAsString,
                "type": type,
                "typeSimple": typeSimple,
                "isOptional": isOptional,
                "defaultValue": defaultValue,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["typeAsString"]) -> MetaOapg.properties.typeAsString: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["typeSimple"]) -> MetaOapg.properties.typeSimple: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isOptional"]) -> MetaOapg.properties.isOptional: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["defaultValue"]) -> MetaOapg.properties.defaultValue: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "typeAsString", "type", "typeSimple", "isOptional", "defaultValue", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["typeAsString"]) -> typing.Union[MetaOapg.properties.typeAsString, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["typeSimple"]) -> typing.Union[MetaOapg.properties.typeSimple, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isOptional"]) -> typing.Union[MetaOapg.properties.isOptional, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["defaultValue"]) -> typing.Union[MetaOapg.properties.defaultValue, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "typeAsString", "type", "typeSimple", "isOptional", "defaultValue", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        typeAsString: typing.Union[MetaOapg.properties.typeAsString, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        typeSimple: typing.Union[MetaOapg.properties.typeSimple, str, schemas.Unset] = schemas.unset,
        isOptional: typing.Union[MetaOapg.properties.isOptional, bool, schemas.Unset] = schemas.unset,
        defaultValue: typing.Union[MetaOapg.properties.defaultValue, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MethodParameterApiDescriptionModel':
        return super().__new__(
            cls,
            *args,
            name=name,
            typeAsString=typeAsString,
            type=type,
            typeSimple=typeSimple,
            isOptional=isOptional,
            defaultValue=defaultValue,
            _configuration=_configuration,
            **kwargs,
        )
