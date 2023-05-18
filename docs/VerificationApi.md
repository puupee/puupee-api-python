# puupee-api.VerificationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_app_verification_send_code_post**](VerificationApi.md#api_app_verification_send_code_post) | **POST** /api/app/verification/send-code | 


# **api_app_verification_send_code_post**
> api_app_verification_send_code_post(send_verification_code_dto=send_verification_code_dto)



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
    api_instance = puupee-api.VerificationApi(api_client)
    send_verification_code_dto = puupee-api.SendVerificationCodeDto() # SendVerificationCodeDto |  (optional)

    try:
        api_instance.api_app_verification_send_code_post(send_verification_code_dto=send_verification_code_dto)
    except ApiException as e:
        print("Exception when calling VerificationApi->api_app_verification_send_code_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_verification_code_dto** | [**SendVerificationCodeDto**](SendVerificationCodeDto.md)|  | [optional] 

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

