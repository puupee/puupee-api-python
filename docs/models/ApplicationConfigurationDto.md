# puupee-api.model.application_configuration_dto.ApplicationConfigurationDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**localization** | [**ApplicationLocalizationConfigurationDto**](ApplicationLocalizationConfigurationDto.md) | [**ApplicationLocalizationConfigurationDto**](ApplicationLocalizationConfigurationDto.md) |  | [optional] 
**auth** | [**ApplicationAuthConfigurationDto**](ApplicationAuthConfigurationDto.md) | [**ApplicationAuthConfigurationDto**](ApplicationAuthConfigurationDto.md) |  | [optional] 
**setting** | [**ApplicationSettingConfigurationDto**](ApplicationSettingConfigurationDto.md) | [**ApplicationSettingConfigurationDto**](ApplicationSettingConfigurationDto.md) |  | [optional] 
**currentUser** | [**CurrentUserDto**](CurrentUserDto.md) | [**CurrentUserDto**](CurrentUserDto.md) |  | [optional] 
**features** | [**ApplicationFeatureConfigurationDto**](ApplicationFeatureConfigurationDto.md) | [**ApplicationFeatureConfigurationDto**](ApplicationFeatureConfigurationDto.md) |  | [optional] 
**globalFeatures** | [**ApplicationGlobalFeatureConfigurationDto**](ApplicationGlobalFeatureConfigurationDto.md) | [**ApplicationGlobalFeatureConfigurationDto**](ApplicationGlobalFeatureConfigurationDto.md) |  | [optional] 
**multiTenancy** | [**MultiTenancyInfoDto**](MultiTenancyInfoDto.md) | [**MultiTenancyInfoDto**](MultiTenancyInfoDto.md) |  | [optional] 
**currentTenant** | [**CurrentTenantDto**](CurrentTenantDto.md) | [**CurrentTenantDto**](CurrentTenantDto.md) |  | [optional] 
**timing** | [**TimingDto**](TimingDto.md) | [**TimingDto**](TimingDto.md) |  | [optional] 
**clock** | [**ClockDto**](ClockDto.md) | [**ClockDto**](ClockDto.md) |  | [optional] 
**objectExtensions** | [**ObjectExtensionsDto**](ObjectExtensionsDto.md) | [**ObjectExtensionsDto**](ObjectExtensionsDto.md) |  | [optional] 
**[extraProperties](#extraProperties)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# extraProperties

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[any_string_name](#any_string_name)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | any string name can be used but the value must be the correct type | [optional] 

# any_string_name

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

