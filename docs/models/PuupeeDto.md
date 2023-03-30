# puupee-api.model.puupee_dto.PuupeeDto

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
**title** | str,  | str,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**text** | str,  | str,  |  | [optional] 
**content** | str,  | str,  |  | [optional] 
**format** | str,  | str,  |  | [optional] 
**password** | str,  | str,  |  | [optional] 
**parentId** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**key** | str,  | str,  |  | [optional] 
**url** | str,  | str,  |  | [optional] 
**size** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**md5** | str,  | str,  |  | [optional] 
**sliceMd5** | str,  | str,  |  | [optional] 
**rapidCode** | str,  | str,  |  | [optional] 
**contentType** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**displayStyle** | str,  | str,  |  | [optional] 
**extension** | str,  | str,  |  | [optional] 
**storageClass** | str,  | str,  |  | [optional] 
**storageObjectCreatedAt** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**storageObjectUpdatedAt** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**storageObjectId** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**storageObject** | [**StorageObjectDto**](StorageObjectDto.md) | [**StorageObjectDto**](StorageObjectDto.md) |  | [optional] 
**thumb** | [**StorageObjectDto**](StorageObjectDto.md) | [**StorageObjectDto**](StorageObjectDto.md) |  | [optional] 
**priority** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**doneAt** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**isDone** | bool,  | BoolClass,  |  | [optional] 
**startAt** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**endAt** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**notifyAt** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**notifyTimingType** | str,  | str,  |  | [optional] 
**notifyTimingUnit** | str,  | str,  |  | [optional] 
**notifyTimingValue** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**repeat** | str,  | str,  |  | [optional] 
**repeatOffAt** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**repeatOffTimes** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**repetitions** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**syncVersion** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**isHidden** | bool,  | BoolClass,  |  | [optional] 
**tagging** | str,  | str,  |  | [optional] 
**lastModifierDeviceToken** | str,  | str,  |  | [optional] 
**lastModifierDevice** | str,  | str,  |  | [optional] 
**app** | str,  | str,  |  | [optional] 
**sortIndex** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

