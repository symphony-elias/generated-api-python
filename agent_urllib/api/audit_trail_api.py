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


class AuditTrailApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v1_audittrail_privilegeduser_get(self, session_token, key_manager_token, start_timestamp, **kwargs):  # noqa: E501
        """Get a list of  actions performed by a privileged account acting as privileged user given a period of time.  # noqa: E501

        Get a list of actions performed by a privileged account acting as privileged user given a period of time.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_audittrail_privilegeduser_get(session_token, key_manager_token, start_timestamp, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str session_token: Session authentication token. (required)
        :param str key_manager_token: Key Manager authentication token. (required)
        :param int start_timestamp: Start timestamp in unix timestamp in millseconds.  (required)
        :param int end_timestamp: End timestamp in unix timestamp in millseconds. If not specified, it assumes to be current time. 
        :param str before: Return results from an opaque “before” cursor value as presented via a response cursor. 
        :param str after: Return results from an opaque “after” cursor value as presented via a response cursor. 
        :param int limit: Max No. of violations to return. If no value is provided, 50 is the default. Some maximums for limit may be enforced for performance reasons. The maximum supported value is 500. 
        :param int initiator_id: If present, only the initiator with this initiator <user id> will be returned. 
        :param str role: If present, only the audit trail initiated by s user with privileged role acting as privileged user will be returned. Privileged eliglible roles: User Provisioning (USER_PROVISIONING), Content Management (CONTENT_MANAGEMENT), Expression Filter Policy Management (EF_POLICY_MANAGEMENT), SCO (SUPER_COMPLIANCE_OFFICER), CO (COMPLIANCE_OFFICER), Super admin (SUPER_ADMINISTRATOR), Admin (ADMINISTRATOR), L1 (L1_SUPPORT), L2 (L2_SUPPORT), Scope Manager (SCOPE_MANAGEMENT) 
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: V1AuditTrailInitiatorList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.v1_audittrail_privilegeduser_get_with_http_info(session_token, key_manager_token, start_timestamp, **kwargs)  # noqa: E501

    def v1_audittrail_privilegeduser_get_with_http_info(self, session_token, key_manager_token, start_timestamp, **kwargs):  # noqa: E501
        """Get a list of  actions performed by a privileged account acting as privileged user given a period of time.  # noqa: E501

        Get a list of actions performed by a privileged account acting as privileged user given a period of time.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_audittrail_privilegeduser_get_with_http_info(session_token, key_manager_token, start_timestamp, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str session_token: Session authentication token. (required)
        :param str key_manager_token: Key Manager authentication token. (required)
        :param int start_timestamp: Start timestamp in unix timestamp in millseconds.  (required)
        :param int end_timestamp: End timestamp in unix timestamp in millseconds. If not specified, it assumes to be current time. 
        :param str before: Return results from an opaque “before” cursor value as presented via a response cursor. 
        :param str after: Return results from an opaque “after” cursor value as presented via a response cursor. 
        :param int limit: Max No. of violations to return. If no value is provided, 50 is the default. Some maximums for limit may be enforced for performance reasons. The maximum supported value is 500. 
        :param int initiator_id: If present, only the initiator with this initiator <user id> will be returned. 
        :param str role: If present, only the audit trail initiated by s user with privileged role acting as privileged user will be returned. Privileged eliglible roles: User Provisioning (USER_PROVISIONING), Content Management (CONTENT_MANAGEMENT), Expression Filter Policy Management (EF_POLICY_MANAGEMENT), SCO (SUPER_COMPLIANCE_OFFICER), CO (COMPLIANCE_OFFICER), Super admin (SUPER_ADMINISTRATOR), Admin (ADMINISTRATOR), L1 (L1_SUPPORT), L2 (L2_SUPPORT), Scope Manager (SCOPE_MANAGEMENT) 
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(V1AuditTrailInitiatorList, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'session_token',
            'key_manager_token',
            'start_timestamp',
            'end_timestamp',
            'before',
            'after',
            'limit',
            'initiator_id',
            'role'
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
                    " to method v1_audittrail_privilegeduser_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'session_token' is set
        if self.api_client.client_side_validation and ('session_token' not in local_var_params or  # noqa: E501
                                                        local_var_params['session_token'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `session_token` when calling `v1_audittrail_privilegeduser_get`")  # noqa: E501
        # verify the required parameter 'key_manager_token' is set
        if self.api_client.client_side_validation and ('key_manager_token' not in local_var_params or  # noqa: E501
                                                        local_var_params['key_manager_token'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `key_manager_token` when calling `v1_audittrail_privilegeduser_get`")  # noqa: E501
        # verify the required parameter 'start_timestamp' is set
        if self.api_client.client_side_validation and ('start_timestamp' not in local_var_params or  # noqa: E501
                                                        local_var_params['start_timestamp'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `start_timestamp` when calling `v1_audittrail_privilegeduser_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_timestamp' in local_var_params and local_var_params['start_timestamp'] is not None:  # noqa: E501
            query_params.append(('startTimestamp', local_var_params['start_timestamp']))  # noqa: E501
        if 'end_timestamp' in local_var_params and local_var_params['end_timestamp'] is not None:  # noqa: E501
            query_params.append(('endTimestamp', local_var_params['end_timestamp']))  # noqa: E501
        if 'before' in local_var_params and local_var_params['before'] is not None:  # noqa: E501
            query_params.append(('before', local_var_params['before']))  # noqa: E501
        if 'after' in local_var_params and local_var_params['after'] is not None:  # noqa: E501
            query_params.append(('after', local_var_params['after']))  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'initiator_id' in local_var_params and local_var_params['initiator_id'] is not None:  # noqa: E501
            query_params.append(('initiatorId', local_var_params['initiator_id']))  # noqa: E501
        if 'role' in local_var_params and local_var_params['role'] is not None:  # noqa: E501
            query_params.append(('role', local_var_params['role']))  # noqa: E501

        header_params = {}
        if 'session_token' in local_var_params:
            header_params['sessionToken'] = local_var_params['session_token']  # noqa: E501
        if 'key_manager_token' in local_var_params:
            header_params['keyManagerToken'] = local_var_params['key_manager_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/audittrail/privilegeduser', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1AuditTrailInitiatorList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
