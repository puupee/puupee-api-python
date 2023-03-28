# puupee-api
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0+3
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python &gt;&#x3D;3.7

## Migration from other generators like python and python-legacy

### Changes
1. This generator uses spec case for all (object) property names and parameter names.
    - So if the spec has a property name like camelCase, it will use camelCase rather than camel_case
    - So you will need to update how you input and read properties to use spec case
2. Endpoint parameters are stored in dictionaries to prevent collisions (explanation below)
    - So you will need to update how you pass data in to endpoints
3. Endpoint responses now include the original response, the deserialized response body, and (todo)the deserialized headers
    - So you will need to update your code to use response.body to access deserialized data
4. All validated data is instantiated in an instance that subclasses all validated Schema classes and Decimal/str/list/tuple/frozendict/NoneClass/BoolClass/bytes/io.FileIO
    - This means that you can use isinstance to check if a payload validated against a schema class
    - This means that no data will be of type None/True/False
        - ingested None will subclass NoneClass
        - ingested True will subclass BoolClass
        - ingested False will subclass BoolClass
        - So if you need to check is True/False/None, instead use instance.is_true_oapg()/.is_false_oapg()/.is_none_oapg()
5. All validated class instances are immutable except for ones based on io.File
    - This is because if properties were changed after validation, that validation would no longer apply
    - So no changing values or property values after a class has been instantiated
6. String + Number types with formats
    - String type data is stored as a string and if you need to access types based on its format like date,
    date-time, uuid, number etc then you will need to use accessor functions on the instance
    - type string + format: See .as_date_oapg, .as_datetime_oapg, .as_decimal_oapg, .as_uuid_oapg
    - type number + format: See .as_float_oapg, .as_int_oapg
    - this was done because openapi/json-schema defines constraints. string data may be type string with no format
    keyword in one schema, and include a format constraint in another schema
    - So if you need to access a string format based type, use as_date_oapg/as_datetime_oapg/as_decimal_oapg/as_uuid_oapg
    - So if you need to access a number format based type, use as_int_oapg/as_float_oapg
7. Property access on AnyType(type unset) or object(dict) schemas
    - Only required keys with valid python names are properties like .someProp and have type hints
    - All optional keys may not exist, so properties are not defined for them
    - One can access optional values with dict_instance['optionalProp'] and KeyError will be raised if it does not exist
    - Use get_item_oapg if you need a way to always get a value whether or not the key exists
        - If the key does not exist, schemas.unset is returned from calling dict_instance.get_item_oapg('optionalProp')
        - All required and optional keys have type hints for this method, and @typing.overload is used
        - A type hint is also generated for additionalProperties accessed using this method
    - So you will need to update you code to use some_instance['optionalProp'] to access optional property
    and additionalProperty values
8. The location of the api classes has changed
    - Api classes are located in your_package.apis.tags.some_api
    - This change was made to eliminate redundant code generation
    - Legacy generators generated the same endpoint twice if it had > 1 tag on it
    - This generator defines an endpoint in one class, then inherits that class to generate
      apis by tags and by paths
    - This change reduces code and allows quicker run time if you use the path apis
        - path apis are at your_package.apis.paths.some_path
    - Those apis will only load their needed models, which is less to load than all of the resources needed in a tag api
    - So you will need to update your import paths to the api classes

### Why are Oapg and _oapg used in class and method names?
Classes can have arbitrarily named properties set on them
Endpoints can have arbitrary operationId method names set
For those reasons, I use the prefix Oapg and _oapg to greatly reduce the likelihood of collisions
on protected + public classes/methods.
oapg stands for OpenApi Python Generator.

### Object property spec case
This was done because when payloads are ingested, they can be validated against N number of schemas.
If the input signature used a different property name then that has mutated the payload.
So SchemaA and SchemaB must both see the camelCase spec named variable.
Also it is possible to send in two properties, named camelCase and camel_case in the same payload.
That use case should be support so spec case is used.

### Parameter spec case
Parameters can be included in different locations including:
- query
- path
- header
- cookie

Any of those parameters could use the same parameter names, so if every parameter
was included as an endpoint parameter in a function signature, they would collide.
For that reason, each of those inputs have been separated out into separate typed dictionaries:
- query_params
- path_params
- header_params
- cookie_params

So when updating your code, you will need to pass endpoint parameters in using those
dictionaries.

### Endpoint responses
Endpoint responses have been enriched to now include more information.
Any response reom an endpoint will now include the following properties:
response: urllib3.HTTPResponse
body: typing.Union[Unset, Schema]
headers: typing.Union[Unset, TODO]
Note: response header deserialization has not yet been added


## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/puupee/puupee-api-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/puupee/puupee-api-python.git`)

