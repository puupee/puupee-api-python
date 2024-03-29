# coding: utf-8

"""
    Puupee API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from puupee-api.api_client import ApiClient
from puupee-api.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class UserLookupApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_identity_users_lookup_by_username_user_name_get(self, user_name, **kwargs):  # noqa: E501
        """api_identity_users_lookup_by_username_user_name_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_identity_users_lookup_by_username_user_name_get(user_name, async_req=True)
        >>> result = thread.get()

        :param user_name: (required)
        :type user_name: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: UserData
        """
        kwargs['_return_http_data_only'] = True
        return self.api_identity_users_lookup_by_username_user_name_get_with_http_info(user_name, **kwargs)  # noqa: E501

    def api_identity_users_lookup_by_username_user_name_get_with_http_info(self, user_name, **kwargs):  # noqa: E501
        """api_identity_users_lookup_by_username_user_name_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_identity_users_lookup_by_username_user_name_get_with_http_info(user_name, async_req=True)
        >>> result = thread.get()

        :param user_name: (required)
        :type user_name: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(UserData, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'user_name'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_identity_users_lookup_by_username_user_name_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'user_name' is set
        if self.api_client.client_side_validation and local_var_params.get('user_name') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `user_name` when calling `api_identity_users_lookup_by_username_user_name_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_name' in local_var_params:
            path_params['userName'] = local_var_params['user_name']  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        response_types_map = {
            200: "UserData",
            403: "RemoteServiceErrorResponse",
            401: "RemoteServiceErrorResponse",
            400: "RemoteServiceErrorResponse",
            404: "RemoteServiceErrorResponse",
            501: "RemoteServiceErrorResponse",
            500: "RemoteServiceErrorResponse",
        }

        return self.api_client.call_api(
            '/api/identity/users/lookup/by-username/{userName}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def api_identity_users_lookup_count_get(self, **kwargs):  # noqa: E501
        """api_identity_users_lookup_count_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_identity_users_lookup_count_get(async_req=True)
        >>> result = thread.get()

        :param filter:
        :type filter: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: int
        """
        kwargs['_return_http_data_only'] = True
        return self.api_identity_users_lookup_count_get_with_http_info(**kwargs)  # noqa: E501

    def api_identity_users_lookup_count_get_with_http_info(self, **kwargs):  # noqa: E501
        """api_identity_users_lookup_count_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_identity_users_lookup_count_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param filter:
        :type filter: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(int, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'filter'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_identity_users_lookup_count_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if local_var_params.get('filter') is not None:  # noqa: E501
            query_params.append(('Filter', local_var_params['filter']))  # noqa: E501

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        response_types_map = {
            200: "int",
            403: "RemoteServiceErrorResponse",
            401: "RemoteServiceErrorResponse",
            400: "RemoteServiceErrorResponse",
            404: "RemoteServiceErrorResponse",
            501: "RemoteServiceErrorResponse",
            500: "RemoteServiceErrorResponse",
        }

        return self.api_client.call_api(
            '/api/identity/users/lookup/count', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def api_identity_users_lookup_id_get(self, id, **kwargs):  # noqa: E501
        """api_identity_users_lookup_id_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_identity_users_lookup_id_get(id, async_req=True)
        >>> result = thread.get()

        :param id: (required)
        :type id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: UserData
        """
        kwargs['_return_http_data_only'] = True
        return self.api_identity_users_lookup_id_get_with_http_info(id, **kwargs)  # noqa: E501

    def api_identity_users_lookup_id_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """api_identity_users_lookup_id_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_identity_users_lookup_id_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param id: (required)
        :type id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(UserData, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_identity_users_lookup_id_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and local_var_params.get('id') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `api_identity_users_lookup_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        response_types_map = {
            200: "UserData",
            403: "RemoteServiceErrorResponse",
            401: "RemoteServiceErrorResponse",
            400: "RemoteServiceErrorResponse",
            404: "RemoteServiceErrorResponse",
            501: "RemoteServiceErrorResponse",
            500: "RemoteServiceErrorResponse",
        }

        return self.api_client.call_api(
            '/api/identity/users/lookup/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def api_identity_users_lookup_search_get(self, **kwargs):  # noqa: E501
        """api_identity_users_lookup_search_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_identity_users_lookup_search_get(async_req=True)
        >>> result = thread.get()

        :param filter:
        :type filter: str
        :param sorting:
        :type sorting: str
        :param skip_count:
        :type skip_count: int
        :param max_result_count:
        :type max_result_count: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: UserDataListResultDto
        """
        kwargs['_return_http_data_only'] = True
        return self.api_identity_users_lookup_search_get_with_http_info(**kwargs)  # noqa: E501

    def api_identity_users_lookup_search_get_with_http_info(self, **kwargs):  # noqa: E501
        """api_identity_users_lookup_search_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_identity_users_lookup_search_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param filter:
        :type filter: str
        :param sorting:
        :type sorting: str
        :param skip_count:
        :type skip_count: int
        :param max_result_count:
        :type max_result_count: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(UserDataListResultDto, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'filter',
            'sorting',
            'skip_count',
            'max_result_count'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_identity_users_lookup_search_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and 'skip_count' in local_var_params and local_var_params['skip_count'] > 2147483647:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `skip_count` when calling `api_identity_users_lookup_search_get`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if self.api_client.client_side_validation and 'skip_count' in local_var_params and local_var_params['skip_count'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `skip_count` when calling `api_identity_users_lookup_search_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'max_result_count' in local_var_params and local_var_params['max_result_count'] > 2147483647:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `max_result_count` when calling `api_identity_users_lookup_search_get`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if self.api_client.client_side_validation and 'max_result_count' in local_var_params and local_var_params['max_result_count'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `max_result_count` when calling `api_identity_users_lookup_search_get`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if local_var_params.get('filter') is not None:  # noqa: E501
            query_params.append(('Filter', local_var_params['filter']))  # noqa: E501
        if local_var_params.get('sorting') is not None:  # noqa: E501
            query_params.append(('Sorting', local_var_params['sorting']))  # noqa: E501
        if local_var_params.get('skip_count') is not None:  # noqa: E501
            query_params.append(('SkipCount', local_var_params['skip_count']))  # noqa: E501
        if local_var_params.get('max_result_count') is not None:  # noqa: E501
            query_params.append(('MaxResultCount', local_var_params['max_result_count']))  # noqa: E501

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        response_types_map = {
            200: "UserDataListResultDto",
            403: "RemoteServiceErrorResponse",
            401: "RemoteServiceErrorResponse",
            400: "RemoteServiceErrorResponse",
            404: "RemoteServiceErrorResponse",
            501: "RemoteServiceErrorResponse",
            500: "RemoteServiceErrorResponse",
        }

        return self.api_client.call_api(
            '/api/identity/users/lookup/search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
