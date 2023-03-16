# puupee-api.model.app_pricing_item_dto.AppPricingItemDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**creationTime** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**creatorId** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**lastModificationTime** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**lastModifierId** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**isDeleted** | bool,  | BoolClass,  |  | [optional] 
**deleterId** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**deletionTime** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**name** | str,  | str,  |  | [optional] 
**display** | str,  | str,  |  | [optional] 
**[values](#values)** | list, tuple,  | tuple,  |  | [optional] 
**appId** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**isAvailable** | bool,  | BoolClass,  |  | [optional] 
**hasValue** | bool,  | BoolClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# values

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

