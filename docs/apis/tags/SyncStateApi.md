<a name="__pageTop"></a>
# openapi_client.apis.tags.sync_state_api.SyncStateApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_app_sync_state_get**](#api_app_sync_state_get) | **get** /api/app/sync-state | 
[**api_app_sync_state_puupee_changed_eto_post**](#api_app_sync_state_puupee_changed_eto_post) | **post** /api/app/sync-state/puupee-changed-eto | 

# **api_app_sync_state_get**
<a name="api_app_sync_state_get"></a>
> SyncStateDto api_app_sync_state_get()



### Example

* OAuth Authentication (oauth2):
```python
import openapi_client
from openapi_client.apis.tags import sync_state_api
from openapi_client.model.sync_state_dto import SyncStateDto
from openapi_client.model.remote_service_error_response import RemoteServiceErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = openapi_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sync_state_api.SyncStateApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.api_app_sync_state_get()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SyncStateApi->api_app_sync_state_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#api_app_sync_state_get.ApiResponseFor200) | Success
403 | [ApiResponseFor403](#api_app_sync_state_get.ApiResponseFor403) | Forbidden
401 | [ApiResponseFor401](#api_app_sync_state_get.ApiResponseFor401) | Unauthorized
400 | [ApiResponseFor400](#api_app_sync_state_get.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#api_app_sync_state_get.ApiResponseFor404) | Not Found
501 | [ApiResponseFor501](#api_app_sync_state_get.ApiResponseFor501) | Server Error
500 | [ApiResponseFor500](#api_app_sync_state_get.ApiResponseFor500) | Server Error

#### api_app_sync_state_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**SyncStateDto**](../../models/SyncStateDto.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SyncStateDto**](../../models/SyncStateDto.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SyncStateDto**](../../models/SyncStateDto.md) |  | 


#### api_app_sync_state_get.ApiResponseFor403
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


#### api_app_sync_state_get.ApiResponseFor401
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


#### api_app_sync_state_get.ApiResponseFor400
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


#### api_app_sync_state_get.ApiResponseFor404
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


#### api_app_sync_state_get.ApiResponseFor501
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


#### api_app_sync_state_get.ApiResponseFor500
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

# **api_app_sync_state_puupee_changed_eto_post**
<a name="api_app_sync_state_puupee_changed_eto_post"></a>
> PuupeeChangedEto api_app_sync_state_puupee_changed_eto_post()



### Example

* OAuth Authentication (oauth2):
```python
import openapi_client
from openapi_client.apis.tags import sync_state_api
from openapi_client.model.remote_service_error_response import RemoteServiceErrorResponse
from openapi_client.model.puupee_changed_eto import PuupeeChangedEto
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = openapi_client.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sync_state_api.SyncStateApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.api_app_sync_state_puupee_changed_eto_post()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SyncStateApi->api_app_sync_state_puupee_changed_eto_post: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#api_app_sync_state_puupee_changed_eto_post.ApiResponseFor200) | Success
403 | [ApiResponseFor403](#api_app_sync_state_puupee_changed_eto_post.ApiResponseFor403) | Forbidden
401 | [ApiResponseFor401](#api_app_sync_state_puupee_changed_eto_post.ApiResponseFor401) | Unauthorized
400 | [ApiResponseFor400](#api_app_sync_state_puupee_changed_eto_post.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#api_app_sync_state_puupee_changed_eto_post.ApiResponseFor404) | Not Found
501 | [ApiResponseFor501](#api_app_sync_state_puupee_changed_eto_post.ApiResponseFor501) | Server Error
500 | [ApiResponseFor500](#api_app_sync_state_puupee_changed_eto_post.ApiResponseFor500) | Server Error

#### api_app_sync_state_puupee_changed_eto_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**PuupeeChangedEto**](../../models/PuupeeChangedEto.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PuupeeChangedEto**](../../models/PuupeeChangedEto.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PuupeeChangedEto**](../../models/PuupeeChangedEto.md) |  | 


#### api_app_sync_state_puupee_changed_eto_post.ApiResponseFor403
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


#### api_app_sync_state_puupee_changed_eto_post.ApiResponseFor401
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


#### api_app_sync_state_puupee_changed_eto_post.ApiResponseFor400
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


#### api_app_sync_state_puupee_changed_eto_post.ApiResponseFor404
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


#### api_app_sync_state_puupee_changed_eto_post.ApiResponseFor501
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


#### api_app_sync_state_puupee_changed_eto_post.ApiResponseFor500
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

