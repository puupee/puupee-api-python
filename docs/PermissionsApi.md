# puupee-api.PermissionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_permission_management_permissions_get**](PermissionsApi.md#api_permission_management_permissions_get) | **GET** /api/permission-management/permissions | 
[**api_permission_management_permissions_put**](PermissionsApi.md#api_permission_management_permissions_put) | **PUT** /api/permission-management/permissions | 


# **api_permission_management_permissions_get**
> GetPermissionListResultDto api_permission_management_permissions_get(provider_name=provider_name, provider_key=provider_key)



### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import puupee-api
from puupee-api.rest import ApiException
from pprint import pprint
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
    api_instance = puupee-api.PermissionsApi(api_client)
    provider_name = 'provider_name_example' # str |  (optional)
provider_key = 'provider_key_example' # str |  (optional)

    try:
        api_response = api_instance.api_permission_management_permissions_get(provider_name=provider_name, provider_key=provider_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PermissionsApi->api_permission_management_permissions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_name** | **str**|  | [optional] 
 **provider_key** | **str**|  | [optional] 

### Return type

[**GetPermissionListResultDto**](GetPermissionListResultDto.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**501** | Server Error |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_permission_management_permissions_put**
> api_permission_management_permissions_put(provider_name=provider_name, provider_key=provider_key, update_permissions_dto=update_permissions_dto)



### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import puupee-api
from puupee-api.rest import ApiException
from pprint import pprint
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
    api_instance = puupee-api.PermissionsApi(api_client)
    provider_name = 'provider_name_example' # str |  (optional)
provider_key = 'provider_key_example' # str |  (optional)
update_permissions_dto = puupee-api.UpdatePermissionsDto() # UpdatePermissionsDto |  (optional)

    try:
        api_instance.api_permission_management_permissions_put(provider_name=provider_name, provider_key=provider_key, update_permissions_dto=update_permissions_dto)
    except ApiException as e:
        print("Exception when calling PermissionsApi->api_permission_management_permissions_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_name** | **str**|  | [optional] 
 **provider_key** | **str**|  | [optional] 
 **update_permissions_dto** | [**UpdatePermissionsDto**](UpdatePermissionsDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**501** | Server Error |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

