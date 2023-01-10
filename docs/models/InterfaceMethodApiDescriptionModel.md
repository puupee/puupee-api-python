# openapi_client.model.interface_method_api_description_model.InterfaceMethodApiDescriptionModel

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  |  | [optional] 
**[parametersOnMethod](#parametersOnMethod)** | list, tuple,  | tuple,  |  | [optional] 
**returnValue** | [**ReturnValueApiDescriptionModel**](ReturnValueApiDescriptionModel.md) | [**ReturnValueApiDescriptionModel**](ReturnValueApiDescriptionModel.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# parametersOnMethod

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**MethodParameterApiDescriptionModel**](MethodParameterApiDescriptionModel.md) | [**MethodParameterApiDescriptionModel**](MethodParameterApiDescriptionModel.md) | [**MethodParameterApiDescriptionModel**](MethodParameterApiDescriptionModel.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

