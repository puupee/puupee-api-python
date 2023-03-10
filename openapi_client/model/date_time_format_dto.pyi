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


class DateTimeFormatDto(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            calendarAlgorithmType = schemas.StrSchema
            dateTimeFormatLong = schemas.StrSchema
            shortDatePattern = schemas.StrSchema
            fullDateTimePattern = schemas.StrSchema
            dateSeparator = schemas.StrSchema
            shortTimePattern = schemas.StrSchema
            longTimePattern = schemas.StrSchema
            __annotations__ = {
                "calendarAlgorithmType": calendarAlgorithmType,
                "dateTimeFormatLong": dateTimeFormatLong,
                "shortDatePattern": shortDatePattern,
                "fullDateTimePattern": fullDateTimePattern,
                "dateSeparator": dateSeparator,
                "shortTimePattern": shortTimePattern,
                "longTimePattern": longTimePattern,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["calendarAlgorithmType"]) -> MetaOapg.properties.calendarAlgorithmType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dateTimeFormatLong"]) -> MetaOapg.properties.dateTimeFormatLong: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shortDatePattern"]) -> MetaOapg.properties.shortDatePattern: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fullDateTimePattern"]) -> MetaOapg.properties.fullDateTimePattern: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dateSeparator"]) -> MetaOapg.properties.dateSeparator: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shortTimePattern"]) -> MetaOapg.properties.shortTimePattern: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["longTimePattern"]) -> MetaOapg.properties.longTimePattern: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["calendarAlgorithmType", "dateTimeFormatLong", "shortDatePattern", "fullDateTimePattern", "dateSeparator", "shortTimePattern", "longTimePattern", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["calendarAlgorithmType"]) -> typing.Union[MetaOapg.properties.calendarAlgorithmType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dateTimeFormatLong"]) -> typing.Union[MetaOapg.properties.dateTimeFormatLong, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shortDatePattern"]) -> typing.Union[MetaOapg.properties.shortDatePattern, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fullDateTimePattern"]) -> typing.Union[MetaOapg.properties.fullDateTimePattern, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dateSeparator"]) -> typing.Union[MetaOapg.properties.dateSeparator, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shortTimePattern"]) -> typing.Union[MetaOapg.properties.shortTimePattern, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["longTimePattern"]) -> typing.Union[MetaOapg.properties.longTimePattern, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["calendarAlgorithmType", "dateTimeFormatLong", "shortDatePattern", "fullDateTimePattern", "dateSeparator", "shortTimePattern", "longTimePattern", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        calendarAlgorithmType: typing.Union[MetaOapg.properties.calendarAlgorithmType, str, schemas.Unset] = schemas.unset,
        dateTimeFormatLong: typing.Union[MetaOapg.properties.dateTimeFormatLong, str, schemas.Unset] = schemas.unset,
        shortDatePattern: typing.Union[MetaOapg.properties.shortDatePattern, str, schemas.Unset] = schemas.unset,
        fullDateTimePattern: typing.Union[MetaOapg.properties.fullDateTimePattern, str, schemas.Unset] = schemas.unset,
        dateSeparator: typing.Union[MetaOapg.properties.dateSeparator, str, schemas.Unset] = schemas.unset,
        shortTimePattern: typing.Union[MetaOapg.properties.shortTimePattern, str, schemas.Unset] = schemas.unset,
        longTimePattern: typing.Union[MetaOapg.properties.longTimePattern, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DateTimeFormatDto':
        return super().__new__(
            cls,
            *args,
            calendarAlgorithmType=calendarAlgorithmType,
            dateTimeFormatLong=dateTimeFormatLong,
            shortDatePattern=shortDatePattern,
            fullDateTimePattern=fullDateTimePattern,
            dateSeparator=dateSeparator,
            shortTimePattern=shortTimePattern,
            longTimePattern=longTimePattern,
            _configuration=_configuration,
            **kwargs,
        )
