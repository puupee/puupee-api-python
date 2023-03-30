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


class ModuleApiDescriptionModel(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            rootPath = schemas.StrSchema
            remoteServiceName = schemas.StrSchema
            
            
            class controllers(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def additional_properties() -> typing.Type['ControllerApiDescriptionModel']:
                        return ControllerApiDescriptionModel
                
                def __getitem__(self, name: typing.Union[str, ]) -> 'ControllerApiDescriptionModel':
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: typing.Union[str, ]) -> 'ControllerApiDescriptionModel':
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: 'ControllerApiDescriptionModel',
                ) -> 'controllers':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "rootPath": rootPath,
                "remoteServiceName": remoteServiceName,
                "controllers": controllers,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rootPath"]) -> MetaOapg.properties.rootPath: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["remoteServiceName"]) -> MetaOapg.properties.remoteServiceName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["controllers"]) -> MetaOapg.properties.controllers: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["rootPath", "remoteServiceName", "controllers", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rootPath"]) -> typing.Union[MetaOapg.properties.rootPath, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["remoteServiceName"]) -> typing.Union[MetaOapg.properties.remoteServiceName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["controllers"]) -> typing.Union[MetaOapg.properties.controllers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["rootPath", "remoteServiceName", "controllers", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        rootPath: typing.Union[MetaOapg.properties.rootPath, str, schemas.Unset] = schemas.unset,
        remoteServiceName: typing.Union[MetaOapg.properties.remoteServiceName, str, schemas.Unset] = schemas.unset,
        controllers: typing.Union[MetaOapg.properties.controllers, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ModuleApiDescriptionModel':
        return super().__new__(
            cls,
            *args,
            rootPath=rootPath,
            remoteServiceName=remoteServiceName,
            controllers=controllers,
            _configuration=_configuration,
            **kwargs,
        )

from puupee-api.model.controller_api_description_model import ControllerApiDescriptionModel
