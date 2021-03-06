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


class V4MessageBlastResponse(object):
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
        'messages': 'list[V4Message]',
        'errors': 'dict(str, Error)'
    }

    attribute_map = {
        'messages': 'messages',
        'errors': 'errors'
    }

    def __init__(self, messages=None, errors=None, local_vars_configuration=None):  # noqa: E501
        """V4MessageBlastResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._messages = None
        self._errors = None
        self.discriminator = None

        if messages is not None:
            self.messages = messages
        if errors is not None:
            self.errors = errors

    @property
    def messages(self):
        """Gets the messages of this V4MessageBlastResponse.  # noqa: E501

        List of messages successfully sent  # noqa: E501

        :return: The messages of this V4MessageBlastResponse.  # noqa: E501
        :rtype: list[V4Message]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """Sets the messages of this V4MessageBlastResponse.

        List of messages successfully sent  # noqa: E501

        :param messages: The messages of this V4MessageBlastResponse.  # noqa: E501
        :type: list[V4Message]
        """

        self._messages = messages

    @property
    def errors(self):
        """Gets the errors of this V4MessageBlastResponse.  # noqa: E501

        List of streams where the messages ingestion has failed  # noqa: E501

        :return: The errors of this V4MessageBlastResponse.  # noqa: E501
        :rtype: dict(str, Error)
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this V4MessageBlastResponse.

        List of streams where the messages ingestion has failed  # noqa: E501

        :param errors: The errors of this V4MessageBlastResponse.  # noqa: E501
        :type: dict(str, Error)
        """

        self._errors = errors

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
        if not isinstance(other, V4MessageBlastResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V4MessageBlastResponse):
            return True

        return self.to_dict() != other.to_dict()
