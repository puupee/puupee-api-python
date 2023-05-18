# puupee-api.AbpTenantApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_abp_multi_tenancy_tenants_by_id_id_get**](AbpTenantApi.md#api_abp_multi_tenancy_tenants_by_id_id_get) | **GET** /api/abp/multi-tenancy/tenants/by-id/{id} | 
[**api_abp_multi_tenancy_tenants_by_name_name_get**](AbpTenantApi.md#api_abp_multi_tenancy_tenants_by_name_name_get) | **GET** /api/abp/multi-tenancy/tenants/by-name/{name} | 


# **api_abp_multi_tenancy_tenants_by_id_id_get**
> FindTenantResultDto api_abp_multi_tenancy_tenants_by_id_id_get(id)



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
    api_instance = puupee-api.AbpTenantApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.api_abp_multi_tenancy_tenants_by_id_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AbpTenantApi->api_abp_multi_tenancy_tenants_by_id_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**FindTenantResultDto**](FindTenantResultDto.md)

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

# **api_abp_multi_tenancy_tenants_by_name_name_get**
> FindTenantResultDto api_abp_multi_tenancy_tenants_by_name_name_get(name)



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
    api_instance = puupee-api.AbpTenantApi(api_client)
    name = 'name_example' # str | 

    try:
        api_response = api_instance.api_abp_multi_tenancy_tenants_by_name_name_get(name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AbpTenantApi->api_abp_multi_tenancy_tenants_by_name_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**FindTenantResultDto**](FindTenantResultDto.md)

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

