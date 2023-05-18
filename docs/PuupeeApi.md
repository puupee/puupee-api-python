# puupee-api.PuupeeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_app_puupee_pull_get**](PuupeeApi.md#api_app_puupee_pull_get) | **GET** /api/app/puupee/pull | 
[**api_app_puupee_push_post**](PuupeeApi.md#api_app_puupee_push_post) | **POST** /api/app/puupee/push | 


# **api_app_puupee_pull_get**
> PuupeeDtoPagedResultDto api_app_puupee_pull_get(app_name=app_name, after_version=after_version, skip_count=skip_count, max_result_count=max_result_count)



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
    api_instance = puupee-api.PuupeeApi(api_client)
    app_name = 'app_name_example' # str |  (optional)
after_version = 56 # int |  (optional)
skip_count = 56 # int |  (optional)
max_result_count = 56 # int |  (optional)

    try:
        api_response = api_instance.api_app_puupee_pull_get(app_name=app_name, after_version=after_version, skip_count=skip_count, max_result_count=max_result_count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PuupeeApi->api_app_puupee_pull_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**|  | [optional] 
 **after_version** | **int**|  | [optional] 
 **skip_count** | **int**|  | [optional] 
 **max_result_count** | **int**|  | [optional] 

### Return type

[**PuupeeDtoPagedResultDto**](PuupeeDtoPagedResultDto.md)

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

# **api_app_puupee_push_post**
> PuupeeDto api_app_puupee_push_post(create_or_update_puupee_dto=create_or_update_puupee_dto)



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
    api_instance = puupee-api.PuupeeApi(api_client)
    create_or_update_puupee_dto = puupee-api.CreateOrUpdatePuupeeDto() # CreateOrUpdatePuupeeDto |  (optional)

    try:
        api_response = api_instance.api_app_puupee_push_post(create_or_update_puupee_dto=create_or_update_puupee_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PuupeeApi->api_app_puupee_push_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_or_update_puupee_dto** | [**CreateOrUpdatePuupeeDto**](CreateOrUpdatePuupeeDto.md)|  | [optional] 

### Return type

[**PuupeeDto**](PuupeeDto.md)

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

