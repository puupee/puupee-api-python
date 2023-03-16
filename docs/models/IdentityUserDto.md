# puupee-api.model.identity_user_dto.IdentityUserDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[extraProperties](#extraProperties)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**id** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**creationTime** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**creatorId** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**lastModificationTime** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**lastModifierId** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**isDeleted** | bool,  | BoolClass,  |  | [optional] 
**deleterId** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**deletionTime** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**tenantId** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**userName** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**surname** | str,  | str,  |  | [optional] 
**email** | str,  | str,  |  | [optional] 
**emailConfirmed** | bool,  | BoolClass,  |  | [optional] 
**phoneNumber** | str,  | str,  |  | [optional] 
**phoneNumberConfirmed** | bool,  | BoolClass,  |  | [optional] 
**isActive** | bool,  | BoolClass,  |  | [optional] 
**lockoutEnabled** | bool,  | BoolClass,  |  | [optional] 
**lockoutEnd** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**concurrencyStamp** | str,  | str,  |  | [optional] 
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

