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


class CreateMessageTemplateReleaseDto(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            content = schemas.StrSchema
            templateId = schemas.UUIDSchema
            __annotations__ = {
                "content": content,
                "templateId": templateId,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["content"]) -> MetaOapg.properties.content: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["templateId"]) -> MetaOapg.properties.templateId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["content", "templateId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["content"]) -> typing.Union[MetaOapg.properties.content, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["templateId"]) -> typing.Union[MetaOapg.properties.templateId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["content", "templateId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        content: typing.Union[MetaOapg.properties.content, str, schemas.Unset] = schemas.unset,
        templateId: typing.Union[MetaOapg.properties.templateId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateMessageTemplateReleaseDto':
        return super().__new__(
            cls,
            *args,
            content=content,
            templateId=templateId,
            _configuration=_configuration,
            **kwargs,
        )