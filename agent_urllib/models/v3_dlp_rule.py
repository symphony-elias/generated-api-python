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


class V3DLPRule(object):
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
        'id': 'str',
        'type': 'str',
        'name': 'str',
        'text_match_config': 'V3DLPTextMatchConfig',
        'file_size_config': 'V3DLPFileSizeConfig',
        'file_extension_config': 'V3DLPFileExtensionConfig',
        'file_password_config': 'V3DLPFilePasswordConfig',
        'file_classifier_config': 'V3DLPFileClassifierConfig'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'name': 'name',
        'text_match_config': 'textMatchConfig',
        'file_size_config': 'fileSizeConfig',
        'file_extension_config': 'fileExtensionConfig',
        'file_password_config': 'filePasswordConfig',
        'file_classifier_config': 'fileClassifierConfig'
    }

    def __init__(self, id=None, type=None, name=None, text_match_config=None, file_size_config=None, file_extension_config=None, file_password_config=None, file_classifier_config=None, local_vars_configuration=None):  # noqa: E501
        """V3DLPRule - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._type = None
        self._name = None
        self._text_match_config = None
        self._file_size_config = None
        self._file_extension_config = None
        self._file_password_config = None
        self._file_classifier_config = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.type = type
        self.name = name
        if text_match_config is not None:
            self.text_match_config = text_match_config
        if file_size_config is not None:
            self.file_size_config = file_size_config
        if file_extension_config is not None:
            self.file_extension_config = file_extension_config
        if file_password_config is not None:
            self.file_password_config = file_password_config
        if file_classifier_config is not None:
            self.file_classifier_config = file_classifier_config

    @property
    def id(self):
        """Gets the id of this V3DLPRule.  # noqa: E501


        :return: The id of this V3DLPRule.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V3DLPRule.


        :param id: The id of this V3DLPRule.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this V3DLPRule.  # noqa: E501

        Type of a rule used by policy. Can be [\"UNKNOWN\", \"TEXT_MATCH\", \"FILE_EXTENSION\", \"FILE_SIZE\", \"FILE_PASSWORD\", \"FILE_CLASSIFIER\"].  # noqa: E501

        :return: The type of this V3DLPRule.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this V3DLPRule.

        Type of a rule used by policy. Can be [\"UNKNOWN\", \"TEXT_MATCH\", \"FILE_EXTENSION\", \"FILE_SIZE\", \"FILE_PASSWORD\", \"FILE_CLASSIFIER\"].  # noqa: E501

        :param type: The type of this V3DLPRule.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this V3DLPRule.  # noqa: E501

        Name for rule.  # noqa: E501

        :return: The name of this V3DLPRule.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V3DLPRule.

        Name for rule.  # noqa: E501

        :param name: The name of this V3DLPRule.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def text_match_config(self):
        """Gets the text_match_config of this V3DLPRule.  # noqa: E501


        :return: The text_match_config of this V3DLPRule.  # noqa: E501
        :rtype: V3DLPTextMatchConfig
        """
        return self._text_match_config

    @text_match_config.setter
    def text_match_config(self, text_match_config):
        """Sets the text_match_config of this V3DLPRule.


        :param text_match_config: The text_match_config of this V3DLPRule.  # noqa: E501
        :type: V3DLPTextMatchConfig
        """

        self._text_match_config = text_match_config

    @property
    def file_size_config(self):
        """Gets the file_size_config of this V3DLPRule.  # noqa: E501


        :return: The file_size_config of this V3DLPRule.  # noqa: E501
        :rtype: V3DLPFileSizeConfig
        """
        return self._file_size_config

    @file_size_config.setter
    def file_size_config(self, file_size_config):
        """Sets the file_size_config of this V3DLPRule.


        :param file_size_config: The file_size_config of this V3DLPRule.  # noqa: E501
        :type: V3DLPFileSizeConfig
        """

        self._file_size_config = file_size_config

    @property
    def file_extension_config(self):
        """Gets the file_extension_config of this V3DLPRule.  # noqa: E501


        :return: The file_extension_config of this V3DLPRule.  # noqa: E501
        :rtype: V3DLPFileExtensionConfig
        """
        return self._file_extension_config

    @file_extension_config.setter
    def file_extension_config(self, file_extension_config):
        """Sets the file_extension_config of this V3DLPRule.


        :param file_extension_config: The file_extension_config of this V3DLPRule.  # noqa: E501
        :type: V3DLPFileExtensionConfig
        """

        self._file_extension_config = file_extension_config

    @property
    def file_password_config(self):
        """Gets the file_password_config of this V3DLPRule.  # noqa: E501


        :return: The file_password_config of this V3DLPRule.  # noqa: E501
        :rtype: V3DLPFilePasswordConfig
        """
        return self._file_password_config

    @file_password_config.setter
    def file_password_config(self, file_password_config):
        """Sets the file_password_config of this V3DLPRule.


        :param file_password_config: The file_password_config of this V3DLPRule.  # noqa: E501
        :type: V3DLPFilePasswordConfig
        """

        self._file_password_config = file_password_config

    @property
    def file_classifier_config(self):
        """Gets the file_classifier_config of this V3DLPRule.  # noqa: E501


        :return: The file_classifier_config of this V3DLPRule.  # noqa: E501
        :rtype: V3DLPFileClassifierConfig
        """
        return self._file_classifier_config

    @file_classifier_config.setter
    def file_classifier_config(self, file_classifier_config):
        """Sets the file_classifier_config of this V3DLPRule.


        :param file_classifier_config: The file_classifier_config of this V3DLPRule.  # noqa: E501
        :type: V3DLPFileClassifierConfig
        """

        self._file_classifier_config = file_classifier_config

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
        if not isinstance(other, V3DLPRule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V3DLPRule):
            return True

        return self.to_dict() != other.to_dict()
