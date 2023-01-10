<a name="__pageTop"></a>
# openapi_client.apis.tags.email_settings_api.EmailSettingsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_setting_management_emailing_get**](#api_setting_management_emailing_get) | **get** /api/setting-management/emailing | 
[**api_setting_management_emailing_post**](#api_setting_management_emailing_post) | **post** /api/setting-management/emailing | 
[**api_setting_management_emailing_send_test_email_post**](#api_setting_management_emailing_send_test_email_post) | **post** /api/setting-management/emailing/send-test-email | 

# **api_setting_management_emailing_get**
<a name="api_setting_management_emailing_get"></a>
> EmailSettingsDto api_setting_management_emailing_get()



### Example

* OAuth Authentication (oauth2):
```python
import openapi_client
from openapi_client.apis.tags import email_settings_api
from openapi_client.model.remote_service_error_response import RemoteServiceErrorResponse
from openapi_client.model.email_settings_dto import EmailSettingsDto
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
    api_instance = email_settings_api.EmailSettingsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.api_setting_management_emailing_get()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EmailSettingsApi->api_setting_management_emailing_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#api_setting_management_emailing_get.ApiResponseFor200) | Success
403 | [ApiResponseFor403](#api_setting_management_emailing_get.ApiResponseFor403) | Forbidden
401 | [ApiResponseFor401](#api_setting_management_emailing_get.ApiResponseFor401) | Unauthorized
400 | [ApiResponseFor400](#api_setting_management_emailing_get.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#api_setting_management_emailing_get.ApiResponseFor404) | Not Found
501 | [ApiResponseFor501](#api_setting_management_emailing_get.ApiResponseFor501) | Server Error
500 | [ApiResponseFor500](#api_setting_management_emailing_get.ApiResponseFor500) | Server Error

#### api_setting_management_emailing_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextPlain, SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextPlain
Type | Description  | Notes
------------- | ------------- | -------------
[**EmailSettingsDto**](../../models/EmailSettingsDto.md) |  | 


# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EmailSettingsDto**](../../models/EmailSettingsDto.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EmailSettingsDto**](../../models/EmailSettingsDto.md) |  | 


#### api_setting_management_emailing_get.ApiResponseFor403
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


#### api_setting_management_emailing_get.ApiResponseFor401
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


#### api_setting_management_emailing_get.ApiResponseFor400
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


#### api_setting_management_emailing_get.ApiResponseFor404
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


#### api_setting_management_emailing_get.ApiResponseFor501
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


#### api_setting_management_emailing_get.ApiResponseFor500
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

# **api_setting_management_emailing_post**
<a name="api_setting_management_emailing_post"></a>
> api_setting_management_emailing_post()



### Example

* OAuth Authentication (oauth2):
```python
import openapi_client
from openapi_client.apis.tags import email_settings_api
from openapi_client.model.remote_service_error_response import RemoteServiceErrorResponse
from openapi_client.model.update_email_settings_dto import UpdateEmailSettingsDto
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
    api_instance = email_settings_api.EmailSettingsApi(api_client)

    # example passing only optional values
    body = UpdateEmailSettingsDto(
        smtp_host="smtp_host_example",
        smtp_port=1,
        smtp_user_name="smtp_user_name_example",
        smtp_password="smtp_password_example",
        smtp_domain="smtp_domain_example",
        smtp_enable_ssl=True,
        smtp_use_default_credentials=True,
        default_from_address="default_from_address_example",
        default_from_display_name="default_from_display_name_example",
    )
    try:
        api_response = api_instance.api_setting_management_emailing_post(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling EmailSettingsApi->api_setting_management_emailing_post: %s\n" % e)
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
[**UpdateEmailSettingsDto**](../../models/UpdateEmailSettingsDto.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpdateEmailSettingsDto**](../../models/UpdateEmailSettingsDto.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpdateEmailSettingsDto**](../../models/UpdateEmailSettingsDto.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#api_setting_management_emailing_post.ApiResponseFor200) | Success
403 | [ApiResponseFor403](#api_setting_management_emailing_post.ApiResponseFor403) | Forbidden
401 | [ApiResponseFor401](#api_setting_management_emailing_post.ApiResponseFor401) | Unauthorized
400 | [ApiResponseFor400](#api_setting_management_emailing_post.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#api_setting_management_emailing_post.ApiResponseFor404) | Not Found
501 | [ApiResponseFor501](#api_setting_management_emailing_post.ApiResponseFor501) | Server Error
500 | [ApiResponseFor500](#api_setting_management_emailing_post.ApiResponseFor500) | Server Error

#### api_setting_management_emailing_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### api_setting_management_emailing_post.ApiResponseFor403
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


#### api_setting_management_emailing_post.ApiResponseFor401
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


#### api_setting_management_emailing_post.ApiResponseFor400
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


#### api_setting_management_emailing_post.ApiResponseFor404
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


#### api_setting_management_emailing_post.ApiResponseFor501
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


#### api_setting_management_emailing_post.ApiResponseFor500
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

# **api_setting_management_emailing_send_test_email_post**
<a name="api_setting_management_emailing_send_test_email_post"></a>
> api_setting_management_emailing_send_test_email_post()



### Example

* OAuth Authentication (oauth2):
```python
import openapi_client
from openapi_client.apis.tags import email_settings_api
from openapi_client.model.remote_service_error_response import RemoteServiceErrorResponse
from openapi_client.model.send_test_email_input import SendTestEmailInput
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
    api_instance = email_settings_api.EmailSettingsApi(api_client)

    # example passing only optional values
    body = SendTestEmailInput(
        sender_email_address="sender_email_address_example",
        target_email_address="target_email_address_example",
        subject="subject_example",
        body="body_example",
    )
    try:
        api_response = api_instance.api_setting_management_emailing_send_test_email_post(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling EmailSettingsApi->api_setting_management_emailing_send_test_email_post: %s\n" % e)
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
[**SendTestEmailInput**](../../models/SendTestEmailInput.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SendTestEmailInput**](../../models/SendTestEmailInput.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SendTestEmailInput**](../../models/SendTestEmailInput.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#api_setting_management_emailing_send_test_email_post.ApiResponseFor200) | Success
403 | [ApiResponseFor403](#api_setting_management_emailing_send_test_email_post.ApiResponseFor403) | Forbidden
401 | [ApiResponseFor401](#api_setting_management_emailing_send_test_email_post.ApiResponseFor401) | Unauthorized
400 | [ApiResponseFor400](#api_setting_management_emailing_send_test_email_post.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#api_setting_management_emailing_send_test_email_post.ApiResponseFor404) | Not Found
501 | [ApiResponseFor501](#api_setting_management_emailing_send_test_email_post.ApiResponseFor501) | Server Error
500 | [ApiResponseFor500](#api_setting_management_emailing_send_test_email_post.ApiResponseFor500) | Server Error

#### api_setting_management_emailing_send_test_email_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

#### api_setting_management_emailing_send_test_email_post.ApiResponseFor403
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


#### api_setting_management_emailing_send_test_email_post.ApiResponseFor401
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


#### api_setting_management_emailing_send_test_email_post.ApiResponseFor400
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


#### api_setting_management_emailing_send_test_email_post.ApiResponseFor404
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


#### api_setting_management_emailing_send_test_email_post.ApiResponseFor501
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


#### api_setting_management_emailing_send_test_email_post.ApiResponseFor500
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

