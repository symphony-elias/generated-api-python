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


class V1DLPViolationMessage(object):
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
        'violation': 'V1DLPViolation',
        'message': 'V4Message',
        'diagnostic': 'str'
    }

    attribute_map = {
        'violation': 'violation',
        'message': 'message',
        'diagnostic': 'diagnostic'
    }

    def __init__(self, violation=None, message=None, diagnostic=None, local_vars_configuration=None):  # noqa: E501
        """V1DLPViolationMessage - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._violation = None
        self._message = None
        self._diagnostic = None
        self.discriminator = None

        if violation is not None:
            self.violation = violation
        if message is not None:
            self.message = message
        if diagnostic is not None:
            self.diagnostic = diagnostic

    @property
    def violation(self):
        """Gets the violation of this V1DLPViolationMessage.  # noqa: E501


        :return: The violation of this V1DLPViolationMessage.  # noqa: E501
        :rtype: V1DLPViolation
        """
        return self._violation

    @violation.setter
    def violation(self, violation):
        """Sets the violation of this V1DLPViolationMessage.


        :param violation: The violation of this V1DLPViolationMessage.  # noqa: E501
        :type: V1DLPViolation
        """

        self._violation = violation

    @property
    def message(self):
        """Gets the message of this V1DLPViolationMessage.  # noqa: E501


        :return: The message of this V1DLPViolationMessage.  # noqa: E501
        :rtype: V4Message
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this V1DLPViolationMessage.


        :param message: The message of this V1DLPViolationMessage.  # noqa: E501
        :type: V4Message
        """

        self._message = message

    @property
    def diagnostic(self):
        """Gets the diagnostic of this V1DLPViolationMessage.  # noqa: E501

        A diagnostic message containing an error message in the event there are parsing errors. May also be present in the case of a successful call if there is useful narrative to return.   # noqa: E501

        :return: The diagnostic of this V1DLPViolationMessage.  # noqa: E501
        :rtype: str
        """
        return self._diagnostic

    @diagnostic.setter
    def diagnostic(self, diagnostic):
        """Sets the diagnostic of this V1DLPViolationMessage.

        A diagnostic message containing an error message in the event there are parsing errors. May also be present in the case of a successful call if there is useful narrative to return.   # noqa: E501

        :param diagnostic: The diagnostic of this V1DLPViolationMessage.  # noqa: E501
        :type: str
        """

        self._diagnostic = diagnostic

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
        if not isinstance(other, V1DLPViolationMessage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1DLPViolationMessage):
            return True

        return self.to_dict() != other.to_dict()
