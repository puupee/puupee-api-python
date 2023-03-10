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


class InterfaceMethodApiDescriptionModel(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            name = schemas.StrSchema
            
            
            class parametersOnMethod(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['MethodParameterApiDescriptionModel']:
                        return MethodParameterApiDescriptionModel
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['MethodParameterApiDescriptionModel'], typing.List['MethodParameterApiDescriptionModel']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'parametersOnMethod':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'MethodParameterApiDescriptionModel':
                    return super().__getitem__(i)
        
            @staticmethod
            def returnValue() -> typing.Type['ReturnValueApiDescriptionModel']:
                return ReturnValueApiDescriptionModel
            __annotations__ = {
                "name": name,
                "parametersOnMethod": parametersOnMethod,
                "returnValue": returnValue,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parametersOnMethod"]) -> MetaOapg.properties.parametersOnMethod: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["returnValue"]) -> 'ReturnValueApiDescriptionModel': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "parametersOnMethod", "returnValue", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parametersOnMethod"]) -> typing.Union[MetaOapg.properties.parametersOnMethod, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["returnValue"]) -> typing.Union['ReturnValueApiDescriptionModel', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "parametersOnMethod", "returnValue", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        parametersOnMethod: typing.Union[MetaOapg.properties.parametersOnMethod, list, tuple, schemas.Unset] = schemas.unset,
        returnValue: typing.Union['ReturnValueApiDescriptionModel', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'InterfaceMethodApiDescriptionModel':
        return super().__new__(
            cls,
            *args,
            name=name,
            parametersOnMethod=parametersOnMethod,
            returnValue=returnValue,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.method_parameter_api_description_model import MethodParameterApiDescriptionModel
from openapi_client.model.return_value_api_description_model import ReturnValueApiDescriptionModel
