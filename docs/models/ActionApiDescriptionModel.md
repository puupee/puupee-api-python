# openapi_client.model.action_api_description_model.ActionApiDescriptionModel

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**uniqueName** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**httpMethod** | str,  | str,  |  | [optional] 
**url** | str,  | str,  |  | [optional] 
**[supportedVersions](#supportedVersions)** | list, tuple,  | tuple,  |  | [optional] 
**[parametersOnMethod](#parametersOnMethod)** | list, tuple,  | tuple,  |  | [optional] 
**[parameters](#parameters)** | list, tuple,  | tuple,  |  | [optional] 
**returnValue** | [**ReturnValueApiDescriptionModel**](ReturnValueApiDescriptionModel.md) | [**ReturnValueApiDescriptionModel**](ReturnValueApiDescriptionModel.md) |  | [optional] 
**allowAnonymous** | bool,  | BoolClass,  |  | [optional] 
**implementFrom** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# supportedVersions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# parametersOnMethod

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**MethodParameterApiDescriptionModel**](MethodParameterApiDescriptionModel.md) | [**MethodParameterApiDescriptionModel**](MethodParameterApiDescriptionModel.md) | [**MethodParameterApiDescriptionModel**](MethodParameterApiDescriptionModel.md) |  | 

# parameters

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ParameterApiDescriptionModel**](ParameterApiDescriptionModel.md) | [**ParameterApiDescriptionModel**](ParameterApiDescriptionModel.md) | [**ParameterApiDescriptionModel**](ParameterApiDescriptionModel.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

