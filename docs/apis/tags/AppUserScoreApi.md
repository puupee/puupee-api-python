<a name="__pageTop"></a>
# openapi_client.apis.tags.app_user_score_api.AppUserScoreApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_app_app_user_score_post**](#api_app_app_user_score_post) | **post** /api/app/app-user-score | 

# **api_app_app_user_score_post**
<a name="api_app_app_user_score_post"></a>
> AppUserScoreDto api_app_app_user_score_post()



### Example

* OAuth Authentication (oauth2):
```python
import openapi_client
from openapi_client.apis.tags import app_user_score_api
from openapi_client.model.remote_service_error_response import RemoteServiceErrorResponse
from openapi_client.model.app_user_score_dto import AppUserScoreDto
from openapi_client.model.create_or_update_app_user_score_dto import CreateOrUpdateAppUserScoreDto
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
    api_instance = app_user_score_api.AppUserScoreApi(api_client)

    # example passing only optional values
    body = CreateOrUpdateAppUserScoreDto(
        app_id="app_id_example",
        score=1,
        comment="comment_example",
    )
    try:
        api_response = api_instance.api_app_app_user_score_post(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AppUserScoreApi->api_app_app_user_score_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateOrUpdateAppUserScoreDto**](../../models/CreateOrUpdateAppUserScoreDto.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateOrUpdateAppUserScoreDto**](../../models/CreateOrUpdateAppUserScoreDto.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateOrUpdateAppUserScoreDto**](../../models/CreateOrUpdateAppUserScoreDto.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#api_app_app_user_score_post.ApiResponseFor200) | Success
403 | [ApiResponseFor403](#api_app_app_user_score_post.ApiResponseFor403) | Forbidden
401 | [ApiResponseFor401](#api_app_app_user_score_post.ApiResponseFor401) | Unauthorized
400 | [ApiResponseFor400](#api_app_app_user_score_post.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#api_app_app_user_score_post.ApiResponseFor404) | Not Found
501 | [ApiResponseFor501](#api_app_app_user_score_post.ApiResponseFor501) | Server Error
500 | [ApiResponseFor500](#api_app_app_user_score_post.ApiResponseFor500) | Server Error

#### api_app_app_user_score_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**AppUserScoreDto**](../../models/AppUserScoreDto.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AppUserScoreDto**](../../models/AppUserScoreDto.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AppUserScoreDto**](../../models/AppUserScoreDto.md) |  | 


#### api_app_app_user_score_post.ApiResponseFor403
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


#### api_app_app_user_score_post.ApiResponseFor401
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


#### api_app_app_user_score_post.ApiResponseFor400
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


#### api_app_app_user_score_post.ApiResponseFor404
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


#### api_app_app_user_score_post.ApiResponseFor501
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


#### api_app_app_user_score_post.ApiResponseFor500
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

