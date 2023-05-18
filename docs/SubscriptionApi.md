# puupee-api.SubscriptionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_app_subscription_apple_notifications_post**](SubscriptionApi.md#api_app_subscription_apple_notifications_post) | **POST** /api/app/subscription/apple-notifications | 
[**api_app_subscription_get**](SubscriptionApi.md#api_app_subscription_get) | **GET** /api/app/subscription | 
[**api_app_subscription_order_post**](SubscriptionApi.md#api_app_subscription_order_post) | **POST** /api/app/subscription/order | 
[**api_app_subscription_verify_receipt_post**](SubscriptionApi.md#api_app_subscription_verify_receipt_post) | **POST** /api/app/subscription/verify-receipt | 


# **api_app_subscription_apple_notifications_post**
> api_app_subscription_apple_notifications_post(apple_notificaion_dto=apple_notificaion_dto)



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
    api_instance = puupee-api.SubscriptionApi(api_client)
    apple_notificaion_dto = puupee-api.AppleNotificaionDto() # AppleNotificaionDto |  (optional)

    try:
        api_instance.api_app_subscription_apple_notifications_post(apple_notificaion_dto=apple_notificaion_dto)
    except ApiException as e:
        print("Exception when calling SubscriptionApi->api_app_subscription_apple_notifications_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apple_notificaion_dto** | [**AppleNotificaionDto**](AppleNotificaionDto.md)|  | [optional] 

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

# **api_app_subscription_get**
> SubscriptionDto api_app_subscription_get(app_id=app_id)



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
    api_instance = puupee-api.SubscriptionApi(api_client)
    app_id = 'app_id_example' # str |  (optional)

    try:
        api_response = api_instance.api_app_subscription_get(app_id=app_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SubscriptionApi->api_app_subscription_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | [optional] 

### Return type

[**SubscriptionDto**](SubscriptionDto.md)

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

# **api_app_subscription_order_post**
> SubscriptionOrderDto api_app_subscription_order_post(create_or_get_subscription_order_dto=create_or_get_subscription_order_dto)



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
    api_instance = puupee-api.SubscriptionApi(api_client)
    create_or_get_subscription_order_dto = puupee-api.CreateOrGetSubscriptionOrderDto() # CreateOrGetSubscriptionOrderDto |  (optional)

    try:
        api_response = api_instance.api_app_subscription_order_post(create_or_get_subscription_order_dto=create_or_get_subscription_order_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SubscriptionApi->api_app_subscription_order_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_or_get_subscription_order_dto** | [**CreateOrGetSubscriptionOrderDto**](CreateOrGetSubscriptionOrderDto.md)|  | [optional] 

### Return type

[**SubscriptionOrderDto**](SubscriptionOrderDto.md)

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

# **api_app_subscription_verify_receipt_post**
> VerifyReceiptResult api_app_subscription_verify_receipt_post(verify_receipt_dto=verify_receipt_dto)



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
    api_instance = puupee-api.SubscriptionApi(api_client)
    verify_receipt_dto = puupee-api.VerifyReceiptDto() # VerifyReceiptDto |  (optional)

    try:
        api_response = api_instance.api_app_subscription_verify_receipt_post(verify_receipt_dto=verify_receipt_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SubscriptionApi->api_app_subscription_verify_receipt_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verify_receipt_dto** | [**VerifyReceiptDto**](VerifyReceiptDto.md)|  | [optional] 

### Return type

[**VerifyReceiptResult**](VerifyReceiptResult.md)

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

