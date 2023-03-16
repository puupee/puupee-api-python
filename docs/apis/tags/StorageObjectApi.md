<a name="__pageTop"></a>
# puupee-api.apis.tags.storage_object_api.StorageObjectApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_app_storage_object_file_get**](#api_app_storage_object_file_get) | **get** /api/app/storage-object/file | 
[**api_app_storage_object_file_or_credentials_get**](#api_app_storage_object_file_or_credentials_get) | **get** /api/app/storage-object/file-or-credentials | 
[**api_app_storage_object_pre_sign_url_post**](#api_app_storage_object_pre_sign_url_post) | **post** /api/app/storage-object/pre-sign-url | 
[**api_app_storage_object_thumb_get**](#api_app_storage_object_thumb_get) | **get** /api/app/storage-object/thumb | 

# **api_app_storage_object_file_get**
<a name="api_app_storage_object_file_get"></a>
> api_app_storage_object_file_get()



### Example

* OAuth Authentication (oauth2):
```python
import puupee-api
from puupee-api.apis.tags import storage_object_api
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
    api_instance = storage_object_api.StorageObjectApi(api_client)

    # example passing only optional values
    query_params = {
        'key': "key_example",
    }
    try:
        api_response = api_instance.api_app_storage_object_file_get(
            query_params=query_params,
        )
    except puupee-api.ApiException as e:
        print("Exception when calling StorageObjectApi->api_app_storage_object_file_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
key | KeySchema | | optional


# KeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#api_app_storage_object_file_get.ApiResponseFor200) | Success

#### api_app_storage_object_file_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **api_app_storage_object_file_or_credentials_get**
<a name="api_app_storage_object_file_or_credentials_get"></a>
> StorageObjectOrCredentialsDto api_app_storage_object_file_or_credentials_get()



### Example

* OAuth Authentication (oauth2):
```python
import puupee-api
from puupee-api.apis.tags import storage_object_api
from puupee-api.model.storage_object_or_credentials_dto import StorageObjectOrCredentialsDto
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
    api_instance = storage_object_api.StorageObjectApi(api_client)

    # example passing only optional values
    query_params = {
        'rapidCode': "rapidCode_example",
        'key': "key_example",
    }
    try:
        api_response = api_instance.api_app_storage_object_file_or_credentials_get(
            query_params=query_params,
        )
        pprint(api_response)
    except puupee-api.ApiException as e:
        print("Exception when calling StorageObjectApi->api_app_storage_object_file_or_credentials_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
rapidCode | RapidCodeSchema | | optional
key | KeySchema | | optional


# RapidCodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# KeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#api_app_storage_object_file_or_credentials_get.ApiResponseFor200) | Success
403 | [ApiResponseFor403](#api_app_storage_object_file_or_credentials_get.ApiResponseFor403) | Forbidden
401 | [ApiResponseFor401](#api_app_storage_object_file_or_credentials_get.ApiResponseFor401) | Unauthorized
400 | [ApiResponseFor400](#api_app_storage_object_file_or_credentials_get.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#api_app_storage_object_file_or_credentials_get.ApiResponseFor404) | Not Found
501 | [ApiResponseFor501](#api_app_storage_object_file_or_credentials_get.ApiResponseFor501) | Server Error
500 | [ApiResponseFor500](#api_app_storage_object_file_or_credentials_get.ApiResponseFor500) | Server Error

#### api_app_storage_object_file_or_credentials_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**StorageObjectOrCredentialsDto**](../../models/StorageObjectOrCredentialsDto.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**StorageObjectOrCredentialsDto**](../../models/StorageObjectOrCredentialsDto.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**StorageObjectOrCredentialsDto**](../../models/StorageObjectOrCredentialsDto.md) |  | 


#### api_app_storage_object_file_or_credentials_get.ApiResponseFor403
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


#### api_app_storage_object_file_or_credentials_get.ApiResponseFor401
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


#### api_app_storage_object_file_or_credentials_get.ApiResponseFor400
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


#### api_app_storage_object_file_or_credentials_get.ApiResponseFor404
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


#### api_app_storage_object_file_or_credentials_get.ApiResponseFor501
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


#### api_app_storage_object_file_or_credentials_get.ApiResponseFor500
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

# **api_app_storage_object_pre_sign_url_post**
<a name="api_app_storage_object_pre_sign_url_post"></a>
> str api_app_storage_object_pre_sign_url_post()



### Example

* OAuth Authentication (oauth2):
```python
import puupee-api
from puupee-api.apis.tags import storage_object_api
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
    api_instance = storage_object_api.StorageObjectApi(api_client)

    # example passing only optional values
    query_params = {
        'key': "key_example",
    }
    try:
        api_response = api_instance.api_app_storage_object_pre_sign_url_post(
            query_params=query_params,
        )
        pprint(api_response)
    except puupee-api.ApiException as e:
        print("Exception when calling StorageObjectApi->api_app_storage_object_pre_sign_url_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('text/plain', 'application/json', 'text/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
key | KeySchema | | optional


# KeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#api_app_storage_object_pre_sign_url_post.ApiResponseFor200) | Success
403 | [ApiResponseFor403](#api_app_storage_object_pre_sign_url_post.ApiResponseFor403) | Forbidden
401 | [ApiResponseFor401](#api_app_storage_object_pre_sign_url_post.ApiResponseFor401) | Unauthorized
400 | [ApiResponseFor400](#api_app_storage_object_pre_sign_url_post.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#api_app_storage_object_pre_sign_url_post.ApiResponseFor404) | Not Found
501 | [ApiResponseFor501](#api_app_storage_object_pre_sign_url_post.ApiResponseFor501) | Server Error
500 | [ApiResponseFor500](#api_app_storage_object_pre_sign_url_post.ApiResponseFor500) | Server Error

#### api_app_storage_object_pre_sign_url_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SchemaFor200ResponseBodyTextJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

#### api_app_storage_object_pre_sign_url_post.ApiResponseFor403
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


#### api_app_storage_object_pre_sign_url_post.ApiResponseFor401
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


#### api_app_storage_object_pre_sign_url_post.ApiResponseFor400
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


#### api_app_storage_object_pre_sign_url_post.ApiResponseFor404
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


#### api_app_storage_object_pre_sign_url_post.ApiResponseFor501
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


#### api_app_storage_object_pre_sign_url_post.ApiResponseFor500
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

# **api_app_storage_object_thumb_get**
<a name="api_app_storage_object_thumb_get"></a>
> api_app_storage_object_thumb_get()



### Example

* OAuth Authentication (oauth2):
```python
import puupee-api
from puupee-api.apis.tags import storage_object_api
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
    api_instance = storage_object_api.StorageObjectApi(api_client)

    # example passing only optional values
    query_params = {
        'key': "key_example",
    }
    try:
        api_response = api_instance.api_app_storage_object_thumb_get(
            query_params=query_params,
        )
    except puupee-api.ApiException as e:
        print("Exception when calling StorageObjectApi->api_app_storage_object_thumb_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
key | KeySchema | | optional


# KeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#api_app_storage_object_thumb_get.ApiResponseFor200) | Success

#### api_app_storage_object_thumb_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[oauth2](../../../README.md#oauth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

