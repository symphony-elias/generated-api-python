"""
    Authenticator API

    For bots and other on-premise processes to authenticate. Once authenticated, the bot will be able to use the methods described in serviceAPI.yaml and agentAPI.yaml.  Connections to the servers will be over client authenticated TLS, the servers for this API will perform the authentication by inspecting the certificate presented by the SSLSocketClient.  There will be two implementations of this API, one on your Pod and one on the Key Manager. In order to fully authenticate, an API client will have to call both of these implementations and pass both of the session tokens returned as headers in all subsequent requests to the Symphony API.   # noqa: E501

    The version of the OpenAPI document: 20.10.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from aiohttp_gen_api.api_client import ApiClient, Endpoint
from aiohttp_gen_api.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from aiohttp_gen_api.auth_model.error import Error
from aiohttp_gen_api.auth_model.obo_auth_response import OboAuthResponse


class AuthenticationApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __v1_app_username_username_authenticate_post(
            self,
            username,
            session_token,
            **kwargs
        ):
            """PROVISIONAL - Authenicate an application in a delegated context to act on behalf of a user  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = auth_api.v1_app_username_username_authenticate_post(username, session_token, async_req=True)
            >>> result = thread.get()

            Args:
                username (str): username
                session_token (str): Authorization token obtains from app/authenicate API

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                OboAuthResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['username'] = \
                username
            kwargs['session_token'] = \
                session_token
            return self.call_with_http_info(**kwargs)

        self.v1_app_username_username_authenticate_post = Endpoint(
            settings={
                'response_type': (OboAuthResponse,),
                'auth': [],
                'endpoint_path': '/v1/app/username/{username}/authenticate',
                'operation_id': 'v1_app_username_username_authenticate_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'username',
                    'session_token',
                ],
                'required': [
                    'username',
                    'session_token',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'username':
                        (str,),
                    'session_token':
                        (str,),
                },
                'attribute_map': {
                    'username': 'username',
                    'session_token': 'sessionToken',
                },
                'location_map': {
                    'username': 'path',
                    'session_token': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__v1_app_username_username_authenticate_post
        )
