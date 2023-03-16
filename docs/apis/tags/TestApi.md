<a name="__pageTop"></a>
# puupee-api.apis.tags.test_api.TestApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_test_datetime_get**](#api_test_datetime_get) | **get** /api/Test/datetime | 

# **api_test_datetime_get**
<a name="api_test_datetime_get"></a>
> TestDateTime api_test_datetime_get()



### Example

* OAuth Authentication (oauth2):
```python
import puupee-api
from puupee-api.apis.tags import test_api
from puupee-api.model.test_date_time import TestDateTime
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
    api_instance = test_api.TestApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.api_test_datetime_get()
        pprint(api_response)
    except puupee-api.ApiException as e:
        print("Exception when calling TestApi->api_test_datetime_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#api_test_datetime_get.ApiResponseFor200) | Success

#### api_test_datetime_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**TestDateTime**](../../models/TestDateTime.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TestDateTime**](../../models/TestDateTime.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TestDateTime**](../../models/TestDateTime.md) |  | 


### Authorization

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

