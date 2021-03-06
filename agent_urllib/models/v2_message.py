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


class V2Message(object):
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
        'message': 'str',
        'from_user_id': 'int',
        'attachments': 'list[AttachmentInfo]'
    }

    attribute_map = {
        'message': 'message',
        'from_user_id': 'fromUserId',
        'attachments': 'attachments'
    }

    def __init__(self, message=None, from_user_id=None, attachments=None, local_vars_configuration=None):  # noqa: E501
        """V2Message - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._message = None
        self._from_user_id = None
        self._attachments = None
        self.discriminator = None

        self.message = message
        self.from_user_id = from_user_id
        if attachments is not None:
            self.attachments = attachments

    @property
    def message(self):
        """Gets the message of this V2Message.  # noqa: E501

        Message text in MessageML  # noqa: E501

        :return: The message of this V2Message.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this V2Message.

        Message text in MessageML  # noqa: E501

        :param message: The message of this V2Message.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and message is None:  # noqa: E501
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def from_user_id(self):
        """Gets the from_user_id of this V2Message.  # noqa: E501

        the Symphony userId of the user who sent the message. This will be populated by the server (and actually ignored if included when sending a message).  # noqa: E501

        :return: The from_user_id of this V2Message.  # noqa: E501
        :rtype: int
        """
        return self._from_user_id

    @from_user_id.setter
    def from_user_id(self, from_user_id):
        """Sets the from_user_id of this V2Message.

        the Symphony userId of the user who sent the message. This will be populated by the server (and actually ignored if included when sending a message).  # noqa: E501

        :param from_user_id: The from_user_id of this V2Message.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and from_user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `from_user_id`, must not be `None`")  # noqa: E501

        self._from_user_id = from_user_id

    @property
    def attachments(self):
        """Gets the attachments of this V2Message.  # noqa: E501


        :return: The attachments of this V2Message.  # noqa: E501
        :rtype: list[AttachmentInfo]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this V2Message.


        :param attachments: The attachments of this V2Message.  # noqa: E501
        :type: list[AttachmentInfo]
        """

        self._attachments = attachments

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
        if not isinstance(other, V2Message):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V2Message):
            return True

        return self.to_dict() != other.to_dict()
