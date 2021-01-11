"""
    Agent API

    This document refers to Symphony API calls to send and receive messages and content. They need the on-premise Agent installed to perform decryption/encryption of content.  - sessionToken and keyManagerToken can be obtained by calling the authenticationAPI on the symphony back end and the key manager respectively. Refer to the methods described in authenticatorAPI.yaml. - Actions are defined to be atomic, ie will succeed in their entirety or fail and have changed nothing. - If it returns a 40X status then it will have sent no message to any stream even if a request to aome subset of the requested streams would have succeeded. - If this contract cannot be met for any reason then this is an error and the response code will be 50X. - MessageML is a markup language for messages. See reference here: https://rest-api.symphony.com/docs/messagemlv2 - **Real Time Events**: The following events are returned when reading from a real time messages and events stream (\"datafeed\"). These events will be returned for datafeeds created with the v5 endpoints. To know more about the endpoints, refer to Create Messages/Events Stream and Read Messages/Events Stream. Unless otherwise specified, all events were added in 1.46.   # noqa: E501

    The version of the OpenAPI document: 20.10.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client_urllib.api_client import ApiClient, Endpoint
from openapi_client_urllib.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from openapi_client_urllib.model.error import Error
from openapi_client_urllib.model.share_content import ShareContent
from openapi_client_urllib.model.v2_message import V2Message


class ShareApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __v3_stream_sid_share_post(
            self,
            sid,
            session_token,
            share_content,
            **kwargs
        ):
            """PROVISIONAL -  Share a piece of content into Symphony  # noqa: E501

            Given a 3rd party content (eg. news article), it can share to the given stream. The stream can be a chatroom, an IM or a multiparty IM.   # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.v3_stream_sid_share_post(sid, session_token, share_content, async_req=True)
            >>> result = thread.get()

            Args:
                sid (str): Stream ID
                session_token (str): Session authentication token.
                share_content (ShareContent):

            Keyword Args:
                key_manager_token (str): Key Manager authentication token.. [optional]
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
                V2Message
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
            kwargs['sid'] = \
                sid
            kwargs['session_token'] = \
                session_token
            kwargs['share_content'] = \
                share_content
            return self.call_with_http_info(**kwargs)

        self.v3_stream_sid_share_post = Endpoint(
            settings={
                'response_type': (V2Message,),
                'auth': [],
                'endpoint_path': '/v3/stream/{sid}/share',
                'operation_id': 'v3_stream_sid_share_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'sid',
                    'session_token',
                    'share_content',
                    'key_manager_token',
                ],
                'required': [
                    'sid',
                    'session_token',
                    'share_content',
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
                    'sid':
                        (str,),
                    'session_token':
                        (str,),
                    'share_content':
                        (ShareContent,),
                    'key_manager_token':
                        (str,),
                },
                'attribute_map': {
                    'sid': 'sid',
                    'session_token': 'sessionToken',
                    'key_manager_token': 'keyManagerToken',
                },
                'location_map': {
                    'sid': 'path',
                    'session_token': 'header',
                    'share_content': 'body',
                    'key_manager_token': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__v3_stream_sid_share_post
        )
