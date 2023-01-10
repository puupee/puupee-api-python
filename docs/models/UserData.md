# openapi_client.model.user_data.UserData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**tenantId** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**userName** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**surname** | str,  | str,  |  | [optional] 
**isActive** | bool,  | BoolClass,  |  | [optional] 
**email** | str,  | str,  |  | [optional] 
**emailConfirmed** | bool,  | BoolClass,  |  | [optional] 
**phoneNumber** | str,  | str,  |  | [optional] 
**phoneNumberConfirmed** | bool,  | BoolClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

