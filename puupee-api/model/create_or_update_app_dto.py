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


class CreateOrUpdateAppDto(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            name = schemas.StrSchema
            displayName = schemas.StrSchema
            framework = schemas.StrSchema
            appType = schemas.StrSchema
            description = schemas.StrSchema
            icon = schemas.StrSchema
            homePage = schemas.StrSchema
            sortIndex = schemas.Int32Schema
            gitRepository = schemas.StrSchema
            gitRepositoryType = schemas.StrSchema
            isEnabled = schemas.BoolSchema
            isPublished = schemas.BoolSchema
            
            
            class features(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['AppFeatureDto']:
                        return AppFeatureDto
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['AppFeatureDto'], typing.List['AppFeatureDto']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'features':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'AppFeatureDto':
                    return super().__getitem__(i)
            
            
            class sdks(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['AppSdkDto']:
                        return AppSdkDto
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['AppSdkDto'], typing.List['AppSdkDto']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'sdks':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'AppSdkDto':
                    return super().__getitem__(i)
            __annotations__ = {
                "name": name,
                "displayName": displayName,
                "framework": framework,
                "appType": appType,
                "description": description,
                "icon": icon,
                "homePage": homePage,
                "sortIndex": sortIndex,
                "gitRepository": gitRepository,
                "gitRepositoryType": gitRepositoryType,
                "isEnabled": isEnabled,
                "isPublished": isPublished,
                "features": features,
                "sdks": sdks,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["displayName"]) -> MetaOapg.properties.displayName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["framework"]) -> MetaOapg.properties.framework: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["appType"]) -> MetaOapg.properties.appType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["icon"]) -> MetaOapg.properties.icon: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["homePage"]) -> MetaOapg.properties.homePage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sortIndex"]) -> MetaOapg.properties.sortIndex: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gitRepository"]) -> MetaOapg.properties.gitRepository: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gitRepositoryType"]) -> MetaOapg.properties.gitRepositoryType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isEnabled"]) -> MetaOapg.properties.isEnabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isPublished"]) -> MetaOapg.properties.isPublished: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["features"]) -> MetaOapg.properties.features: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sdks"]) -> MetaOapg.properties.sdks: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "displayName", "framework", "appType", "description", "icon", "homePage", "sortIndex", "gitRepository", "gitRepositoryType", "isEnabled", "isPublished", "features", "sdks", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["displayName"]) -> typing.Union[MetaOapg.properties.displayName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["framework"]) -> typing.Union[MetaOapg.properties.framework, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["appType"]) -> typing.Union[MetaOapg.properties.appType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["icon"]) -> typing.Union[MetaOapg.properties.icon, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["homePage"]) -> typing.Union[MetaOapg.properties.homePage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sortIndex"]) -> typing.Union[MetaOapg.properties.sortIndex, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gitRepository"]) -> typing.Union[MetaOapg.properties.gitRepository, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gitRepositoryType"]) -> typing.Union[MetaOapg.properties.gitRepositoryType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isEnabled"]) -> typing.Union[MetaOapg.properties.isEnabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isPublished"]) -> typing.Union[MetaOapg.properties.isPublished, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["features"]) -> typing.Union[MetaOapg.properties.features, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sdks"]) -> typing.Union[MetaOapg.properties.sdks, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "displayName", "framework", "appType", "description", "icon", "homePage", "sortIndex", "gitRepository", "gitRepositoryType", "isEnabled", "isPublished", "features", "sdks", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        displayName: typing.Union[MetaOapg.properties.displayName, str, schemas.Unset] = schemas.unset,
        framework: typing.Union[MetaOapg.properties.framework, str, schemas.Unset] = schemas.unset,
        appType: typing.Union[MetaOapg.properties.appType, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        icon: typing.Union[MetaOapg.properties.icon, str, schemas.Unset] = schemas.unset,
        homePage: typing.Union[MetaOapg.properties.homePage, str, schemas.Unset] = schemas.unset,
        sortIndex: typing.Union[MetaOapg.properties.sortIndex, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        gitRepository: typing.Union[MetaOapg.properties.gitRepository, str, schemas.Unset] = schemas.unset,
        gitRepositoryType: typing.Union[MetaOapg.properties.gitRepositoryType, str, schemas.Unset] = schemas.unset,
        isEnabled: typing.Union[MetaOapg.properties.isEnabled, bool, schemas.Unset] = schemas.unset,
        isPublished: typing.Union[MetaOapg.properties.isPublished, bool, schemas.Unset] = schemas.unset,
        features: typing.Union[MetaOapg.properties.features, list, tuple, schemas.Unset] = schemas.unset,
        sdks: typing.Union[MetaOapg.properties.sdks, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateOrUpdateAppDto':
        return super().__new__(
            cls,
            *args,
            name=name,
            displayName=displayName,
            framework=framework,
            appType=appType,
            description=description,
            icon=icon,
            homePage=homePage,
            sortIndex=sortIndex,
            gitRepository=gitRepository,
            gitRepositoryType=gitRepositoryType,
            isEnabled=isEnabled,
            isPublished=isPublished,
            features=features,
            sdks=sdks,
            _configuration=_configuration,
            **kwargs,
        )

from puupee-api.model.app_feature_dto import AppFeatureDto
from puupee-api.model.app_sdk_dto import AppSdkDto
