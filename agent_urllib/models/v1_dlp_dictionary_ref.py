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

from openapi_client.configuration import Configuration


class V1DLPDictionaryRef(object):
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
        'dict_id': 'str',
        'name': 'str',
        'version': 'str'
    }

    attribute_map = {
        'dict_id': 'dictId',
        'name': 'name',
        'version': 'version'
    }

    def __init__(self, dict_id=None, name=None, version=None, local_vars_configuration=None):  # noqa: E501
        """V1DLPDictionaryRef - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._dict_id = None
        self._name = None
        self._version = None
        self.discriminator = None

        if dict_id is not None:
            self.dict_id = dict_id
        self.name = name
        if version is not None:
            self.version = version

    @property
    def dict_id(self):
        """Gets the dict_id of this V1DLPDictionaryRef.  # noqa: E501

        Unique dictionary id  # noqa: E501

        :return: The dict_id of this V1DLPDictionaryRef.  # noqa: E501
        :rtype: str
        """
        return self._dict_id

    @dict_id.setter
    def dict_id(self, dict_id):
        """Sets the dict_id of this V1DLPDictionaryRef.

        Unique dictionary id  # noqa: E501

        :param dict_id: The dict_id of this V1DLPDictionaryRef.  # noqa: E501
        :type: str
        """

        self._dict_id = dict_id

    @property
    def name(self):
        """Gets the name of this V1DLPDictionaryRef.  # noqa: E501

        Unique name of a dictionary, max 30 characters, with trimmed leading and trailing blank spaces.  # noqa: E501

        :return: The name of this V1DLPDictionaryRef.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1DLPDictionaryRef.

        Unique name of a dictionary, max 30 characters, with trimmed leading and trailing blank spaces.  # noqa: E501

        :param name: The name of this V1DLPDictionaryRef.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def version(self):
        """Gets the version of this V1DLPDictionaryRef.  # noqa: E501

        The version of a dictionary, in format \"major.minor\". Initial value will set by backend as \"1.0\" when created. Whenever the dictionary version needs to be changed, the minor version by 1 unless minor == 999, then the major version is increased by 1 until it reaches 999.   # noqa: E501

        :return: The version of this V1DLPDictionaryRef.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this V1DLPDictionaryRef.

        The version of a dictionary, in format \"major.minor\". Initial value will set by backend as \"1.0\" when created. Whenever the dictionary version needs to be changed, the minor version by 1 unless minor == 999, then the major version is increased by 1 until it reaches 999.   # noqa: E501

        :param version: The version of this V1DLPDictionaryRef.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if not isinstance(other, V1DLPDictionaryRef):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1DLPDictionaryRef):
            return True

        return self.to_dict() != other.to_dict()