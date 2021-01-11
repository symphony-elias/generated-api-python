# coding: utf-8

"""
    Agent API

    This document refers to Symphony API calls to send and receive messages and content. They need the on-premise Agent installed to perform decryption/encryption of content.  - sessionToken and keyManagerToken can be obtained by calling the authenticationAPI on the symphony back end and the key manager respectively. Refer to the methods described in authenticatorAPI.yaml. - Actions are defined to be atomic, ie will succeed in their entirety or fail and have changed nothing. - If it returns a 40X status then it will have sent no message to any stream even if a request to aome subset of the requested streams would have succeeded. - If this contract cannot be met for any reason then this is an error and the response code will be 50X. - MessageML is a markup language for messages. See reference here: https://rest-api.symphony.com/docs/messagemlv2 - **Real Time Events**: The following events are returned when reading from a real time messages and events stream (\"datafeed\"). These events will be returned for datafeeds created with the v5 endpoints. To know more about the endpoints, refer to Create Messages/Events Stream and Read Messages/Events Stream. Unless otherwise specified, all events were added in 1.46.   # noqa: E501

    The version of the OpenAPI document: 20.10.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from agent_urllib.configuration import Configuration


class ConnectionRequestMessage(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'requesting_user_id': 'int',
        'target_user_id': 'int',
        'first_requested_at': 'int',
        'updated_at': 'int',
        'request_counter': 'int',
        'status': 'str'
    }

    attribute_map = {
        'requesting_user_id': 'requestingUserId',
        'target_user_id': 'targetUserId',
        'first_requested_at': 'firstRequestedAt',
        'updated_at': 'updatedAt',
        'request_counter': 'requestCounter',
        'status': 'status'
    }

    def __init__(self, requesting_user_id=None, target_user_id=None, first_requested_at=None, updated_at=None, request_counter=None, status=None, local_vars_configuration=None):  # noqa: E501
        """ConnectionRequestMessage - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._requesting_user_id = None
        self._target_user_id = None
        self._first_requested_at = None
        self._updated_at = None
        self._request_counter = None
        self._status = None
        self.discriminator = None

        if requesting_user_id is not None:
            self.requesting_user_id = requesting_user_id
        if target_user_id is not None:
            self.target_user_id = target_user_id
        if first_requested_at is not None:
            self.first_requested_at = first_requested_at
        if updated_at is not None:
            self.updated_at = updated_at
        if request_counter is not None:
            self.request_counter = request_counter
        if status is not None:
            self.status = status

    @property
    def requesting_user_id(self):
        """Gets the requesting_user_id of this ConnectionRequestMessage.  # noqa: E501


        :return: The requesting_user_id of this ConnectionRequestMessage.  # noqa: E501
        :rtype: int
        """
        return self._requesting_user_id

    @requesting_user_id.setter
    def requesting_user_id(self, requesting_user_id):
        """Sets the requesting_user_id of this ConnectionRequestMessage.


        :param requesting_user_id: The requesting_user_id of this ConnectionRequestMessage.  # noqa: E501
        :type: int
        """

        self._requesting_user_id = requesting_user_id

    @property
    def target_user_id(self):
        """Gets the target_user_id of this ConnectionRequestMessage.  # noqa: E501


        :return: The target_user_id of this ConnectionRequestMessage.  # noqa: E501
        :rtype: int
        """
        return self._target_user_id

    @target_user_id.setter
    def target_user_id(self, target_user_id):
        """Sets the target_user_id of this ConnectionRequestMessage.


        :param target_user_id: The target_user_id of this ConnectionRequestMessage.  # noqa: E501
        :type: int
        """

        self._target_user_id = target_user_id

    @property
    def first_requested_at(self):
        """Gets the first_requested_at of this ConnectionRequestMessage.  # noqa: E501


        :return: The first_requested_at of this ConnectionRequestMessage.  # noqa: E501
        :rtype: int
        """
        return self._first_requested_at

    @first_requested_at.setter
    def first_requested_at(self, first_requested_at):
        """Sets the first_requested_at of this ConnectionRequestMessage.


        :param first_requested_at: The first_requested_at of this ConnectionRequestMessage.  # noqa: E501
        :type: int
        """

        self._first_requested_at = first_requested_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ConnectionRequestMessage.  # noqa: E501


        :return: The updated_at of this ConnectionRequestMessage.  # noqa: E501
        :rtype: int
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ConnectionRequestMessage.


        :param updated_at: The updated_at of this ConnectionRequestMessage.  # noqa: E501
        :type: int
        """

        self._updated_at = updated_at

    @property
    def request_counter(self):
        """Gets the request_counter of this ConnectionRequestMessage.  # noqa: E501


        :return: The request_counter of this ConnectionRequestMessage.  # noqa: E501
        :rtype: int
        """
        return self._request_counter

    @request_counter.setter
    def request_counter(self, request_counter):
        """Sets the request_counter of this ConnectionRequestMessage.


        :param request_counter: The request_counter of this ConnectionRequestMessage.  # noqa: E501
        :type: int
        """

        self._request_counter = request_counter

    @property
    def status(self):
        """Gets the status of this ConnectionRequestMessage.  # noqa: E501


        :return: The status of this ConnectionRequestMessage.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ConnectionRequestMessage.


        :param status: The status of this ConnectionRequestMessage.  # noqa: E501
        :type: str
        """

        self._status = status

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ConnectionRequestMessage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConnectionRequestMessage):
            return True

        return self.to_dict() != other.to_dict()
