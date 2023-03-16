<a name="__pageTop"></a>
# puupee-api.apis.tags.user_storage_api.UserStorageApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_app_user_storage_get**](#api_app_user_storage_get) | **get** /api/app/user-storage | 

# **api_app_user_storage_get**
<a name="api_app_user_storage_get"></a>
> UserStorageDto api_app_user_storage_get()



### Example

* OAuth Authentication (oauth2):
```python
import puupee-api
from puupee-api.apis.tags import user_storage_api
from puupee-api.model.user_storage_dto import UserStorageDto
from puupee-api.model.remote_service_error_response import RemoteServiceErrorResponse
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
    api_instance = user_storage_api.UserStorageApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.api_app_user_storage_get()
        pprint(api_response)
    except puupee-api.ApiException as e:
        print("Exception when calling UserStorageApi->api_app_user_storage_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#api_app_user_storage_get.ApiResponseFor200) | Success
403 | [ApiResponseFor403](#api_app_user_storage_get.ApiResponseFor403) | Forbidden
401 | [ApiResponseFor401](#api_app_user_storage_get.ApiResponseFor401) | Unauthorized
400 | [ApiResponseFor400](#api_app_user_storage_get.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#api_app_user_storage_get.ApiResponseFor404) | Not Found
501 | [ApiResponseFor501](#api_app_user_storage_get.ApiResponseFor501) | Server Error
500 | [ApiResponseFor500](#api_app_user_storage_get.ApiResponseFor500) | Server Error

#### api_app_user_storage_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**UserStorageDto**](../../models/UserStorageDto.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UserStorageDto**](../../models/UserStorageDto.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UserStorageDto**](../../models/UserStorageDto.md) |  | 


#### api_app_user_storage_get.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyTextPlain, SchemaFor403ResponseBodyApplicationJson, SchemaFor403ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**RemoteServiceErrorResponse**](../../models/RemoteServiceErrorResponse.md) |  | 


# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RemoteServiceErrorResponse**](../../models/RemoteServiceErrorResponse.md) |  | 


# SchemaFor403ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RemoteServiceErrorResponse**](../../models/RemoteServiceErrorResponse.md) |  | 


#### api_app_user_storage_get.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyTextPlain, SchemaFor401ResponseBodyApplicationJson, SchemaFor401ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**RemoteServiceErrorResponse**](../../models/RemoteServiceErrorResponse.md) |  | 


# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RemoteServiceErrorResponse**](../../models/RemoteServiceErrorResponse.md) |  | 


# SchemaFor401ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RemoteServiceErrorResponse**](../../models/RemoteServiceErrorResponse.md) |  | 


#### api_app_user_storage_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyTextPlain, SchemaFor400ResponseBodyApplicationJson, SchemaFor400ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**RemoteServiceErrorResponse**](../../models/RemoteServiceErrorResponse.md) |  | 


# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RemoteServiceErrorResponse**](../../models/RemoteServiceErrorResponse.md) |  | 


# SchemaFor400ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RemoteServiceErrorResponse**](../../models/RemoteServiceErrorResponse.md) |  | 


#### api_app_user_storage_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyTextPlain, SchemaFor404ResponseBodyApplicationJson, SchemaFor404ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**RemoteServiceErrorResponse**](../../models/RemoteServiceErrorResponse.md) |  | 


# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RemoteServiceErrorResponse**](../../models/RemoteServiceErrorResponse.md) |  | 


# SchemaFor404ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RemoteServiceErrorResponse**](../../models/RemoteServiceErrorResponse.md) |  | 


#### api_app_user_storage_get.ApiResponseFor501
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor501ResponseBodyTextPlain, SchemaFor501ResponseBodyApplicationJson, SchemaFor501ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor501ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**RemoteServiceErrorResponse**](../../models/RemoteServiceErrorResponse.md) |  | 


# SchemaFor501ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RemoteServiceErrorResponse**](../../models/RemoteServiceErrorResponse.md) |  | 


# SchemaFor501ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RemoteServiceErrorResponse**](../../models/RemoteServiceErrorResponse.md) |  | 


#### api_app_user_storage_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyTextPlain, SchemaFor500ResponseBodyApplicationJson, SchemaFor500ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**RemoteServiceErrorResponse**](../../models/RemoteServiceErrorResponse.md) |  | 


# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RemoteServiceErrorResponse**](../../models/RemoteServiceErrorResponse.md) |  | 


# SchemaFor500ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RemoteServiceErrorResponse**](../../models/RemoteServiceErrorResponse.md) |  | 


### Authorization

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