Then import the package:
```python
import puupee-api
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import puupee-api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import puupee-api
from pprint import pprint
from puupee-api.apis.tags import abp_api_definition_api
from puupee-api.model.application_api_description_model import ApplicationApiDescriptionModel
from puupee-api.model.remote_service_error_response import RemoteServiceErrorResponse
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = puupee-api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = puupee-api.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with puupee-api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = abp_api_definition_api.AbpApiDefinitionApi(api_client)
    include_types = True # bool |  (optional)

    try:
        api_response = api_instance.api_abp_api_definition_get(include_types=include_types)
        pprint(api_response)
    except puupee-api.ApiException as e:
        print("Exception when calling AbpApiDefinitionApi->api_abp_api_definition_get: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AbpApiDefinitionApi* | [**api_abp_api_definition_get**](docs/apis/tags/AbpApiDefinitionApi.md#api_abp_api_definition_get) | **get** /api/abp/api-definition | 
*AbpApplicationConfigurationApi* | [**api_abp_application_configuration_get**](docs/apis/tags/AbpApplicationConfigurationApi.md#api_abp_application_configuration_get) | **get** /api/abp/application-configuration | 
*AbpApplicationLocalizationApi* | [**api_abp_application_localization_get**](docs/apis/tags/AbpApplicationLocalizationApi.md#api_abp_application_localization_get) | **get** /api/abp/application-localization | 
*AbpTenantApi* | [**api_abp_multi_tenancy_tenants_by_id_id_get**](docs/apis/tags/AbpTenantApi.md#api_abp_multi_tenancy_tenants_by_id_id_get) | **get** /api/abp/multi-tenancy/tenants/by-id/{id} | 
*AbpTenantApi* | [**api_abp_multi_tenancy_tenants_by_name_name_get**](docs/apis/tags/AbpTenantApi.md#api_abp_multi_tenancy_tenants_by_name_name_get) | **get** /api/abp/multi-tenancy/tenants/by-name/{name} | 
*AccountApi* | [**api_account_register_post**](docs/apis/tags/AccountApi.md#api_account_register_post) | **post** /api/account/register | 
*AccountApi* | [**api_account_reset_password_post**](docs/apis/tags/AccountApi.md#api_account_reset_password_post) | **post** /api/account/reset-password | 
*AccountApi* | [**api_account_send_password_reset_code_post**](docs/apis/tags/AccountApi.md#api_account_send_password_reset_code_post) | **post** /api/account/send-password-reset-code | 
*AccountApi* | [**api_account_verify_password_reset_token_post**](docs/apis/tags/AccountApi.md#api_account_verify_password_reset_token_post) | **post** /api/account/verify-password-reset-token | 
*AccountApi* | [**api_app_account_delete**](docs/apis/tags/AccountApi.md#api_app_account_delete) | **delete** /api/app/account | 
*AppApi* | [**api_app_app_by_developer_all_get**](docs/apis/tags/AppApi.md#api_app_app_by_developer_all_get) | **get** /api/app/app/by-developer-all | 
*AppApi* | [**api_app_app_by_developer_get**](docs/apis/tags/AppApi.md#api_app_app_by_developer_get) | **get** /api/app/app/by-developer | 
*AppApi* | [**api_app_app_by_name_get**](docs/apis/tags/AppApi.md#api_app_app_by_name_get) | **get** /api/app/app/by-name | 
*AppApi* | [**api_app_app_get**](docs/apis/tags/AppApi.md#api_app_app_get) | **get** /api/app/app | 
*AppApi* | [**api_app_app_id_delete**](docs/apis/tags/AppApi.md#api_app_app_id_delete) | **delete** /api/app/app/{id} | 
*AppApi* | [**api_app_app_id_get**](docs/apis/tags/AppApi.md#api_app_app_id_get) | **get** /api/app/app/{id} | 
*AppApi* | [**api_app_app_id_put**](docs/apis/tags/AppApi.md#api_app_app_id_put) | **put** /api/app/app/{id} | 
*AppApi* | [**api_app_app_post**](docs/apis/tags/AppApi.md#api_app_app_post) | **post** /api/app/app | 
*AppApi* | [**api_app_app_upload_credentials_get**](docs/apis/tags/AppApi.md#api_app_app_upload_credentials_get) | **get** /api/app/app/upload-credentials | 
*AppFeatureApi* | [**api_app_app_feature_get**](docs/apis/tags/AppFeatureApi.md#api_app_app_feature_get) | **get** /api/app/app-feature | 
*AppFeatureApi* | [**api_app_app_feature_id_delete**](docs/apis/tags/AppFeatureApi.md#api_app_app_feature_id_delete) | **delete** /api/app/app-feature/{id} | 
*AppFeatureApi* | [**api_app_app_feature_id_put**](docs/apis/tags/AppFeatureApi.md#api_app_app_feature_id_put) | **put** /api/app/app-feature/{id} | 
*AppFeatureApi* | [**api_app_app_feature_post**](docs/apis/tags/AppFeatureApi.md#api_app_app_feature_post) | **post** /api/app/app-feature | 
*AppPricingApi* | [**api_app_app_pricing_by_app_id_app_id_get**](docs/apis/tags/AppPricingApi.md#api_app_app_pricing_by_app_id_app_id_get) | **get** /api/app/app-pricing/by-app-id/{appId} | 
*AppPricingApi* | [**api_app_app_pricing_get**](docs/apis/tags/AppPricingApi.md#api_app_app_pricing_get) | **get** /api/app/app-pricing | 
*AppPricingApi* | [**api_app_app_pricing_id_delete**](docs/apis/tags/AppPricingApi.md#api_app_app_pricing_id_delete) | **delete** /api/app/app-pricing/{id} | 
*AppPricingApi* | [**api_app_app_pricing_id_get**](docs/apis/tags/AppPricingApi.md#api_app_app_pricing_id_get) | **get** /api/app/app-pricing/{id} | 
*AppPricingApi* | [**api_app_app_pricing_id_put**](docs/apis/tags/AppPricingApi.md#api_app_app_pricing_id_put) | **put** /api/app/app-pricing/{id} | 
*AppPricingApi* | [**api_app_app_pricing_post**](docs/apis/tags/AppPricingApi.md#api_app_app_pricing_post) | **post** /api/app/app-pricing | 
*AppPricingItemApi* | [**api_app_app_pricing_item_get**](docs/apis/tags/AppPricingItemApi.md#api_app_app_pricing_item_get) | **get** /api/app/app-pricing-item | 
*AppPricingItemApi* | [**api_app_app_pricing_item_id_delete**](docs/apis/tags/AppPricingItemApi.md#api_app_app_pricing_item_id_delete) | **delete** /api/app/app-pricing-item/{id} | 
*AppPricingItemApi* | [**api_app_app_pricing_item_id_get**](docs/apis/tags/AppPricingItemApi.md#api_app_app_pricing_item_id_get) | **get** /api/app/app-pricing-item/{id} | 
*AppPricingItemApi* | [**api_app_app_pricing_item_id_put**](docs/apis/tags/AppPricingItemApi.md#api_app_app_pricing_item_id_put) | **put** /api/app/app-pricing-item/{id} | 
*AppPricingItemApi* | [**api_app_app_pricing_item_post**](docs/apis/tags/AppPricingItemApi.md#api_app_app_pricing_item_post) | **post** /api/app/app-pricing-item | 
*AppReleaseApi* | [**api_app_app_release_get**](docs/apis/tags/AppReleaseApi.md#api_app_app_release_get) | **get** /api/app/app-release | 
*AppReleaseApi* | [**api_app_app_release_id_delete**](docs/apis/tags/AppReleaseApi.md#api_app_app_release_id_delete) | **delete** /api/app/app-release/{id} | 
*AppReleaseApi* | [**api_app_app_release_id_get**](docs/apis/tags/AppReleaseApi.md#api_app_app_release_id_get) | **get** /api/app/app-release/{id} | 
*AppReleaseApi* | [**api_app_app_release_id_put**](docs/apis/tags/AppReleaseApi.md#api_app_app_release_id_put) | **put** /api/app/app-release/{id} | 
*AppReleaseApi* | [**api_app_app_release_latest_get**](docs/apis/tags/AppReleaseApi.md#api_app_app_release_latest_get) | **get** /api/app/app-release/latest | 
*AppReleaseApi* | [**api_app_app_release_post**](docs/apis/tags/AppReleaseApi.md#api_app_app_release_post) | **post** /api/app/app-release | 
*AppSdkApi* | [**api_app_app_sdk_get**](docs/apis/tags/AppSdkApi.md#api_app_app_sdk_get) | **get** /api/app/app-sdk | 
*AppSdkApi* | [**api_app_app_sdk_id_delete**](docs/apis/tags/AppSdkApi.md#api_app_app_sdk_id_delete) | **delete** /api/app/app-sdk/{id} | 
*AppSdkApi* | [**api_app_app_sdk_id_put**](docs/apis/tags/AppSdkApi.md#api_app_app_sdk_id_put) | **put** /api/app/app-sdk/{id} | 
*AppSdkApi* | [**api_app_app_sdk_post**](docs/apis/tags/AppSdkApi.md#api_app_app_sdk_post) | **post** /api/app/app-sdk | 
*AppUserScoreApi* | [**api_app_app_user_score_post**](docs/apis/tags/AppUserScoreApi.md#api_app_app_user_score_post) | **post** /api/app/app-user-score | 
*DeviceApi* | [**api_app_device_bind_post**](docs/apis/tags/DeviceApi.md#api_app_device_bind_post) | **post** /api/app/device/bind | 
*DeviceApi* | [**api_app_device_delete**](docs/apis/tags/DeviceApi.md#api_app_device_delete) | **delete** /api/app/device | 
*DeviceApi* | [**api_app_device_get**](docs/apis/tags/DeviceApi.md#api_app_device_get) | **get** /api/app/device | 
*DeviceApi* | [**api_app_device_refresh_post**](docs/apis/tags/DeviceApi.md#api_app_device_refresh_post) | **post** /api/app/device/refresh | 
*EmailSettingsApi* | [**api_setting_management_emailing_get**](docs/apis/tags/EmailSettingsApi.md#api_setting_management_emailing_get) | **get** /api/setting-management/emailing | 
*EmailSettingsApi* | [**api_setting_management_emailing_post**](docs/apis/tags/EmailSettingsApi.md#api_setting_management_emailing_post) | **post** /api/setting-management/emailing | 
*EmailSettingsApi* | [**api_setting_management_emailing_send_test_email_post**](docs/apis/tags/EmailSettingsApi.md#api_setting_management_emailing_send_test_email_post) | **post** /api/setting-management/emailing/send-test-email | 
*FeaturesApi* | [**api_feature_management_features_delete**](docs/apis/tags/FeaturesApi.md#api_feature_management_features_delete) | **delete** /api/feature-management/features | 
*FeaturesApi* | [**api_feature_management_features_get**](docs/apis/tags/FeaturesApi.md#api_feature_management_features_get) | **get** /api/feature-management/features | 
*FeaturesApi* | [**api_feature_management_features_put**](docs/apis/tags/FeaturesApi.md#api_feature_management_features_put) | **put** /api/feature-management/features | 
*KeyValueApi* | [**api_app_key_value_bool_get**](docs/apis/tags/KeyValueApi.md#api_app_key_value_bool_get) | **get** /api/app/key-value/bool | 
*KeyValueApi* | [**api_app_key_value_date_time_get**](docs/apis/tags/KeyValueApi.md#api_app_key_value_date_time_get) | **get** /api/app/key-value/date-time | 
*KeyValueApi* | [**api_app_key_value_decimal_get**](docs/apis/tags/KeyValueApi.md#api_app_key_value_decimal_get) | **get** /api/app/key-value/decimal | 
*KeyValueApi* | [**api_app_key_value_double_get**](docs/apis/tags/KeyValueApi.md#api_app_key_value_double_get) | **get** /api/app/key-value/double | 
*KeyValueApi* | [**api_app_key_value_int_get**](docs/apis/tags/KeyValueApi.md#api_app_key_value_int_get) | **get** /api/app/key-value/int | 
*KeyValueApi* | [**api_app_key_value_set_bool_post**](docs/apis/tags/KeyValueApi.md#api_app_key_value_set_bool_post) | **post** /api/app/key-value/set-bool | 
*KeyValueApi* | [**api_app_key_value_set_date_time_post**](docs/apis/tags/KeyValueApi.md#api_app_key_value_set_date_time_post) | **post** /api/app/key-value/set-date-time | 
*KeyValueApi* | [**api_app_key_value_set_decimal_post**](docs/apis/tags/KeyValueApi.md#api_app_key_value_set_decimal_post) | **post** /api/app/key-value/set-decimal | 
*KeyValueApi* | [**api_app_key_value_set_double_post**](docs/apis/tags/KeyValueApi.md#api_app_key_value_set_double_post) | **post** /api/app/key-value/set-double | 
*KeyValueApi* | [**api_app_key_value_set_int_post**](docs/apis/tags/KeyValueApi.md#api_app_key_value_set_int_post) | **post** /api/app/key-value/set-int | 
*KeyValueApi* | [**api_app_key_value_set_string_post**](docs/apis/tags/KeyValueApi.md#api_app_key_value_set_string_post) | **post** /api/app/key-value/set-string | 
*KeyValueApi* | [**api_app_key_value_string_get**](docs/apis/tags/KeyValueApi.md#api_app_key_value_string_get) | **get** /api/app/key-value/string | 
*LoginApi* | [**api_account_check_password_post**](docs/apis/tags/LoginApi.md#api_account_check_password_post) | **post** /api/account/check-password | 
*LoginApi* | [**api_account_login_post**](docs/apis/tags/LoginApi.md#api_account_login_post) | **post** /api/account/login | 
*LoginApi* | [**api_account_logout_get**](docs/apis/tags/LoginApi.md#api_account_logout_get) | **get** /api/account/logout | 
*PermissionsApi* | [**api_permission_management_permissions_get**](docs/apis/tags/PermissionsApi.md#api_permission_management_permissions_get) | **get** /api/permission-management/permissions | 
*PermissionsApi* | [**api_permission_management_permissions_put**](docs/apis/tags/PermissionsApi.md#api_permission_management_permissions_put) | **put** /api/permission-management/permissions | 
*ProfileApi* | [**api_account_my_profile_change_password_post**](docs/apis/tags/ProfileApi.md#api_account_my_profile_change_password_post) | **post** /api/account/my-profile/change-password | 
*ProfileApi* | [**api_account_my_profile_get**](docs/apis/tags/ProfileApi.md#api_account_my_profile_get) | **get** /api/account/my-profile | 
*ProfileApi* | [**api_account_my_profile_put**](docs/apis/tags/ProfileApi.md#api_account_my_profile_put) | **put** /api/account/my-profile | 
*PuupeeApi* | [**api_app_puupee_pull_get**](docs/apis/tags/PuupeeApi.md#api_app_puupee_pull_get) | **get** /api/app/puupee/pull | 
*PuupeeApi* | [**api_app_puupee_push_post**](docs/apis/tags/PuupeeApi.md#api_app_puupee_push_post) | **post** /api/app/puupee/push | 
*RoleApi* | [**api_identity_roles_all_get**](docs/apis/tags/RoleApi.md#api_identity_roles_all_get) | **get** /api/identity/roles/all | 
*RoleApi* | [**api_identity_roles_get**](docs/apis/tags/RoleApi.md#api_identity_roles_get) | **get** /api/identity/roles | 
*RoleApi* | [**api_identity_roles_id_delete**](docs/apis/tags/RoleApi.md#api_identity_roles_id_delete) | **delete** /api/identity/roles/{id} | 
*RoleApi* | [**api_identity_roles_id_get**](docs/apis/tags/RoleApi.md#api_identity_roles_id_get) | **get** /api/identity/roles/{id} | 
*RoleApi* | [**api_identity_roles_id_put**](docs/apis/tags/RoleApi.md#api_identity_roles_id_put) | **put** /api/identity/roles/{id} | 
*RoleApi* | [**api_identity_roles_post**](docs/apis/tags/RoleApi.md#api_identity_roles_post) | **post** /api/identity/roles | 
*SettingsApi* | [**api_app_settings_get**](docs/apis/tags/SettingsApi.md#api_app_settings_get) | **get** /api/app/settings | 
*SettingsApi* | [**api_app_settings_set_post**](docs/apis/tags/SettingsApi.md#api_app_settings_set_post) | **post** /api/app/settings/set | 
*SimpleDataApi* | [**api_app_simple_data_get**](docs/apis/tags/SimpleDataApi.md#api_app_simple_data_get) | **get** /api/app/simple-data | 
*SimpleDataApi* | [**api_app_simple_data_id_delete**](docs/apis/tags/SimpleDataApi.md#api_app_simple_data_id_delete) | **delete** /api/app/simple-data/{id} | 
*SimpleDataApi* | [**api_app_simple_data_id_get**](docs/apis/tags/SimpleDataApi.md#api_app_simple_data_id_get) | **get** /api/app/simple-data/{id} | 
*SimpleDataApi* | [**api_app_simple_data_save_post**](docs/apis/tags/SimpleDataApi.md#api_app_simple_data_save_post) | **post** /api/app/simple-data/save | 
*StorageObjectApi* | [**api_app_storage_object_file_get**](docs/apis/tags/StorageObjectApi.md#api_app_storage_object_file_get) | **get** /api/app/storage-object/file | 
*StorageObjectApi* | [**api_app_storage_object_file_or_credentials_get**](docs/apis/tags/StorageObjectApi.md#api_app_storage_object_file_or_credentials_get) | **get** /api/app/storage-object/file-or-credentials | 
*StorageObjectApi* | [**api_app_storage_object_pre_sign_url_post**](docs/apis/tags/StorageObjectApi.md#api_app_storage_object_pre_sign_url_post) | **post** /api/app/storage-object/pre-sign-url | 
*StorageObjectApi* | [**api_app_storage_object_thumb_get**](docs/apis/tags/StorageObjectApi.md#api_app_storage_object_thumb_get) | **get** /api/app/storage-object/thumb | 
*SubscriptionApi* | [**api_app_subscription_verify_apple_post**](docs/apis/tags/SubscriptionApi.md#api_app_subscription_verify_apple_post) | **post** /api/app/subscription/verify-apple | 
*SyncStateApi* | [**api_app_sync_state_get**](docs/apis/tags/SyncStateApi.md#api_app_sync_state_get) | **get** /api/app/sync-state | 
*SyncStateApi* | [**api_app_sync_state_puupee_changed_eto_post**](docs/apis/tags/SyncStateApi.md#api_app_sync_state_puupee_changed_eto_post) | **post** /api/app/sync-state/puupee-changed-eto | 
*TenantApi* | [**api_multi_tenancy_tenants_get**](docs/apis/tags/TenantApi.md#api_multi_tenancy_tenants_get) | **get** /api/multi-tenancy/tenants | 
*TenantApi* | [**api_multi_tenancy_tenants_id_default_connection_string_delete**](docs/apis/tags/TenantApi.md#api_multi_tenancy_tenants_id_default_connection_string_delete) | **delete** /api/multi-tenancy/tenants/{id}/default-connection-string | 
*TenantApi* | [**api_multi_tenancy_tenants_id_default_connection_string_get**](docs/apis/tags/TenantApi.md#api_multi_tenancy_tenants_id_default_connection_string_get) | **get** /api/multi-tenancy/tenants/{id}/default-connection-string | 
*TenantApi* | [**api_multi_tenancy_tenants_id_default_connection_string_put**](docs/apis/tags/TenantApi.md#api_multi_tenancy_tenants_id_default_connection_string_put) | **put** /api/multi-tenancy/tenants/{id}/default-connection-string | 
*TenantApi* | [**api_multi_tenancy_tenants_id_delete**](docs/apis/tags/TenantApi.md#api_multi_tenancy_tenants_id_delete) | **delete** /api/multi-tenancy/tenants/{id} | 
*TenantApi* | [**api_multi_tenancy_tenants_id_get**](docs/apis/tags/TenantApi.md#api_multi_tenancy_tenants_id_get) | **get** /api/multi-tenancy/tenants/{id} | 
*TenantApi* | [**api_multi_tenancy_tenants_id_put**](docs/apis/tags/TenantApi.md#api_multi_tenancy_tenants_id_put) | **put** /api/multi-tenancy/tenants/{id} | 
*TenantApi* | [**api_multi_tenancy_tenants_post**](docs/apis/tags/TenantApi.md#api_multi_tenancy_tenants_post) | **post** /api/multi-tenancy/tenants | 
*TestApi* | [**api_test_datetime_get**](docs/apis/tags/TestApi.md#api_test_datetime_get) | **get** /api/Test/datetime | 
*UserApi* | [**api_identity_users_assignable_roles_get**](docs/apis/tags/UserApi.md#api_identity_users_assignable_roles_get) | **get** /api/identity/users/assignable-roles | 
*UserApi* | [**api_identity_users_by_email_email_get**](docs/apis/tags/UserApi.md#api_identity_users_by_email_email_get) | **get** /api/identity/users/by-email/{email} | 
*UserApi* | [**api_identity_users_by_username_user_name_get**](docs/apis/tags/UserApi.md#api_identity_users_by_username_user_name_get) | **get** /api/identity/users/by-username/{userName} | 
*UserApi* | [**api_identity_users_get**](docs/apis/tags/UserApi.md#api_identity_users_get) | **get** /api/identity/users | 
*UserApi* | [**api_identity_users_id_delete**](docs/apis/tags/UserApi.md#api_identity_users_id_delete) | **delete** /api/identity/users/{id} | 
*UserApi* | [**api_identity_users_id_get**](docs/apis/tags/UserApi.md#api_identity_users_id_get) | **get** /api/identity/users/{id} | 
*UserApi* | [**api_identity_users_id_put**](docs/apis/tags/UserApi.md#api_identity_users_id_put) | **put** /api/identity/users/{id} | 
*UserApi* | [**api_identity_users_id_roles_get**](docs/apis/tags/UserApi.md#api_identity_users_id_roles_get) | **get** /api/identity/users/{id}/roles | 
*UserApi* | [**api_identity_users_id_roles_put**](docs/apis/tags/UserApi.md#api_identity_users_id_roles_put) | **put** /api/identity/users/{id}/roles | 
*UserApi* | [**api_identity_users_post**](docs/apis/tags/UserApi.md#api_identity_users_post) | **post** /api/identity/users | 
*UserLookupApi* | [**api_identity_users_lookup_by_username_user_name_get**](docs/apis/tags/UserLookupApi.md#api_identity_users_lookup_by_username_user_name_get) | **get** /api/identity/users/lookup/by-username/{userName} | 
*UserLookupApi* | [**api_identity_users_lookup_count_get**](docs/apis/tags/UserLookupApi.md#api_identity_users_lookup_count_get) | **get** /api/identity/users/lookup/count | 
*UserLookupApi* | [**api_identity_users_lookup_id_get**](docs/apis/tags/UserLookupApi.md#api_identity_users_lookup_id_get) | **get** /api/identity/users/lookup/{id} | 
*UserLookupApi* | [**api_identity_users_lookup_search_get**](docs/apis/tags/UserLookupApi.md#api_identity_users_lookup_search_get) | **get** /api/identity/users/lookup/search | 
*UserStorageApi* | [**api_app_user_storage_get**](docs/apis/tags/UserStorageApi.md#api_app_user_storage_get) | **get** /api/app/user-storage | 
*VerificationApi* | [**api_app_verification_send_code_post**](docs/apis/tags/VerificationApi.md#api_app_verification_send_code_post) | **post** /api/app/verification/send-code | 

## Documentation For Models

 - [AbpLoginResult](docs/models/AbpLoginResult.md)
 - [ActionApiDescriptionModel](docs/models/ActionApiDescriptionModel.md)
 - [AppDto](docs/models/AppDto.md)
 - [AppDtoPagedResultDto](docs/models/AppDtoPagedResultDto.md)
 - [AppFeatureDto](docs/models/AppFeatureDto.md)
 - [AppPricingDto](docs/models/AppPricingDto.md)
 - [AppPricingDtoPagedResultDto](docs/models/AppPricingDtoPagedResultDto.md)
 - [AppPricingItemDto](docs/models/AppPricingItemDto.md)
 - [AppReleaseDto](docs/models/AppReleaseDto.md)
 - [AppReleaseDtoPagedResultDto](docs/models/AppReleaseDtoPagedResultDto.md)
 - [AppSdkDto](docs/models/AppSdkDto.md)
 - [AppTheme](docs/models/AppTheme.md)
 - [AppThemeMode](docs/models/AppThemeMode.md)
 - [AppUserScoreDto](docs/models/AppUserScoreDto.md)
 - [ApplicationApiDescriptionModel](docs/models/ApplicationApiDescriptionModel.md)
 - [ApplicationAuthConfigurationDto](docs/models/ApplicationAuthConfigurationDto.md)
 - [ApplicationConfigurationDto](docs/models/ApplicationConfigurationDto.md)
 - [ApplicationFeatureConfigurationDto](docs/models/ApplicationFeatureConfigurationDto.md)
 - [ApplicationGlobalFeatureConfigurationDto](docs/models/ApplicationGlobalFeatureConfigurationDto.md)
 - [ApplicationLocalizationConfigurationDto](docs/models/ApplicationLocalizationConfigurationDto.md)
 - [ApplicationLocalizationDto](docs/models/ApplicationLocalizationDto.md)
 - [ApplicationLocalizationResourceDto](docs/models/ApplicationLocalizationResourceDto.md)
 - [ApplicationSettingConfigurationDto](docs/models/ApplicationSettingConfigurationDto.md)
 - [BindDeviceDto](docs/models/BindDeviceDto.md)
 - [BooleanKeyValue](docs/models/BooleanKeyValue.md)
 - [BooleanSetKeyValueDto](docs/models/BooleanSetKeyValueDto.md)
 - [ChangePasswordInput](docs/models/ChangePasswordInput.md)
 - [ClockDto](docs/models/ClockDto.md)
 - [ControllerApiDescriptionModel](docs/models/ControllerApiDescriptionModel.md)
 - [ControllerInterfaceApiDescriptionModel](docs/models/ControllerInterfaceApiDescriptionModel.md)
 - [CreateOrUpdateAppDto](docs/models/CreateOrUpdateAppDto.md)
 - [CreateOrUpdateAppFeatureDto](docs/models/CreateOrUpdateAppFeatureDto.md)
 - [CreateOrUpdateAppPricingDto](docs/models/CreateOrUpdateAppPricingDto.md)
 - [CreateOrUpdateAppPricingItemDto](docs/models/CreateOrUpdateAppPricingItemDto.md)
 - [CreateOrUpdateAppReleaseDto](docs/models/CreateOrUpdateAppReleaseDto.md)
 - [CreateOrUpdateAppSdkDto](docs/models/CreateOrUpdateAppSdkDto.md)
 - [CreateOrUpdateAppUserScoreDto](docs/models/CreateOrUpdateAppUserScoreDto.md)
 - [CreateOrUpdatePuupeeDto](docs/models/CreateOrUpdatePuupeeDto.md)
 - [CurrentCultureDto](docs/models/CurrentCultureDto.md)
 - [CurrentTenantDto](docs/models/CurrentTenantDto.md)
 - [CurrentUserDto](docs/models/CurrentUserDto.md)
 - [DateTimeFormatDto](docs/models/DateTimeFormatDto.md)
 - [DateTimeKeyValue](docs/models/DateTimeKeyValue.md)
 - [DateTimeSetKeyValueDto](docs/models/DateTimeSetKeyValueDto.md)
 - [DecimalKeyValue](docs/models/DecimalKeyValue.md)
 - [DecimalSetKeyValueDto](docs/models/DecimalSetKeyValueDto.md)
 - [DeviceDto](docs/models/DeviceDto.md)
 - [DeviceDtoPagedResultDto](docs/models/DeviceDtoPagedResultDto.md)
 - [DoubleKeyValue](docs/models/DoubleKeyValue.md)
 - [DoubleSetKeyValueDto](docs/models/DoubleSetKeyValueDto.md)
 - [EmailSettingsDto](docs/models/EmailSettingsDto.md)
 - [EntityExtensionDto](docs/models/EntityExtensionDto.md)
 - [ExtensionEnumDto](docs/models/ExtensionEnumDto.md)
 - [ExtensionEnumFieldDto](docs/models/ExtensionEnumFieldDto.md)
 - [ExtensionPropertyApiCreateDto](docs/models/ExtensionPropertyApiCreateDto.md)
 - [ExtensionPropertyApiDto](docs/models/ExtensionPropertyApiDto.md)
 - [ExtensionPropertyApiGetDto](docs/models/ExtensionPropertyApiGetDto.md)
 - [ExtensionPropertyApiUpdateDto](docs/models/ExtensionPropertyApiUpdateDto.md)
 - [ExtensionPropertyAttributeDto](docs/models/ExtensionPropertyAttributeDto.md)
 - [ExtensionPropertyDto](docs/models/ExtensionPropertyDto.md)
 - [ExtensionPropertyUiDto](docs/models/ExtensionPropertyUiDto.md)
 - [ExtensionPropertyUiFormDto](docs/models/ExtensionPropertyUiFormDto.md)
 - [ExtensionPropertyUiLookupDto](docs/models/ExtensionPropertyUiLookupDto.md)
 - [ExtensionPropertyUiTableDto](docs/models/ExtensionPropertyUiTableDto.md)
 - [FeatureDto](docs/models/FeatureDto.md)
 - [FeatureGroupDto](docs/models/FeatureGroupDto.md)
 - [FeatureProviderDto](docs/models/FeatureProviderDto.md)
 - [FindTenantResultDto](docs/models/FindTenantResultDto.md)
 - [GetFeatureListResultDto](docs/models/GetFeatureListResultDto.md)
 - [GetPermissionListResultDto](docs/models/GetPermissionListResultDto.md)
 - [IStringValueType](docs/models/IStringValueType.md)
 - [IValueValidator](docs/models/IValueValidator.md)
 - [IanaTimeZone](docs/models/IanaTimeZone.md)
 - [IdentityRoleCreateDto](docs/models/IdentityRoleCreateDto.md)
 - [IdentityRoleDto](docs/models/IdentityRoleDto.md)
 - [IdentityRoleDtoListResultDto](docs/models/IdentityRoleDtoListResultDto.md)
 - [IdentityRoleDtoPagedResultDto](docs/models/IdentityRoleDtoPagedResultDto.md)
 - [IdentityRoleUpdateDto](docs/models/IdentityRoleUpdateDto.md)
 - [IdentityUserCreateDto](docs/models/IdentityUserCreateDto.md)
 - [IdentityUserDto](docs/models/IdentityUserDto.md)
 - [IdentityUserDtoPagedResultDto](docs/models/IdentityUserDtoPagedResultDto.md)
 - [IdentityUserUpdateDto](docs/models/IdentityUserUpdateDto.md)
 - [IdentityUserUpdateRolesDto](docs/models/IdentityUserUpdateRolesDto.md)
 - [Int32KeyValue](docs/models/Int32KeyValue.md)
 - [Int32SetKeyValueDto](docs/models/Int32SetKeyValueDto.md)
 - [InterfaceMethodApiDescriptionModel](docs/models/InterfaceMethodApiDescriptionModel.md)
 - [LanguageInfo](docs/models/LanguageInfo.md)
 - [LocalizableStringDto](docs/models/LocalizableStringDto.md)
 - [LoginResultType](docs/models/LoginResultType.md)
 - [MethodParameterApiDescriptionModel](docs/models/MethodParameterApiDescriptionModel.md)
 - [ModuleApiDescriptionModel](docs/models/ModuleApiDescriptionModel.md)
 - [ModuleExtensionDto](docs/models/ModuleExtensionDto.md)
 - [MultiTenancyInfoDto](docs/models/MultiTenancyInfoDto.md)
 - [NameValue](docs/models/NameValue.md)
 - [ObjectExtensionsDto](docs/models/ObjectExtensionsDto.md)
 - [ParameterApiDescriptionModel](docs/models/ParameterApiDescriptionModel.md)
 - [PermissionGrantInfoDto](docs/models/PermissionGrantInfoDto.md)
 - [PermissionGroupDto](docs/models/PermissionGroupDto.md)
 - [ProfileDto](docs/models/ProfileDto.md)
 - [PropertyApiDescriptionModel](docs/models/PropertyApiDescriptionModel.md)
 - [ProviderInfoDto](docs/models/ProviderInfoDto.md)
 - [PuupeeChangedEto](docs/models/PuupeeChangedEto.md)
 - [PuupeeDto](docs/models/PuupeeDto.md)
 - [PuupeeDtoPagedResultDto](docs/models/PuupeeDtoPagedResultDto.md)
 - [RefreshDeviceStatusDto](docs/models/RefreshDeviceStatusDto.md)
 - [RegisterDto](docs/models/RegisterDto.md)
 - [RemoteServiceErrorInfo](docs/models/RemoteServiceErrorInfo.md)
 - [RemoteServiceErrorResponse](docs/models/RemoteServiceErrorResponse.md)
 - [RemoteServiceValidationErrorInfo](docs/models/RemoteServiceValidationErrorInfo.md)
 - [ResetPasswordDto](docs/models/ResetPasswordDto.md)
 - [ReturnValueApiDescriptionModel](docs/models/ReturnValueApiDescriptionModel.md)
 - [SendPasswordResetCodeDto](docs/models/SendPasswordResetCodeDto.md)
 - [SendTestEmailInput](docs/models/SendTestEmailInput.md)
 - [SendVerificationCodeDto](docs/models/SendVerificationCodeDto.md)
 - [SettingsDto](docs/models/SettingsDto.md)
 - [SimpleDataDto](docs/models/SimpleDataDto.md)
 - [SimpleDataDtoPagedResultDto](docs/models/SimpleDataDtoPagedResultDto.md)
 - [StorageObjectCredentials](docs/models/StorageObjectCredentials.md)
 - [StorageObjectDto](docs/models/StorageObjectDto.md)
 - [StorageObjectOrCredentialsDto](docs/models/StorageObjectOrCredentialsDto.md)
 - [StringKeyValue](docs/models/StringKeyValue.md)
 - [StringSetKeyValueDto](docs/models/StringSetKeyValueDto.md)
 - [SyncStateDto](docs/models/SyncStateDto.md)
 - [TenantCreateDto](docs/models/TenantCreateDto.md)
 - [TenantDto](docs/models/TenantDto.md)
 - [TenantDtoPagedResultDto](docs/models/TenantDtoPagedResultDto.md)
 - [TenantUpdateDto](docs/models/TenantUpdateDto.md)
 - [TestDateTime](docs/models/TestDateTime.md)
 - [TimeZone](docs/models/TimeZone.md)
 - [TimingDto](docs/models/TimingDto.md)
 - [TodoOrderBy](docs/models/TodoOrderBy.md)
 - [TodoSettingsDto](docs/models/TodoSettingsDto.md)
 - [TypeApiDescriptionModel](docs/models/TypeApiDescriptionModel.md)
 - [UpdateEmailSettingsDto](docs/models/UpdateEmailSettingsDto.md)
 - [UpdateFeatureDto](docs/models/UpdateFeatureDto.md)
 - [UpdateFeaturesDto](docs/models/UpdateFeaturesDto.md)
 - [UpdatePermissionDto](docs/models/UpdatePermissionDto.md)
 - [UpdatePermissionsDto](docs/models/UpdatePermissionsDto.md)
 - [UpdateProfileDto](docs/models/UpdateProfileDto.md)
 - [UserData](docs/models/UserData.md)
 - [UserDataListResultDto](docs/models/UserDataListResultDto.md)
 - [UserLoginInfo](docs/models/UserLoginInfo.md)
 - [UserStorageDto](docs/models/UserStorageDto.md)
 - [UserStorageItemDto](docs/models/UserStorageItemDto.md)
 - [VerifyPasswordResetTokenInput](docs/models/VerifyPasswordResetTokenInput.md)
 - [WindowsTimeZone](docs/models/WindowsTimeZone.md)

## Documentation For Authorization

 Authentication schemes defined for the API:
## oauth2

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: https://localhost:44355/connect/authorize
- **Scopes**: 
 - **Puupees**: Puupee API


## Author


































## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in puupee-api.apis and puupee-api.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from puupee-api.apis.default_api import DefaultApi`
- `from puupee-api.model.pet import Pet`

Solution 1:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import puupee-api
from puupee-api.apis import *
from puupee-api.models import *
```
