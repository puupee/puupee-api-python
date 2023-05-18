# puupee-api.MessageSourceRouteSubApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_app_message_source_route_sub_get**](MessageSourceRouteSubApi.md#api_app_message_source_route_sub_get) | **GET** /api/app/message-source-route-sub | 
[**api_app_message_source_route_sub_id_delete**](MessageSourceRouteSubApi.md#api_app_message_source_route_sub_id_delete) | **DELETE** /api/app/message-source-route-sub/{id} | 
[**api_app_message_source_route_sub_id_get**](MessageSourceRouteSubApi.md#api_app_message_source_route_sub_id_get) | **GET** /api/app/message-source-route-sub/{id} | 
[**api_app_message_source_route_sub_id_put**](MessageSourceRouteSubApi.md#api_app_message_source_route_sub_id_put) | **PUT** /api/app/message-source-route-sub/{id} | 
[**api_app_message_source_route_sub_post**](MessageSourceRouteSubApi.md#api_app_message_source_route_sub_post) | **POST** /api/app/message-source-route-sub | 


# **api_app_message_source_route_sub_get**
> list[MessageSourceRouteSubDto] api_app_message_source_route_sub_get()



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
    api_instance = puupee-api.MessageSourceRouteSubApi(api_client)
    
    try:
        api_response = api_instance.api_app_message_source_route_sub_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MessageSourceRouteSubApi->api_app_message_source_route_sub_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[MessageSourceRouteSubDto]**](MessageSourceRouteSubDto.md)

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

# **api_app_message_source_route_sub_id_delete**
> api_app_message_source_route_sub_id_delete(id)



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
    api_instance = puupee-api.MessageSourceRouteSubApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.api_app_message_source_route_sub_id_delete(id)
    except ApiException as e:
        print("Exception when calling MessageSourceRouteSubApi->api_app_message_source_route_sub_id_delete: %s\n" % e)
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

# **api_app_message_source_route_sub_id_get**
> MessageSourceRouteSubDto api_app_message_source_route_sub_id_get(id)



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
    api_instance = puupee-api.MessageSourceRouteSubApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.api_app_message_source_route_sub_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MessageSourceRouteSubApi->api_app_message_source_route_sub_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**MessageSourceRouteSubDto**](MessageSourceRouteSubDto.md)

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

# **api_app_message_source_route_sub_id_put**
> api_app_message_source_route_sub_id_put(id, create_update_message_source_route_sub_dto=create_update_message_source_route_sub_dto)



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
    api_instance = puupee-api.MessageSourceRouteSubApi(api_client)
    id = 'id_example' # str | 
create_update_message_source_route_sub_dto = puupee-api.CreateUpdateMessageSourceRouteSubDto() # CreateUpdateMessageSourceRouteSubDto |  (optional)

    try:
        api_instance.api_app_message_source_route_sub_id_put(id, create_update_message_source_route_sub_dto=create_update_message_source_route_sub_dto)
    except ApiException as e:
        print("Exception when calling MessageSourceRouteSubApi->api_app_message_source_route_sub_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **create_update_message_source_route_sub_dto** | [**CreateUpdateMessageSourceRouteSubDto**](CreateUpdateMessageSourceRouteSubDto.md)|  | [optional] 

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

# **api_app_message_source_route_sub_post**
> api_app_message_source_route_sub_post(create_update_message_source_route_sub_dto=create_update_message_source_route_sub_dto)



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
    api_instance = puupee-api.MessageSourceRouteSubApi(api_client)
    create_update_message_source_route_sub_dto = puupee-api.CreateUpdateMessageSourceRouteSubDto() # CreateUpdateMessageSourceRouteSubDto |  (optional)

    try:
        api_instance.api_app_message_source_route_sub_post(create_update_message_source_route_sub_dto=create_update_message_source_route_sub_dto)
    except ApiException as e:
        print("Exception when calling MessageSourceRouteSubApi->api_app_message_source_route_sub_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_update_message_source_route_sub_dto** | [**CreateUpdateMessageSourceRouteSubDto**](CreateUpdateMessageSourceRouteSubDto.md)|  | [optional] 

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

