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


class ChannelSubscriptionResponse(object):
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
        'requested_subscription': 'int',
        'successful_subscription': 'int',
        'failed_subscription': 'int',
        'subscription_errors': 'list[ChannelSubscriptionError]'
    }

    attribute_map = {
        'requested_subscription': 'requestedSubscription',
        'successful_subscription': 'successfulSubscription',
        'failed_subscription': 'failedSubscription',
        'subscription_errors': 'subscriptionErrors'
    }

    def __init__(self, requested_subscription=None, successful_subscription=None, failed_subscription=None, subscription_errors=None, local_vars_configuration=None):  # noqa: E501
        """ChannelSubscriptionResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._requested_subscription = None
        self._successful_subscription = None
        self._failed_subscription = None
        self._subscription_errors = None
        self.discriminator = None

        if requested_subscription is not None:
            self.requested_subscription = requested_subscription
        if successful_subscription is not None:
            self.successful_subscription = successful_subscription
        if failed_subscription is not None:
            self.failed_subscription = failed_subscription
        if subscription_errors is not None:
            self.subscription_errors = subscription_errors

    @property
    def requested_subscription(self):
        """Gets the requested_subscription of this ChannelSubscriptionResponse.  # noqa: E501

        The number of requested userIds to subscribe  # noqa: E501

        :return: The requested_subscription of this ChannelSubscriptionResponse.  # noqa: E501
        :rtype: int
        """
        return self._requested_subscription

    @requested_subscription.setter
    def requested_subscription(self, requested_subscription):
        """Sets the requested_subscription of this ChannelSubscriptionResponse.

        The number of requested userIds to subscribe  # noqa: E501

        :param requested_subscription: The requested_subscription of this ChannelSubscriptionResponse.  # noqa: E501
        :type: int
        """

        self._requested_subscription = requested_subscription

    @property
    def successful_subscription(self):
        """Gets the successful_subscription of this ChannelSubscriptionResponse.  # noqa: E501

        The number of successful subscriptions done  # noqa: E501

        :return: The successful_subscription of this ChannelSubscriptionResponse.  # noqa: E501
        :rtype: int
        """
        return self._successful_subscription

    @successful_subscription.setter
    def successful_subscription(self, successful_subscription):
        """Sets the successful_subscription of this ChannelSubscriptionResponse.

        The number of successful subscriptions done  # noqa: E501

        :param successful_subscription: The successful_subscription of this ChannelSubscriptionResponse.  # noqa: E501
        :type: int
        """

        self._successful_subscription = successful_subscription

    @property
    def failed_subscription(self):
        """Gets the failed_subscription of this ChannelSubscriptionResponse.  # noqa: E501

        The number of subscription failures  # noqa: E501

        :return: The failed_subscription of this ChannelSubscriptionResponse.  # noqa: E501
        :rtype: int
        """
        return self._failed_subscription

    @failed_subscription.setter
    def failed_subscription(self, failed_subscription):
        """Sets the failed_subscription of this ChannelSubscriptionResponse.

        The number of subscription failures  # noqa: E501

        :param failed_subscription: The failed_subscription of this ChannelSubscriptionResponse.  # noqa: E501
        :type: int
        """

        self._failed_subscription = failed_subscription

    @property
    def subscription_errors(self):
        """Gets the subscription_errors of this ChannelSubscriptionResponse.  # noqa: E501


        :return: The subscription_errors of this ChannelSubscriptionResponse.  # noqa: E501
        :rtype: list[ChannelSubscriptionError]
        """
        return self._subscription_errors

    @subscription_errors.setter
    def subscription_errors(self, subscription_errors):
        """Sets the subscription_errors of this ChannelSubscriptionResponse.


        :param subscription_errors: The subscription_errors of this ChannelSubscriptionResponse.  # noqa: E501
        :type: list[ChannelSubscriptionError]
        """

        self._subscription_errors = subscription_errors

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
        if not isinstance(other, ChannelSubscriptionResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ChannelSubscriptionResponse):
            return True

        return self.to_dict() != other.to_dict()
