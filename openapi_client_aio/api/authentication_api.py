# coding: utf-8

"""
    Login API

    For bots and other on-premise processes to authenticate. Once authenticated, the bot will be able to use the methods described in serviceAPI.yaml and agentAPI.yaml.  Authentication requests will expect the user to pass a token containing user identification information and signed by the user's private key  There will be two implementations of this API, one on your Pod and one on the Key Manager. In order to fully authenticate, an API client will have to call both of these implementations and pass both of the session tokens returned as headers in all subsequent requests to the Symphony API.   # noqa: E501

    The version of the OpenAPI document: 20.10.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from openapi_client_aio.api_client import ApiClient
from openapi_client_aio.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class AuthenticationApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def pubkey_app_authenticate_post(self, authenticate_request, **kwargs):  # noqa: E501
        """Authenticate an App with public key  # noqa: E501

        Based on an authentication request token signed by the application's RSA private key, authenticate the API caller and return a session token.  A HTTP 401 Unauthorized error is returned on errors during authentication (e.g. invalid app, malformed authentication token, app's public key not imported in the pod, invalid token signature etc.).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pubkey_app_authenticate_post(authenticate_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param AuthenticateRequest authenticate_request: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Token
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.pubkey_app_authenticate_post_with_http_info(authenticate_request, **kwargs)  # noqa: E501

    def pubkey_app_authenticate_post_with_http_info(self, authenticate_request, **kwargs):  # noqa: E501
        """Authenticate an App with public key  # noqa: E501

        Based on an authentication request token signed by the application's RSA private key, authenticate the API caller and return a session token.  A HTTP 401 Unauthorized error is returned on errors during authentication (e.g. invalid app, malformed authentication token, app's public key not imported in the pod, invalid token signature etc.).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pubkey_app_authenticate_post_with_http_info(authenticate_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param AuthenticateRequest authenticate_request: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Token, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'authenticate_request'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pubkey_app_authenticate_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'authenticate_request' is set
        if self.api_client.client_side_validation and ('authenticate_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['authenticate_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `authenticate_request` when calling `pubkey_app_authenticate_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'authenticate_request' in local_var_params:
            body_params = local_var_params['authenticate_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/pubkey/app/authenticate', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Token',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def pubkey_app_user_user_id_authenticate_post(self, session_token, user_id, **kwargs):  # noqa: E501
        """Authenticate an application in a delegated context to act on behalf of a user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pubkey_app_user_user_id_authenticate_post(session_token, user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str session_token: App Session authentication token. (required)
        :param int user_id: the user ID (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Token
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.pubkey_app_user_user_id_authenticate_post_with_http_info(session_token, user_id, **kwargs)  # noqa: E501

    def pubkey_app_user_user_id_authenticate_post_with_http_info(self, session_token, user_id, **kwargs):  # noqa: E501
        """Authenticate an application in a delegated context to act on behalf of a user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pubkey_app_user_user_id_authenticate_post_with_http_info(session_token, user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str session_token: App Session authentication token. (required)
        :param int user_id: the user ID (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Token, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'session_token',
            'user_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pubkey_app_user_user_id_authenticate_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'session_token' is set
        if self.api_client.client_side_validation and ('session_token' not in local_var_params or  # noqa: E501
                                                        local_var_params['session_token'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `session_token` when calling `pubkey_app_user_user_id_authenticate_post`")  # noqa: E501
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and ('user_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['user_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `user_id` when calling `pubkey_app_user_user_id_authenticate_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['userId'] = local_var_params['user_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'session_token' in local_var_params:
            header_params['sessionToken'] = local_var_params['session_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/pubkey/app/user/{userId}/authenticate', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Token',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def pubkey_app_username_username_authenticate_post(self, session_token, username, **kwargs):  # noqa: E501
        """Authenticate an application in a delegated context to act on behalf of a user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pubkey_app_username_username_authenticate_post(session_token, username, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str session_token: App Session authentication token. (required)
        :param str username: the username (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Token
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.pubkey_app_username_username_authenticate_post_with_http_info(session_token, username, **kwargs)  # noqa: E501

    def pubkey_app_username_username_authenticate_post_with_http_info(self, session_token, username, **kwargs):  # noqa: E501
        """Authenticate an application in a delegated context to act on behalf of a user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pubkey_app_username_username_authenticate_post_with_http_info(session_token, username, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str session_token: App Session authentication token. (required)
        :param str username: the username (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Token, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'session_token',
            'username'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pubkey_app_username_username_authenticate_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'session_token' is set
        if self.api_client.client_side_validation and ('session_token' not in local_var_params or  # noqa: E501
                                                        local_var_params['session_token'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `session_token` when calling `pubkey_app_username_username_authenticate_post`")  # noqa: E501
        # verify the required parameter 'username' is set
        if self.api_client.client_side_validation and ('username' not in local_var_params or  # noqa: E501
                                                        local_var_params['username'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `username` when calling `pubkey_app_username_username_authenticate_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'username' in local_var_params:
            path_params['username'] = local_var_params['username']  # noqa: E501

        query_params = []

        header_params = {}
        if 'session_token' in local_var_params:
            header_params['sessionToken'] = local_var_params['session_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/pubkey/app/username/{username}/authenticate', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Token',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def pubkey_authenticate_post(self, authenticate_request, **kwargs):  # noqa: E501
        """Authenticate with public key  # noqa: E501

        Based on an authentication request token signed by the caller's RSA private key, authenticate the API caller and return a session token.  A HTTP 401 Unauthorized error is returned on errors during authentication (e.g. invalid user, malformed authentication token, user's public key not imported in the pod, invalid token signature etc.).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pubkey_authenticate_post(authenticate_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param AuthenticateRequest authenticate_request: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Token
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.pubkey_authenticate_post_with_http_info(authenticate_request, **kwargs)  # noqa: E501

    def pubkey_authenticate_post_with_http_info(self, authenticate_request, **kwargs):  # noqa: E501
        """Authenticate with public key  # noqa: E501

        Based on an authentication request token signed by the caller's RSA private key, authenticate the API caller and return a session token.  A HTTP 401 Unauthorized error is returned on errors during authentication (e.g. invalid user, malformed authentication token, user's public key not imported in the pod, invalid token signature etc.).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pubkey_authenticate_post_with_http_info(authenticate_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param AuthenticateRequest authenticate_request: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Token, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'authenticate_request'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pubkey_authenticate_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'authenticate_request' is set
        if self.api_client.client_side_validation and ('authenticate_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['authenticate_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `authenticate_request` when calling `pubkey_authenticate_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'authenticate_request' in local_var_params:
            body_params = local_var_params['authenticate_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/pubkey/authenticate', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Token',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_pubkey_app_authenticate_extension_app_post(self, authenticate_request, **kwargs):  # noqa: E501
        """Authenticate extension app with public key  # noqa: E501

        Based on an authentication request token signed by the caller's RSA private key, authenticate the API caller and return a session token.  A HTTP 401 Unauthorized error is returned on errors during authentication (e.g. invalid user, malformed authentication token, user's public key not imported in the pod, invalid token signature etc.).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_pubkey_app_authenticate_extension_app_post(authenticate_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param AuthenticateExtensionAppRequest authenticate_request: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ExtensionAppTokens
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.v1_pubkey_app_authenticate_extension_app_post_with_http_info(authenticate_request, **kwargs)  # noqa: E501

    def v1_pubkey_app_authenticate_extension_app_post_with_http_info(self, authenticate_request, **kwargs):  # noqa: E501
        """Authenticate extension app with public key  # noqa: E501

        Based on an authentication request token signed by the caller's RSA private key, authenticate the API caller and return a session token.  A HTTP 401 Unauthorized error is returned on errors during authentication (e.g. invalid user, malformed authentication token, user's public key not imported in the pod, invalid token signature etc.).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_pubkey_app_authenticate_extension_app_post_with_http_info(authenticate_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param AuthenticateExtensionAppRequest authenticate_request: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ExtensionAppTokens, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'authenticate_request'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_pubkey_app_authenticate_extension_app_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'authenticate_request' is set
        if self.api_client.client_side_validation and ('authenticate_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['authenticate_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `authenticate_request` when calling `v1_pubkey_app_authenticate_extension_app_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'authenticate_request' in local_var_params:
            body_params = local_var_params['authenticate_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/pubkey/app/authenticate/extensionApp', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ExtensionAppTokens',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
