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


class RoomMemberPromotedToOwnerMessageAllOf(object):
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
        'promoted_by_user_id': 'int',
        'promoted_user_id': 'int'
    }

    attribute_map = {
        'promoted_by_user_id': 'promotedByUserId',
        'promoted_user_id': 'promotedUserId'
    }

    def __init__(self, promoted_by_user_id=None, promoted_user_id=None, local_vars_configuration=None):  # noqa: E501
        """RoomMemberPromotedToOwnerMessageAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._promoted_by_user_id = None
        self._promoted_user_id = None
        self.discriminator = None

        if promoted_by_user_id is not None:
            self.promoted_by_user_id = promoted_by_user_id
        if promoted_user_id is not None:
            self.promoted_user_id = promoted_user_id

    @property
    def promoted_by_user_id(self):
        """Gets the promoted_by_user_id of this RoomMemberPromotedToOwnerMessageAllOf.  # noqa: E501


        :return: The promoted_by_user_id of this RoomMemberPromotedToOwnerMessageAllOf.  # noqa: E501
        :rtype: int
        """
        return self._promoted_by_user_id

    @promoted_by_user_id.setter
    def promoted_by_user_id(self, promoted_by_user_id):
        """Sets the promoted_by_user_id of this RoomMemberPromotedToOwnerMessageAllOf.


        :param promoted_by_user_id: The promoted_by_user_id of this RoomMemberPromotedToOwnerMessageAllOf.  # noqa: E501
        :type: int
        """

        self._promoted_by_user_id = promoted_by_user_id

    @property
    def promoted_user_id(self):
        """Gets the promoted_user_id of this RoomMemberPromotedToOwnerMessageAllOf.  # noqa: E501


        :return: The promoted_user_id of this RoomMemberPromotedToOwnerMessageAllOf.  # noqa: E501
        :rtype: int
        """
        return self._promoted_user_id

    @promoted_user_id.setter
    def promoted_user_id(self, promoted_user_id):
        """Sets the promoted_user_id of this RoomMemberPromotedToOwnerMessageAllOf.


        :param promoted_user_id: The promoted_user_id of this RoomMemberPromotedToOwnerMessageAllOf.  # noqa: E501
        :type: int
        """

        self._promoted_user_id = promoted_user_id

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
        if not isinstance(other, RoomMemberPromotedToOwnerMessageAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RoomMemberPromotedToOwnerMessageAllOf):
            return True

        return self.to_dict() != other.to_dict()
