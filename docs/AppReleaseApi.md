# puupee-api.AppReleaseApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_app_app_release_get**](AppReleaseApi.md#api_app_app_release_get) | **GET** /api/app/app-release | 
[**api_app_app_release_id_delete**](AppReleaseApi.md#api_app_app_release_id_delete) | **DELETE** /api/app/app-release/{id} | 
[**api_app_app_release_id_get**](AppReleaseApi.md#api_app_app_release_id_get) | **GET** /api/app/app-release/{id} | 
[**api_app_app_release_id_put**](AppReleaseApi.md#api_app_app_release_id_put) | **PUT** /api/app/app-release/{id} | 
[**api_app_app_release_latest_get**](AppReleaseApi.md#api_app_app_release_latest_get) | **GET** /api/app/app-release/latest | 
[**api_app_app_release_post**](AppReleaseApi.md#api_app_app_release_post) | **POST** /api/app/app-release | 


# **api_app_app_release_get**
> AppReleaseDtoPagedResultDto api_app_app_release_get(app_id=app_id, environment=environment, platform_name=platform_name, platform_value=platform_value, sorting=sorting, skip_count=skip_count, max_result_count=max_result_count)



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
    api_instance = puupee-api.AppReleaseApi(api_client)
    app_id = 'app_id_example' # str |  (optional)
environment = 'environment_example' # str |  (optional)
platform_name = 'platform_name_example' # str |  (optional)
platform_value = 'platform_value_example' # str |  (optional)
sorting = 'sorting_example' # str |  (optional)
skip_count = 56 # int |  (optional)
max_result_count = 56 # int |  (optional)

    try:
        api_response = api_instance.api_app_app_release_get(app_id=app_id, environment=environment, platform_name=platform_name, platform_value=platform_value, sorting=sorting, skip_count=skip_count, max_result_count=max_result_count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AppReleaseApi->api_app_app_release_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | [optional] 
 **environment** | **str**|  | [optional] 
 **platform_name** | **str**|  | [optional] 
 **platform_value** | **str**|  | [optional] 
 **sorting** | **str**|  | [optional] 
 **skip_count** | **int**|  | [optional] 
 **max_result_count** | **int**|  | [optional] 

### Return type

[**AppReleaseDtoPagedResultDto**](AppReleaseDtoPagedResultDto.md)

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

# **api_app_app_release_id_delete**
> api_app_app_release_id_delete(id)



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
    api_instance = puupee-api.AppReleaseApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.api_app_app_release_id_delete(id)
    except ApiException as e:
        print("Exception when calling AppReleaseApi->api_app_app_release_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

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

# **api_app_app_release_id_get**
> AppReleaseDto api_app_app_release_id_get(id)



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
    api_instance = puupee-api.AppReleaseApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.api_app_app_release_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AppReleaseApi->api_app_app_release_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**AppReleaseDto**](AppReleaseDto.md)

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

# **api_app_app_release_id_put**
> AppReleaseDto api_app_app_release_id_put(id, create_or_update_app_release_dto=create_or_update_app_release_dto)



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
    api_instance = puupee-api.AppReleaseApi(api_client)
    id = 'id_example' # str | 
create_or_update_app_release_dto = puupee-api.CreateOrUpdateAppReleaseDto() # CreateOrUpdateAppReleaseDto |  (optional)

    try:
        api_response = api_instance.api_app_app_release_id_put(id, create_or_update_app_release_dto=create_or_update_app_release_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AppReleaseApi->api_app_app_release_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **create_or_update_app_release_dto** | [**CreateOrUpdateAppReleaseDto**](CreateOrUpdateAppReleaseDto.md)|  | [optional] 

### Return type

[**AppReleaseDto**](AppReleaseDto.md)

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

# **api_app_app_release_latest_get**
> AppReleaseDto api_app_app_release_latest_get(app_name=app_name, platform=platform, product_type=product_type, environment=environment)



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
    api_instance = puupee-api.AppReleaseApi(api_client)
    app_name = 'app_name_example' # str |  (optional)
platform = 'platform_example' # str |  (optional)
product_type = 'product_type_example' # str |  (optional)
environment = 'environment_example' # str |  (optional)

    try:
        api_response = api_instance.api_app_app_release_latest_get(app_name=app_name, platform=platform, product_type=product_type, environment=environment)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AppReleaseApi->api_app_app_release_latest_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**|  | [optional] 
 **platform** | **str**|  | [optional] 
 **product_type** | **str**|  | [optional] 
 **environment** | **str**|  | [optional] 

### Return type

[**AppReleaseDto**](AppReleaseDto.md)

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

# **api_app_app_release_post**
> AppReleaseDto api_app_app_release_post(create_or_update_app_release_dto=create_or_update_app_release_dto)



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
    api_instance = puupee-api.AppReleaseApi(api_client)
    create_or_update_app_release_dto = puupee-api.CreateOrUpdateAppReleaseDto() # CreateOrUpdateAppReleaseDto |  (optional)

    try:
        api_response = api_instance.api_app_app_release_post(create_or_update_app_release_dto=create_or_update_app_release_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AppReleaseApi->api_app_app_release_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_or_update_app_release_dto** | [**CreateOrUpdateAppReleaseDto**](CreateOrUpdateAppReleaseDto.md)|  | [optional] 

### Return type

[**AppReleaseDto**](AppReleaseDto.md)

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

