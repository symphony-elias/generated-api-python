# coding: utf-8

"""
    Agent API

    This document refers to Symphony API calls to send and receive messages and content. They need the on-premise Agent installed to perform decryption/encryption of content.  - sessionToken and keyManagerToken can be obtained by calling the authenticationAPI on the symphony back end and the key manager respectively. Refer to the methods described in authenticatorAPI.yaml. - Actions are defined to be atomic, ie will succeed in their entirety or fail and have changed nothing. - If it returns a 40X status then it will have sent no message to any stream even if a request to aome subset of the requested streams would have succeeded. - If this contract cannot be met for any reason then this is an error and the response code will be 50X. - MessageML is a markup language for messages. See reference here: https://rest-api.symphony.com/docs/messagemlv2 - **Real Time Events**: The following events are returned when reading from a real time messages and events stream (\"datafeed\"). These events will be returned for datafeeds created with the v5 endpoints. To know more about the endpoints, refer to Create Messages/Events Stream and Read Messages/Events Stream. Unless otherwise specified, all events were added in 1.46.   # noqa: E501

    The version of the OpenAPI document: 20.10.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from openapi_client.api_client import ApiClient
from openapi_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class UtilApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v1_util_echo_post(self, session_token, key_manager_token, echo_input, **kwargs):  # noqa: E501
        """Test endpoint, returns input.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_util_echo_post(session_token, key_manager_token, echo_input, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str session_token: Session authentication token. (required)
        :param str key_manager_token: Key Manager authentication token. (required)
        :param SimpleMessage echo_input: Message in plain text (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: SimpleMessage
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.v1_util_echo_post_with_http_info(session_token, key_manager_token, echo_input, **kwargs)  # noqa: E501

    def v1_util_echo_post_with_http_info(self, session_token, key_manager_token, echo_input, **kwargs):  # noqa: E501
        """Test endpoint, returns input.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_util_echo_post_with_http_info(session_token, key_manager_token, echo_input, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str session_token: Session authentication token. (required)
        :param str key_manager_token: Key Manager authentication token. (required)
        :param SimpleMessage echo_input: Message in plain text (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(SimpleMessage, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'session_token',
            'key_manager_token',
            'echo_input'
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
                    " to method v1_util_echo_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'session_token' is set
        if self.api_client.client_side_validation and ('session_token' not in local_var_params or  # noqa: E501
                                                        local_var_params['session_token'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `session_token` when calling `v1_util_echo_post`")  # noqa: E501
        # verify the required parameter 'key_manager_token' is set
        if self.api_client.client_side_validation and ('key_manager_token' not in local_var_params or  # noqa: E501
                                                        local_var_params['key_manager_token'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `key_manager_token` when calling `v1_util_echo_post`")  # noqa: E501
        # verify the required parameter 'echo_input' is set
        if self.api_client.client_side_validation and ('echo_input' not in local_var_params or  # noqa: E501
                                                        local_var_params['echo_input'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `echo_input` when calling `v1_util_echo_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'session_token' in local_var_params:
            header_params['sessionToken'] = local_var_params['session_token']  # noqa: E501
        if 'key_manager_token' in local_var_params:
            header_params['keyManagerToken'] = local_var_params['key_manager_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'echo_input' in local_var_params:
            body_params = local_var_params['echo_input']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/util/echo', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SimpleMessage',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
