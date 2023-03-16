# puupee-api.model.controller_api_description_model.ControllerApiDescriptionModel

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**controllerName** | str,  | str,  |  | [optional] 
**controllerGroupName** | str,  | str,  |  | [optional] 
**isRemoteService** | bool,  | BoolClass,  |  | [optional] 
**isIntegrationService** | bool,  | BoolClass,  |  | [optional] 
**apiVersion** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**[interfaces](#interfaces)** | list, tuple,  | tuple,  |  | [optional] 
**[actions](#actions)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# interfaces

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ControllerInterfaceApiDescriptionModel**](ControllerInterfaceApiDescriptionModel.md) | [**ControllerInterfaceApiDescriptionModel**](ControllerInterfaceApiDescriptionModel.md) | [**ControllerInterfaceApiDescriptionModel**](ControllerInterfaceApiDescriptionModel.md) |  | 

# actions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**ActionApiDescriptionModel**](ActionApiDescriptionModel.md) | [**ActionApiDescriptionModel**](ActionApiDescriptionModel.md) | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

