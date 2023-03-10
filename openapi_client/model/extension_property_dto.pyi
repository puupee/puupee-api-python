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


class ExtensionPropertyDto(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            type = schemas.StrSchema
            typeSimple = schemas.StrSchema
        
            @staticmethod
            def displayName() -> typing.Type['LocalizableStringDto']:
                return LocalizableStringDto
        
            @staticmethod
            def api() -> typing.Type['ExtensionPropertyApiDto']:
                return ExtensionPropertyApiDto
        
            @staticmethod
            def ui() -> typing.Type['ExtensionPropertyUiDto']:
                return ExtensionPropertyUiDto
            
            
            class attributes(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ExtensionPropertyAttributeDto']:
                        return ExtensionPropertyAttributeDto
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ExtensionPropertyAttributeDto'], typing.List['ExtensionPropertyAttributeDto']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'attributes':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ExtensionPropertyAttributeDto':
                    return super().__getitem__(i)
            
            
            class configuration(
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
                ) -> 'configuration':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            defaultValue = schemas.DictSchema
            __annotations__ = {
                "type": type,
                "typeSimple": typeSimple,
                "displayName": displayName,
                "api": api,
                "ui": ui,
                "attributes": attributes,
                "configuration": configuration,
                "defaultValue": defaultValue,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["typeSimple"]) -> MetaOapg.properties.typeSimple: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["displayName"]) -> 'LocalizableStringDto': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["api"]) -> 'ExtensionPropertyApiDto': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ui"]) -> 'ExtensionPropertyUiDto': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attributes"]) -> MetaOapg.properties.attributes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["configuration"]) -> MetaOapg.properties.configuration: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["defaultValue"]) -> MetaOapg.properties.defaultValue: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "typeSimple", "displayName", "api", "ui", "attributes", "configuration", "defaultValue", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["typeSimple"]) -> typing.Union[MetaOapg.properties.typeSimple, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["displayName"]) -> typing.Union['LocalizableStringDto', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["api"]) -> typing.Union['ExtensionPropertyApiDto', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ui"]) -> typing.Union['ExtensionPropertyUiDto', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attributes"]) -> typing.Union[MetaOapg.properties.attributes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["configuration"]) -> typing.Union[MetaOapg.properties.configuration, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["defaultValue"]) -> typing.Union[MetaOapg.properties.defaultValue, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "typeSimple", "displayName", "api", "ui", "attributes", "configuration", "defaultValue", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        typeSimple: typing.Union[MetaOapg.properties.typeSimple, str, schemas.Unset] = schemas.unset,
        displayName: typing.Union['LocalizableStringDto', schemas.Unset] = schemas.unset,
        api: typing.Union['ExtensionPropertyApiDto', schemas.Unset] = schemas.unset,
        ui: typing.Union['ExtensionPropertyUiDto', schemas.Unset] = schemas.unset,
        attributes: typing.Union[MetaOapg.properties.attributes, list, tuple, schemas.Unset] = schemas.unset,
        configuration: typing.Union[MetaOapg.properties.configuration, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        defaultValue: typing.Union[MetaOapg.properties.defaultValue, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ExtensionPropertyDto':
        return super().__new__(
            cls,
            *args,
            type=type,
            typeSimple=typeSimple,
            displayName=displayName,
            api=api,
            ui=ui,
            attributes=attributes,
            configuration=configuration,
            defaultValue=defaultValue,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.extension_property_api_dto import ExtensionPropertyApiDto
from openapi_client.model.extension_property_attribute_dto import ExtensionPropertyAttributeDto
from openapi_client.model.extension_property_ui_dto import ExtensionPropertyUiDto
from openapi_client.model.localizable_string_dto import LocalizableStringDto
