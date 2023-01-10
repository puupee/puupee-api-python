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


class ExtensionPropertyApiDto(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def onGet() -> typing.Type['ExtensionPropertyApiGetDto']:
                return ExtensionPropertyApiGetDto
        
            @staticmethod
            def onCreate() -> typing.Type['ExtensionPropertyApiCreateDto']:
                return ExtensionPropertyApiCreateDto
        
            @staticmethod
            def onUpdate() -> typing.Type['ExtensionPropertyApiUpdateDto']:
                return ExtensionPropertyApiUpdateDto
            __annotations__ = {
                "onGet": onGet,
                "onCreate": onCreate,
                "onUpdate": onUpdate,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["onGet"]) -> 'ExtensionPropertyApiGetDto': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["onCreate"]) -> 'ExtensionPropertyApiCreateDto': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["onUpdate"]) -> 'ExtensionPropertyApiUpdateDto': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["onGet", "onCreate", "onUpdate", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["onGet"]) -> typing.Union['ExtensionPropertyApiGetDto', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["onCreate"]) -> typing.Union['ExtensionPropertyApiCreateDto', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["onUpdate"]) -> typing.Union['ExtensionPropertyApiUpdateDto', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["onGet", "onCreate", "onUpdate", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        onGet: typing.Union['ExtensionPropertyApiGetDto', schemas.Unset] = schemas.unset,
        onCreate: typing.Union['ExtensionPropertyApiCreateDto', schemas.Unset] = schemas.unset,
        onUpdate: typing.Union['ExtensionPropertyApiUpdateDto', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ExtensionPropertyApiDto':
        return super().__new__(
            cls,
            *args,
            onGet=onGet,
            onCreate=onCreate,
            onUpdate=onUpdate,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.extension_property_api_create_dto import ExtensionPropertyApiCreateDto
from openapi_client.model.extension_property_api_get_dto import ExtensionPropertyApiGetDto
from openapi_client.model.extension_property_api_update_dto import ExtensionPropertyApiUpdateDto
