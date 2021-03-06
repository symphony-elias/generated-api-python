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


class V1DLPStream(object):
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
        'name': 'str',
        'creator_pretty_name': 'str',
        'public_room': 'bool',
        'cross_pod': 'bool',
        'allow_external': 'bool',
        'creator_id': 'str',
        'room_description': 'str',
        'stream_id': 'str',
        'state': 'str',
        'type': 'str',
        'last_disabled': 'int',
        'member_add_user_enabled': 'bool',
        'active': 'bool',
        'discoverable': 'bool',
        'read_only': 'bool',
        'copy_disabled': 'bool',
        'external_owned': 'bool',
        'send_message_disabled': 'bool',
        'moderated': 'bool',
        'share_history_enabled': 'bool',
        'diagnostic': 'str'
    }

    attribute_map = {
        'name': 'name',
        'creator_pretty_name': 'creatorPrettyName',
        'public_room': 'publicRoom',
        'cross_pod': 'crossPod',
        'allow_external': 'allowExternal',
        'creator_id': 'creatorId',
        'room_description': 'roomDescription',
        'stream_id': 'streamId',
        'state': 'state',
        'type': 'type',
        'last_disabled': 'lastDisabled',
        'member_add_user_enabled': 'memberAddUserEnabled',
        'active': 'active',
        'discoverable': 'discoverable',
        'read_only': 'readOnly',
        'copy_disabled': 'copyDisabled',
        'external_owned': 'externalOwned',
        'send_message_disabled': 'sendMessageDisabled',
        'moderated': 'moderated',
        'share_history_enabled': 'shareHistoryEnabled',
        'diagnostic': 'diagnostic'
    }

    def __init__(self, name=None, creator_pretty_name=None, public_room=None, cross_pod=None, allow_external=None, creator_id=None, room_description=None, stream_id=None, state=None, type=None, last_disabled=None, member_add_user_enabled=None, active=None, discoverable=None, read_only=None, copy_disabled=None, external_owned=None, send_message_disabled=None, moderated=None, share_history_enabled=None, diagnostic=None, local_vars_configuration=None):  # noqa: E501
        """V1DLPStream - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._creator_pretty_name = None
        self._public_room = None
        self._cross_pod = None
        self._allow_external = None
        self._creator_id = None
        self._room_description = None
        self._stream_id = None
        self._state = None
        self._type = None
        self._last_disabled = None
        self._member_add_user_enabled = None
        self._active = None
        self._discoverable = None
        self._read_only = None
        self._copy_disabled = None
        self._external_owned = None
        self._send_message_disabled = None
        self._moderated = None
        self._share_history_enabled = None
        self._diagnostic = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if creator_pretty_name is not None:
            self.creator_pretty_name = creator_pretty_name
        if public_room is not None:
            self.public_room = public_room
        if cross_pod is not None:
            self.cross_pod = cross_pod
        if allow_external is not None:
            self.allow_external = allow_external
        if creator_id is not None:
            self.creator_id = creator_id
        if room_description is not None:
            self.room_description = room_description
        if stream_id is not None:
            self.stream_id = stream_id
        if state is not None:
            self.state = state
        if type is not None:
            self.type = type
        if last_disabled is not None:
            self.last_disabled = last_disabled
        if member_add_user_enabled is not None:
            self.member_add_user_enabled = member_add_user_enabled
        if active is not None:
            self.active = active
        if discoverable is not None:
            self.discoverable = discoverable
        if read_only is not None:
            self.read_only = read_only
        if copy_disabled is not None:
            self.copy_disabled = copy_disabled
        if external_owned is not None:
            self.external_owned = external_owned
        if send_message_disabled is not None:
            self.send_message_disabled = send_message_disabled
        if moderated is not None:
            self.moderated = moderated
        if share_history_enabled is not None:
            self.share_history_enabled = share_history_enabled
        if diagnostic is not None:
            self.diagnostic = diagnostic

    @property
    def name(self):
        """Gets the name of this V1DLPStream.  # noqa: E501

        Name of the Stream/Room.  # noqa: E501

        :return: The name of this V1DLPStream.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1DLPStream.

        Name of the Stream/Room.  # noqa: E501

        :param name: The name of this V1DLPStream.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def creator_pretty_name(self):
        """Gets the creator_pretty_name of this V1DLPStream.  # noqa: E501

        Name of the creator of the Room.  # noqa: E501

        :return: The creator_pretty_name of this V1DLPStream.  # noqa: E501
        :rtype: str
        """
        return self._creator_pretty_name

    @creator_pretty_name.setter
    def creator_pretty_name(self, creator_pretty_name):
        """Sets the creator_pretty_name of this V1DLPStream.

        Name of the creator of the Room.  # noqa: E501

        :param creator_pretty_name: The creator_pretty_name of this V1DLPStream.  # noqa: E501
        :type: str
        """

        self._creator_pretty_name = creator_pretty_name

    @property
    def public_room(self):
        """Gets the public_room of this V1DLPStream.  # noqa: E501

        Is this a public room?  # noqa: E501

        :return: The public_room of this V1DLPStream.  # noqa: E501
        :rtype: bool
        """
        return self._public_room

    @public_room.setter
    def public_room(self, public_room):
        """Sets the public_room of this V1DLPStream.

        Is this a public room?  # noqa: E501

        :param public_room: The public_room of this V1DLPStream.  # noqa: E501
        :type: bool
        """

        self._public_room = public_room

    @property
    def cross_pod(self):
        """Gets the cross_pod of this V1DLPStream.  # noqa: E501

        Is this a cross pod scenario?  # noqa: E501

        :return: The cross_pod of this V1DLPStream.  # noqa: E501
        :rtype: bool
        """
        return self._cross_pod

    @cross_pod.setter
    def cross_pod(self, cross_pod):
        """Sets the cross_pod of this V1DLPStream.

        Is this a cross pod scenario?  # noqa: E501

        :param cross_pod: The cross_pod of this V1DLPStream.  # noqa: E501
        :type: bool
        """

        self._cross_pod = cross_pod

    @property
    def allow_external(self):
        """Gets the allow_external of this V1DLPStream.  # noqa: E501

        Is external messaging allowed  # noqa: E501

        :return: The allow_external of this V1DLPStream.  # noqa: E501
        :rtype: bool
        """
        return self._allow_external

    @allow_external.setter
    def allow_external(self, allow_external):
        """Sets the allow_external of this V1DLPStream.

        Is external messaging allowed  # noqa: E501

        :param allow_external: The allow_external of this V1DLPStream.  # noqa: E501
        :type: bool
        """

        self._allow_external = allow_external

    @property
    def creator_id(self):
        """Gets the creator_id of this V1DLPStream.  # noqa: E501

        Id of the creator of the Room.  # noqa: E501

        :return: The creator_id of this V1DLPStream.  # noqa: E501
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this V1DLPStream.

        Id of the creator of the Room.  # noqa: E501

        :param creator_id: The creator_id of this V1DLPStream.  # noqa: E501
        :type: str
        """

        self._creator_id = creator_id

    @property
    def room_description(self):
        """Gets the room_description of this V1DLPStream.  # noqa: E501

        Description of the Room.  # noqa: E501

        :return: The room_description of this V1DLPStream.  # noqa: E501
        :rtype: str
        """
        return self._room_description

    @room_description.setter
    def room_description(self, room_description):
        """Sets the room_description of this V1DLPStream.

        Description of the Room.  # noqa: E501

        :param room_description: The room_description of this V1DLPStream.  # noqa: E501
        :type: str
        """

        self._room_description = room_description

    @property
    def stream_id(self):
        """Gets the stream_id of this V1DLPStream.  # noqa: E501

        ThreadId of the Room.  # noqa: E501

        :return: The stream_id of this V1DLPStream.  # noqa: E501
        :rtype: str
        """
        return self._stream_id

    @stream_id.setter
    def stream_id(self, stream_id):
        """Sets the stream_id of this V1DLPStream.

        ThreadId of the Room.  # noqa: E501

        :param stream_id: The stream_id of this V1DLPStream.  # noqa: E501
        :type: str
        """

        self._stream_id = stream_id

    @property
    def state(self):
        """Gets the state of this V1DLPStream.  # noqa: E501

        State of the Room (example CREATED etc)  # noqa: E501

        :return: The state of this V1DLPStream.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this V1DLPStream.

        State of the Room (example CREATED etc)  # noqa: E501

        :param state: The state of this V1DLPStream.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def type(self):
        """Gets the type of this V1DLPStream.  # noqa: E501

        Type of the Room (example ROOM (or IM or Wall))  # noqa: E501

        :return: The type of this V1DLPStream.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this V1DLPStream.

        Type of the Room (example ROOM (or IM or Wall))  # noqa: E501

        :param type: The type of this V1DLPStream.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def last_disabled(self):
        """Gets the last_disabled of this V1DLPStream.  # noqa: E501

        Timestamp of last time the room is Disabled  # noqa: E501

        :return: The last_disabled of this V1DLPStream.  # noqa: E501
        :rtype: int
        """
        return self._last_disabled

    @last_disabled.setter
    def last_disabled(self, last_disabled):
        """Sets the last_disabled of this V1DLPStream.

        Timestamp of last time the room is Disabled  # noqa: E501

        :param last_disabled: The last_disabled of this V1DLPStream.  # noqa: E501
        :type: int
        """

        self._last_disabled = last_disabled

    @property
    def member_add_user_enabled(self):
        """Gets the member_add_user_enabled of this V1DLPStream.  # noqa: E501

        Is memberAddUserEnabled  # noqa: E501

        :return: The member_add_user_enabled of this V1DLPStream.  # noqa: E501
        :rtype: bool
        """
        return self._member_add_user_enabled

    @member_add_user_enabled.setter
    def member_add_user_enabled(self, member_add_user_enabled):
        """Sets the member_add_user_enabled of this V1DLPStream.

        Is memberAddUserEnabled  # noqa: E501

        :param member_add_user_enabled: The member_add_user_enabled of this V1DLPStream.  # noqa: E501
        :type: bool
        """

        self._member_add_user_enabled = member_add_user_enabled

    @property
    def active(self):
        """Gets the active of this V1DLPStream.  # noqa: E501

        Is Room Active  # noqa: E501

        :return: The active of this V1DLPStream.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this V1DLPStream.

        Is Room Active  # noqa: E501

        :param active: The active of this V1DLPStream.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def discoverable(self):
        """Gets the discoverable of this V1DLPStream.  # noqa: E501

        Is Room discoverable  # noqa: E501

        :return: The discoverable of this V1DLPStream.  # noqa: E501
        :rtype: bool
        """
        return self._discoverable

    @discoverable.setter
    def discoverable(self, discoverable):
        """Sets the discoverable of this V1DLPStream.

        Is Room discoverable  # noqa: E501

        :param discoverable: The discoverable of this V1DLPStream.  # noqa: E501
        :type: bool
        """

        self._discoverable = discoverable

    @property
    def read_only(self):
        """Gets the read_only of this V1DLPStream.  # noqa: E501

        Is Room read-only  # noqa: E501

        :return: The read_only of this V1DLPStream.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this V1DLPStream.

        Is Room read-only  # noqa: E501

        :param read_only: The read_only of this V1DLPStream.  # noqa: E501
        :type: bool
        """

        self._read_only = read_only

    @property
    def copy_disabled(self):
        """Gets the copy_disabled of this V1DLPStream.  # noqa: E501

        Is Room copyDisabled  # noqa: E501

        :return: The copy_disabled of this V1DLPStream.  # noqa: E501
        :rtype: bool
        """
        return self._copy_disabled

    @copy_disabled.setter
    def copy_disabled(self, copy_disabled):
        """Sets the copy_disabled of this V1DLPStream.

        Is Room copyDisabled  # noqa: E501

        :param copy_disabled: The copy_disabled of this V1DLPStream.  # noqa: E501
        :type: bool
        """

        self._copy_disabled = copy_disabled

    @property
    def external_owned(self):
        """Gets the external_owned of this V1DLPStream.  # noqa: E501

        Is Room externalOwned  # noqa: E501

        :return: The external_owned of this V1DLPStream.  # noqa: E501
        :rtype: bool
        """
        return self._external_owned

    @external_owned.setter
    def external_owned(self, external_owned):
        """Sets the external_owned of this V1DLPStream.

        Is Room externalOwned  # noqa: E501

        :param external_owned: The external_owned of this V1DLPStream.  # noqa: E501
        :type: bool
        """

        self._external_owned = external_owned

    @property
    def send_message_disabled(self):
        """Gets the send_message_disabled of this V1DLPStream.  # noqa: E501

        Is sendMessage Disabled for this Room  # noqa: E501

        :return: The send_message_disabled of this V1DLPStream.  # noqa: E501
        :rtype: bool
        """
        return self._send_message_disabled

    @send_message_disabled.setter
    def send_message_disabled(self, send_message_disabled):
        """Sets the send_message_disabled of this V1DLPStream.

        Is sendMessage Disabled for this Room  # noqa: E501

        :param send_message_disabled: The send_message_disabled of this V1DLPStream.  # noqa: E501
        :type: bool
        """

        self._send_message_disabled = send_message_disabled

    @property
    def moderated(self):
        """Gets the moderated of this V1DLPStream.  # noqa: E501

        Is room moderated  # noqa: E501

        :return: The moderated of this V1DLPStream.  # noqa: E501
        :rtype: bool
        """
        return self._moderated

    @moderated.setter
    def moderated(self, moderated):
        """Sets the moderated of this V1DLPStream.

        Is room moderated  # noqa: E501

        :param moderated: The moderated of this V1DLPStream.  # noqa: E501
        :type: bool
        """

        self._moderated = moderated

    @property
    def share_history_enabled(self):
        """Gets the share_history_enabled of this V1DLPStream.  # noqa: E501

        Is room shareHistoryEnabled  # noqa: E501

        :return: The share_history_enabled of this V1DLPStream.  # noqa: E501
        :rtype: bool
        """
        return self._share_history_enabled

    @share_history_enabled.setter
    def share_history_enabled(self, share_history_enabled):
        """Sets the share_history_enabled of this V1DLPStream.

        Is room shareHistoryEnabled  # noqa: E501

        :param share_history_enabled: The share_history_enabled of this V1DLPStream.  # noqa: E501
        :type: bool
        """

        self._share_history_enabled = share_history_enabled

    @property
    def diagnostic(self):
        """Gets the diagnostic of this V1DLPStream.  # noqa: E501

        A diagnostic message containing an error message in the event that the stream retrieval failed. May also be present in the case of a successful call if there is useful narrative to return.   # noqa: E501

        :return: The diagnostic of this V1DLPStream.  # noqa: E501
        :rtype: str
        """
        return self._diagnostic

    @diagnostic.setter
    def diagnostic(self, diagnostic):
        """Sets the diagnostic of this V1DLPStream.

        A diagnostic message containing an error message in the event that the stream retrieval failed. May also be present in the case of a successful call if there is useful narrative to return.   # noqa: E501

        :param diagnostic: The diagnostic of this V1DLPStream.  # noqa: E501
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
        if not isinstance(other, V1DLPStream):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1DLPStream):
            return True

        return self.to_dict() != other.to_dict()
