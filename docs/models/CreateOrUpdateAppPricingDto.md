# puupee-api.model.create_or_update_app_pricing_dto.CreateOrUpdateAppPricingDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**naming** | str,  | str,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**appId** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**monthPrice** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**monthDiscount** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**monthDiscountPrice** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**monthDiscountStartAt** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**monthDiscountEndAt** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**yearPrice** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**yearDiscount** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**yearDiscountPrice** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**yearDiscountStartAt** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**yearDiscountEndAt** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**[items](#items)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AppPricingItemDto**](AppPricingItemDto.md) | [**AppPricingItemDto**](AppPricingItemDto.md) | [**AppPricingItemDto**](AppPricingItemDto.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

