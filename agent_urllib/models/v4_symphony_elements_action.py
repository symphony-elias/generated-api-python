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


class V4SymphonyElementsAction(object):
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
        'stream': 'V4Stream',
        'form_message_id': 'str',
        'form_id': 'str',
        'form_values': 'object'
    }

    attribute_map = {
        'stream': 'stream',
        'form_message_id': 'formMessageId',
        'form_id': 'formId',
        'form_values': 'formValues'
    }

    def __init__(self, stream=None, form_message_id=None, form_id=None, form_values=None, local_vars_configuration=None):  # noqa: E501
        """V4SymphonyElementsAction - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._stream = None
        self._form_message_id = None
        self._form_id = None
        self._form_values = None
        self.discriminator = None

        if stream is not None:
            self.stream = stream
        if form_message_id is not None:
            self.form_message_id = form_message_id
        if form_id is not None:
            self.form_id = form_id
        if form_values is not None:
            self.form_values = form_values

    @property
    def stream(self):
        """Gets the stream of this V4SymphonyElementsAction.  # noqa: E501


        :return: The stream of this V4SymphonyElementsAction.  # noqa: E501
        :rtype: V4Stream
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        """Sets the stream of this V4SymphonyElementsAction.


        :param stream: The stream of this V4SymphonyElementsAction.  # noqa: E501
        :type: V4Stream
        """

        self._stream = stream

    @property
    def form_message_id(self):
        """Gets the form_message_id of this V4SymphonyElementsAction.  # noqa: E501

        The id of the message that contains the Form  # noqa: E501

        :return: The form_message_id of this V4SymphonyElementsAction.  # noqa: E501
        :rtype: str
        """
        return self._form_message_id

    @form_message_id.setter
    def form_message_id(self, form_message_id):
        """Sets the form_message_id of this V4SymphonyElementsAction.

        The id of the message that contains the Form  # noqa: E501

        :param form_message_id: The form_message_id of this V4SymphonyElementsAction.  # noqa: E501
        :type: str
        """

        self._form_message_id = form_message_id

    @property
    def form_id(self):
        """Gets the form_id of this V4SymphonyElementsAction.  # noqa: E501

        The id of the Form element  # noqa: E501

        :return: The form_id of this V4SymphonyElementsAction.  # noqa: E501
        :rtype: str
        """
        return self._form_id

    @form_id.setter
    def form_id(self, form_id):
        """Sets the form_id of this V4SymphonyElementsAction.

        The id of the Form element  # noqa: E501

        :param form_id: The form_id of this V4SymphonyElementsAction.  # noqa: E501
        :type: str
        """

        self._form_id = form_id

    @property
    def form_values(self):
        """Gets the form_values of this V4SymphonyElementsAction.  # noqa: E501

        The values (in JSON format) answered on the Form  # noqa: E501

        :return: The form_values of this V4SymphonyElementsAction.  # noqa: E501
        :rtype: object
        """
        return self._form_values

    @form_values.setter
    def form_values(self, form_values):
        """Sets the form_values of this V4SymphonyElementsAction.

        The values (in JSON format) answered on the Form  # noqa: E501

        :param form_values: The form_values of this V4SymphonyElementsAction.  # noqa: E501
        :type: object
        """

        self._form_values = form_values

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
        if not isinstance(other, V4SymphonyElementsAction):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V4SymphonyElementsAction):
            return True

        return self.to_dict() != other.to_dict()