# puupee-api.model.app_release_dto.AppReleaseDto

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
**version** | str,  | str,  |  | [optional] 
**versionName** | str,  | str,  |  | [optional] 
**versionCode** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**notes** | str,  | str,  |  | [optional] 
**platform** | str,  | str,  |  | [optional] 
**key** | str,  | str,  |  | [optional] 
**rapidCode** | str,  | str,  |  | [optional] 
**size** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**md5** | str,  | str,  |  | [optional] 
**sliceMd5** | str,  | str,  |  | [optional] 
**downloadUrl** | str,  | str,  |  | [optional] 
**productType** | str,  | str,  |  | [optional] 
**isForceUpdate** | bool,  | BoolClass,  |  | [optional] 
**appId** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**isEnabled** | bool,  | BoolClass,  |  | [optional] 
**channel** | str,  | str,  |  | [optional] 
**environment** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

