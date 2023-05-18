# puupee-api.NotificationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_app_notification_bark_api_key_message_get**](NotificationApi.md#api_app_notification_bark_api_key_message_get) | **GET** /api/app/notification/bark/{apiKey}/{message} | 
[**api_app_notification_get**](NotificationApi.md#api_app_notification_get) | **GET** /api/app/notification | 
[**api_app_notification_push_post**](NotificationApi.md#api_app_notification_push_post) | **POST** /api/app/notification/push | 


# **api_app_notification_bark_api_key_message_get**
> api_app_notification_bark_api_key_message_get(api_key, message, automatically_copy=automatically_copy, copy=copy, url=url, is_archive=is_archive, group=group, icon=icon, name=name, value=value)



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
    api_instance = puupee-api.NotificationApi(api_client)
    api_key = 'api_key_example' # str | 
message = 'message_example' # str | 
automatically_copy = 0 # int |  (optional) (default to 0)
copy = 'copy_example' # str |  (optional)
url = 'url_example' # str |  (optional)
is_archive = 'is_archive_example' # str |  (optional)
group = 'group_example' # str |  (optional)
icon = 'icon_example' # str |  (optional)
name = 'name_example' # str |  (optional)
value = 'value_example' # str |  (optional)

    try:
        api_instance.api_app_notification_bark_api_key_message_get(api_key, message, automatically_copy=automatically_copy, copy=copy, url=url, is_archive=is_archive, group=group, icon=icon, name=name, value=value)
    except ApiException as e:
        print("Exception when calling NotificationApi->api_app_notification_bark_api_key_message_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**|  | 
 **message** | **str**|  | 
 **automatically_copy** | **int**|  | [optional] [default to 0]
 **copy** | **str**|  | [optional] 
 **url** | **str**|  | [optional] 
 **is_archive** | **str**|  | [optional] 
 **group** | **str**|  | [optional] 
 **icon** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **value** | **str**|  | [optional] 

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

# **api_app_notification_get**
> NotificationInfoDtoPagedResultDto api_app_notification_get(sorting=sorting, skip_count=skip_count, max_result_count=max_result_count)



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
    api_instance = puupee-api.NotificationApi(api_client)
    sorting = 'sorting_example' # str |  (optional)
skip_count = 56 # int |  (optional)
max_result_count = 56 # int |  (optional)

    try:
        api_response = api_instance.api_app_notification_get(sorting=sorting, skip_count=skip_count, max_result_count=max_result_count)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NotificationApi->api_app_notification_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sorting** | **str**|  | [optional] 
 **skip_count** | **int**|  | [optional] 
 **max_result_count** | **int**|  | [optional] 

### Return type

[**NotificationInfoDtoPagedResultDto**](NotificationInfoDtoPagedResultDto.md)

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

# **api_app_notification_push_post**
> api_app_notification_push_post(create_push_notification_dto=create_push_notification_dto)



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
    api_instance = puupee-api.NotificationApi(api_client)
    create_push_notification_dto = puupee-api.CreatePushNotificationDto() # CreatePushNotificationDto |  (optional)

    try:
        api_instance.api_app_notification_push_post(create_push_notification_dto=create_push_notification_dto)
    except ApiException as e:
        print("Exception when calling NotificationApi->api_app_notification_push_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_push_notification_dto** | [**CreatePushNotificationDto**](CreatePushNotificationDto.md)|  | [optional] 

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

