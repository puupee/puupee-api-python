# puupee-api.model.create_or_update_app_dto.CreateOrUpdateAppDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  |  | [optional] 
**displayName** | str,  | str,  |  | [optional] 
**framework** | str,  | str,  |  | [optional] 
**appType** | str,  | str,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**icon** | str,  | str,  |  | [optional] 
**homePage** | str,  | str,  |  | [optional] 
**sortIndex** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**gitRepository** | str,  | str,  |  | [optional] 
**gitRepositoryType** | str,  | str,  |  | [optional] 
**[features](#features)** | list, tuple,  | tuple,  |  | [optional] 
**[sdks](#sdks)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# features

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AppFeatureDto**](AppFeatureDto.md) | [**AppFeatureDto**](AppFeatureDto.md) | [**AppFeatureDto**](AppFeatureDto.md) |  | 

# sdks

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AppSdkDto**](AppSdkDto.md) | [**AppSdkDto**](AppSdkDto.md) | [**AppSdkDto**](AppSdkDto.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

