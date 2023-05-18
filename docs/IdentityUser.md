# IdentityUser


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**extra_properties** | **dict[str, object]** |  | [optional] [readonly] 
**concurrency_stamp** | **str** |  | [optional] 
**creation_time** | **datetime** |  | [optional] 
**creator_id** | **str** |  | [optional] 
**last_modification_time** | **datetime** |  | [optional] 
**last_modifier_id** | **str** |  | [optional] 
**is_deleted** | **bool** |  | [optional] 
**deleter_id** | **str** |  | [optional] 
**deletion_time** | **datetime** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**user_name** | **str** |  | [optional] 
**normalized_user_name** | **str** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**surname** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**normalized_email** | **str** |  | [optional] [readonly] 
**email_confirmed** | **bool** |  | [optional] [readonly] 
**password_hash** | **str** |  | [optional] [readonly] 
**security_stamp** | **str** |  | [optional] [readonly] 
**is_external** | **bool** |  | [optional] 
**phone_number** | **str** |  | [optional] [readonly] 
**phone_number_confirmed** | **bool** |  | [optional] [readonly] 
**is_active** | **bool** |  | [optional] [readonly] 
**two_factor_enabled** | **bool** |  | [optional] [readonly] 
**lockout_end** | **datetime** |  | [optional] [readonly] 
**lockout_enabled** | **bool** |  | [optional] [readonly] 
**access_failed_count** | **int** |  | [optional] [readonly] 
**should_change_password_on_next_login** | **bool** |  | [optional] [readonly] 
**entity_version** | **int** |  | [optional] [readonly] 
**last_password_change_time** | **datetime** |  | [optional] [readonly] 
**roles** | [**list[IdentityUserRole]**](IdentityUserRole.md) |  | [optional] [readonly] 
**claims** | [**list[IdentityUserClaim]**](IdentityUserClaim.md) |  | [optional] [readonly] 
**logins** | [**list[IdentityUserLogin]**](IdentityUserLogin.md) |  | [optional] [readonly] 
**tokens** | [**list[IdentityUserToken]**](IdentityUserToken.md) |  | [optional] [readonly] 
**organization_units** | [**list[IdentityUserOrganizationUnit]**](IdentityUserOrganizationUnit.md) |  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


