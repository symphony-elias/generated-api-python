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


class V1DLPViolation(object):
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
        'enforcement_event_id': 'str',
        'entity_id': 'str',
        'create_time': 'int',
        'last_modified': 'int',
        'requester_id': 'int',
        'matched_policies': 'list[V1DLPMatchedPolicy]',
        'action': 'str',
        'outcome': 'V1DLPOutcome',
        'version': 'str',
        'ignore_dl_pwarning': 'bool'
    }

    attribute_map = {
        'enforcement_event_id': 'enforcementEventID',
        'entity_id': 'entityID',
        'create_time': 'createTime',
        'last_modified': 'lastModified',
        'requester_id': 'requesterId',
        'matched_policies': 'matchedPolicies',
        'action': 'action',
        'outcome': 'outcome',
        'version': 'version',
        'ignore_dl_pwarning': 'ignoreDLPwarning'
    }

    def __init__(self, enforcement_event_id=None, entity_id=None, create_time=None, last_modified=None, requester_id=None, matched_policies=None, action=None, outcome=None, version=None, ignore_dl_pwarning=None, local_vars_configuration=None):  # noqa: E501
        """V1DLPViolation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._enforcement_event_id = None
        self._entity_id = None
        self._create_time = None
        self._last_modified = None
        self._requester_id = None
        self._matched_policies = None
        self._action = None
        self._outcome = None
        self._version = None
        self._ignore_dl_pwarning = None
        self.discriminator = None

        if enforcement_event_id is not None:
            self.enforcement_event_id = enforcement_event_id
        if entity_id is not None:
            self.entity_id = entity_id
        if create_time is not None:
            self.create_time = create_time
        if last_modified is not None:
            self.last_modified = last_modified
        if requester_id is not None:
            self.requester_id = requester_id
        if matched_policies is not None:
            self.matched_policies = matched_policies
        if action is not None:
            self.action = action
        if outcome is not None:
            self.outcome = outcome
        if version is not None:
            self.version = version
        if ignore_dl_pwarning is not None:
            self.ignore_dl_pwarning = ignore_dl_pwarning

    @property
    def enforcement_event_id(self):
        """Gets the enforcement_event_id of this V1DLPViolation.  # noqa: E501

        Enforcement event ID. Unique ID that identifies this enforcement.  # noqa: E501

        :return: The enforcement_event_id of this V1DLPViolation.  # noqa: E501
        :rtype: str
        """
        return self._enforcement_event_id

    @enforcement_event_id.setter
    def enforcement_event_id(self, enforcement_event_id):
        """Sets the enforcement_event_id of this V1DLPViolation.

        Enforcement event ID. Unique ID that identifies this enforcement.  # noqa: E501

        :param enforcement_event_id: The enforcement_event_id of this V1DLPViolation.  # noqa: E501
        :type: str
        """

        self._enforcement_event_id = enforcement_event_id

    @property
    def entity_id(self):
        """Gets the entity_id of this V1DLPViolation.  # noqa: E501

        Entity ID is the content Id of the violation, for example, for messages, its the Id of the message  # noqa: E501

        :return: The entity_id of this V1DLPViolation.  # noqa: E501
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this V1DLPViolation.

        Entity ID is the content Id of the violation, for example, for messages, its the Id of the message  # noqa: E501

        :param entity_id: The entity_id of this V1DLPViolation.  # noqa: E501
        :type: str
        """

        self._entity_id = entity_id

    @property
    def create_time(self):
        """Gets the create_time of this V1DLPViolation.  # noqa: E501

        Timestamp of the violation in milliseconds since Jan 1 1970  # noqa: E501

        :return: The create_time of this V1DLPViolation.  # noqa: E501
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this V1DLPViolation.

        Timestamp of the violation in milliseconds since Jan 1 1970  # noqa: E501

        :param create_time: The create_time of this V1DLPViolation.  # noqa: E501
        :type: int
        """

        self._create_time = create_time

    @property
    def last_modified(self):
        """Gets the last_modified of this V1DLPViolation.  # noqa: E501

        Timestamp of the last modification of violation in milliseconds since Jan 1 1970  # noqa: E501

        :return: The last_modified of this V1DLPViolation.  # noqa: E501
        :rtype: int
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this V1DLPViolation.

        Timestamp of the last modification of violation in milliseconds since Jan 1 1970  # noqa: E501

        :param last_modified: The last_modified of this V1DLPViolation.  # noqa: E501
        :type: int
        """

        self._last_modified = last_modified

    @property
    def requester_id(self):
        """Gets the requester_id of this V1DLPViolation.  # noqa: E501

        Id of the requester responsible for the message/stream/signal  # noqa: E501

        :return: The requester_id of this V1DLPViolation.  # noqa: E501
        :rtype: int
        """
        return self._requester_id

    @requester_id.setter
    def requester_id(self, requester_id):
        """Sets the requester_id of this V1DLPViolation.

        Id of the requester responsible for the message/stream/signal  # noqa: E501

        :param requester_id: The requester_id of this V1DLPViolation.  # noqa: E501
        :type: int
        """

        self._requester_id = requester_id

    @property
    def matched_policies(self):
        """Gets the matched_policies of this V1DLPViolation.  # noqa: E501

        List of policies that matched the violation.  # noqa: E501

        :return: The matched_policies of this V1DLPViolation.  # noqa: E501
        :rtype: list[V1DLPMatchedPolicy]
        """
        return self._matched_policies

    @matched_policies.setter
    def matched_policies(self, matched_policies):
        """Sets the matched_policies of this V1DLPViolation.

        List of policies that matched the violation.  # noqa: E501

        :param matched_policies: The matched_policies of this V1DLPViolation.  # noqa: E501
        :type: list[V1DLPMatchedPolicy]
        """

        self._matched_policies = matched_policies

    @property
    def action(self):
        """Gets the action of this V1DLPViolation.  # noqa: E501

        action taken such as BLOCK or WARN.  See outcome for a more detailed description of the outcome this action.  # noqa: E501

        :return: The action of this V1DLPViolation.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this V1DLPViolation.

        action taken such as BLOCK or WARN.  See outcome for a more detailed description of the outcome this action.  # noqa: E501

        :param action: The action of this V1DLPViolation.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def outcome(self):
        """Gets the outcome of this V1DLPViolation.  # noqa: E501


        :return: The outcome of this V1DLPViolation.  # noqa: E501
        :rtype: V1DLPOutcome
        """
        return self._outcome

    @outcome.setter
    def outcome(self, outcome):
        """Sets the outcome of this V1DLPViolation.


        :param outcome: The outcome of this V1DLPViolation.  # noqa: E501
        :type: V1DLPOutcome
        """

        self._outcome = outcome

    @property
    def version(self):
        """Gets the version of this V1DLPViolation.  # noqa: E501

        Version of application which processed the message and produced this violation.  # noqa: E501

        :return: The version of this V1DLPViolation.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this V1DLPViolation.

        Version of application which processed the message and produced this violation.  # noqa: E501

        :param version: The version of this V1DLPViolation.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def ignore_dl_pwarning(self):
        """Gets the ignore_dl_pwarning of this V1DLPViolation.  # noqa: E501

        Did the user chose to ignore DLP warning that was presented?  # noqa: E501

        :return: The ignore_dl_pwarning of this V1DLPViolation.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_dl_pwarning

    @ignore_dl_pwarning.setter
    def ignore_dl_pwarning(self, ignore_dl_pwarning):
        """Sets the ignore_dl_pwarning of this V1DLPViolation.

        Did the user chose to ignore DLP warning that was presented?  # noqa: E501

        :param ignore_dl_pwarning: The ignore_dl_pwarning of this V1DLPViolation.  # noqa: E501
        :type: bool
        """

        self._ignore_dl_pwarning = ignore_dl_pwarning

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
        if not isinstance(other, V1DLPViolation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1DLPViolation):
            return True

        return self.to_dict() != other.to_dict()