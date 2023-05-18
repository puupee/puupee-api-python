# puupee-api.AbpApiDefinitionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_abp_api_definition_get**](AbpApiDefinitionApi.md#api_abp_api_definition_get) | **GET** /api/abp/api-definition | 


# **api_abp_api_definition_get**
> ApplicationApiDescriptionModel api_abp_api_definition_get(include_types=include_types)



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
    api_instance = puupee-api.AbpApiDefinitionApi(api_client)
    include_types = True # bool |  (optional)

    try:
        api_response = api_instance.api_abp_api_definition_get(include_types=include_types)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AbpApiDefinitionApi->api_abp_api_definition_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_types** | **bool**|  | [optional] 

### Return type

[**ApplicationApiDescriptionModel**](ApplicationApiDescriptionModel.md)

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

