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


class ApplicationConfigurationDto(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def localization() -> typing.Type['ApplicationLocalizationConfigurationDto']:
                return ApplicationLocalizationConfigurationDto
        
            @staticmethod
            def auth() -> typing.Type['ApplicationAuthConfigurationDto']:
                return ApplicationAuthConfigurationDto
        
            @staticmethod
            def setting() -> typing.Type['ApplicationSettingConfigurationDto']:
                return ApplicationSettingConfigurationDto
        
            @staticmethod
            def currentUser() -> typing.Type['CurrentUserDto']:
                return CurrentUserDto
        
            @staticmethod
            def features() -> typing.Type['ApplicationFeatureConfigurationDto']:
                return ApplicationFeatureConfigurationDto
        
            @staticmethod
            def globalFeatures() -> typing.Type['ApplicationGlobalFeatureConfigurationDto']:
                return ApplicationGlobalFeatureConfigurationDto
        
            @staticmethod
            def multiTenancy() -> typing.Type['MultiTenancyInfoDto']:
                return MultiTenancyInfoDto
        
            @staticmethod
            def currentTenant() -> typing.Type['CurrentTenantDto']:
                return CurrentTenantDto
        
            @staticmethod
            def timing() -> typing.Type['TimingDto']:
                return TimingDto
        
            @staticmethod
            def clock() -> typing.Type['ClockDto']:
                return ClockDto
        
            @staticmethod
            def objectExtensions() -> typing.Type['ObjectExtensionsDto']:
                return ObjectExtensionsDto
            
            
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
            __annotations__ = {
                "localization": localization,
                "auth": auth,
                "setting": setting,
                "currentUser": currentUser,
                "features": features,
                "globalFeatures": globalFeatures,
                "multiTenancy": multiTenancy,
                "currentTenant": currentTenant,
                "timing": timing,
                "clock": clock,
                "objectExtensions": objectExtensions,
                "extraProperties": extraProperties,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["localization"]) -> 'ApplicationLocalizationConfigurationDto': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["auth"]) -> 'ApplicationAuthConfigurationDto': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["setting"]) -> 'ApplicationSettingConfigurationDto': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currentUser"]) -> 'CurrentUserDto': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["features"]) -> 'ApplicationFeatureConfigurationDto': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["globalFeatures"]) -> 'ApplicationGlobalFeatureConfigurationDto': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["multiTenancy"]) -> 'MultiTenancyInfoDto': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currentTenant"]) -> 'CurrentTenantDto': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timing"]) -> 'TimingDto': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clock"]) -> 'ClockDto': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["objectExtensions"]) -> 'ObjectExtensionsDto': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["extraProperties"]) -> MetaOapg.properties.extraProperties: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["localization", "auth", "setting", "currentUser", "features", "globalFeatures", "multiTenancy", "currentTenant", "timing", "clock", "objectExtensions", "extraProperties", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["localization"]) -> typing.Union['ApplicationLocalizationConfigurationDto', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["auth"]) -> typing.Union['ApplicationAuthConfigurationDto', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["setting"]) -> typing.Union['ApplicationSettingConfigurationDto', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currentUser"]) -> typing.Union['CurrentUserDto', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["features"]) -> typing.Union['ApplicationFeatureConfigurationDto', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["globalFeatures"]) -> typing.Union['ApplicationGlobalFeatureConfigurationDto', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["multiTenancy"]) -> typing.Union['MultiTenancyInfoDto', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currentTenant"]) -> typing.Union['CurrentTenantDto', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timing"]) -> typing.Union['TimingDto', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clock"]) -> typing.Union['ClockDto', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["objectExtensions"]) -> typing.Union['ObjectExtensionsDto', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["extraProperties"]) -> typing.Union[MetaOapg.properties.extraProperties, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["localization", "auth", "setting", "currentUser", "features", "globalFeatures", "multiTenancy", "currentTenant", "timing", "clock", "objectExtensions", "extraProperties", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        localization: typing.Union['ApplicationLocalizationConfigurationDto', schemas.Unset] = schemas.unset,
        auth: typing.Union['ApplicationAuthConfigurationDto', schemas.Unset] = schemas.unset,
        setting: typing.Union['ApplicationSettingConfigurationDto', schemas.Unset] = schemas.unset,
        currentUser: typing.Union['CurrentUserDto', schemas.Unset] = schemas.unset,
        features: typing.Union['ApplicationFeatureConfigurationDto', schemas.Unset] = schemas.unset,
        globalFeatures: typing.Union['ApplicationGlobalFeatureConfigurationDto', schemas.Unset] = schemas.unset,
        multiTenancy: typing.Union['MultiTenancyInfoDto', schemas.Unset] = schemas.unset,
        currentTenant: typing.Union['CurrentTenantDto', schemas.Unset] = schemas.unset,
        timing: typing.Union['TimingDto', schemas.Unset] = schemas.unset,
        clock: typing.Union['ClockDto', schemas.Unset] = schemas.unset,
        objectExtensions: typing.Union['ObjectExtensionsDto', schemas.Unset] = schemas.unset,
        extraProperties: typing.Union[MetaOapg.properties.extraProperties, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ApplicationConfigurationDto':
        return super().__new__(
            cls,
            *args,
            localization=localization,
            auth=auth,
            setting=setting,
            currentUser=currentUser,
            features=features,
            globalFeatures=globalFeatures,
            multiTenancy=multiTenancy,
            currentTenant=currentTenant,
            timing=timing,
            clock=clock,
            objectExtensions=objectExtensions,
            extraProperties=extraProperties,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.application_auth_configuration_dto import ApplicationAuthConfigurationDto
from openapi_client.model.application_feature_configuration_dto import ApplicationFeatureConfigurationDto
from openapi_client.model.application_global_feature_configuration_dto import ApplicationGlobalFeatureConfigurationDto
from openapi_client.model.application_localization_configuration_dto import ApplicationLocalizationConfigurationDto
from openapi_client.model.application_setting_configuration_dto import ApplicationSettingConfigurationDto
from openapi_client.model.clock_dto import ClockDto
from openapi_client.model.current_tenant_dto import CurrentTenantDto
from openapi_client.model.current_user_dto import CurrentUserDto
from openapi_client.model.multi_tenancy_info_dto import MultiTenancyInfoDto
from openapi_client.model.object_extensions_dto import ObjectExtensionsDto
from openapi_client.model.timing_dto import TimingDto