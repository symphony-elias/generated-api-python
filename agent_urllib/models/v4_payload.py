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


class V4Payload(object):
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
        'message_sent': 'V4MessageSent',
        'shared_post': 'V4SharedPost',
        'instant_message_created': 'V4InstantMessageCreated',
        'room_created': 'V4RoomCreated',
        'room_updated': 'V4RoomUpdated',
        'room_deactivated': 'V4RoomDeactivated',
        'room_reactivated': 'V4RoomReactivated',
        'user_joined_room': 'V4UserJoinedRoom',
        'user_left_room': 'V4UserLeftRoom',
        'room_member_promoted_to_owner': 'V4RoomMemberPromotedToOwner',
        'room_member_demoted_from_owner': 'V4RoomMemberDemotedFromOwner',
        'connection_requested': 'V4ConnectionRequested',
        'connection_accepted': 'V4ConnectionAccepted',
        'message_suppressed': 'V4MessageSuppressed',
        'symphony_elements_action': 'V4SymphonyElementsAction',
        'user_requested_to_join_room': 'V4UserRequestedToJoinRoom'
    }

    attribute_map = {
        'message_sent': 'messageSent',
        'shared_post': 'sharedPost',
        'instant_message_created': 'instantMessageCreated',
        'room_created': 'roomCreated',
        'room_updated': 'roomUpdated',
        'room_deactivated': 'roomDeactivated',
        'room_reactivated': 'roomReactivated',
        'user_joined_room': 'userJoinedRoom',
        'user_left_room': 'userLeftRoom',
        'room_member_promoted_to_owner': 'roomMemberPromotedToOwner',
        'room_member_demoted_from_owner': 'roomMemberDemotedFromOwner',
        'connection_requested': 'connectionRequested',
        'connection_accepted': 'connectionAccepted',
        'message_suppressed': 'messageSuppressed',
        'symphony_elements_action': 'symphonyElementsAction',
        'user_requested_to_join_room': 'userRequestedToJoinRoom'
    }

    def __init__(self, message_sent=None, shared_post=None, instant_message_created=None, room_created=None, room_updated=None, room_deactivated=None, room_reactivated=None, user_joined_room=None, user_left_room=None, room_member_promoted_to_owner=None, room_member_demoted_from_owner=None, connection_requested=None, connection_accepted=None, message_suppressed=None, symphony_elements_action=None, user_requested_to_join_room=None, local_vars_configuration=None):  # noqa: E501
        """V4Payload - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._message_sent = None
        self._shared_post = None
        self._instant_message_created = None
        self._room_created = None
        self._room_updated = None
        self._room_deactivated = None
        self._room_reactivated = None
        self._user_joined_room = None
        self._user_left_room = None
        self._room_member_promoted_to_owner = None
        self._room_member_demoted_from_owner = None
        self._connection_requested = None
        self._connection_accepted = None
        self._message_suppressed = None
        self._symphony_elements_action = None
        self._user_requested_to_join_room = None
        self.discriminator = None

        if message_sent is not None:
            self.message_sent = message_sent
        if shared_post is not None:
            self.shared_post = shared_post
        if instant_message_created is not None:
            self.instant_message_created = instant_message_created
        if room_created is not None:
            self.room_created = room_created
        if room_updated is not None:
            self.room_updated = room_updated
        if room_deactivated is not None:
            self.room_deactivated = room_deactivated
        if room_reactivated is not None:
            self.room_reactivated = room_reactivated
        if user_joined_room is not None:
            self.user_joined_room = user_joined_room
        if user_left_room is not None:
            self.user_left_room = user_left_room
        if room_member_promoted_to_owner is not None:
            self.room_member_promoted_to_owner = room_member_promoted_to_owner
        if room_member_demoted_from_owner is not None:
            self.room_member_demoted_from_owner = room_member_demoted_from_owner
        if connection_requested is not None:
            self.connection_requested = connection_requested
        if connection_accepted is not None:
            self.connection_accepted = connection_accepted
        if message_suppressed is not None:
            self.message_suppressed = message_suppressed
        if symphony_elements_action is not None:
            self.symphony_elements_action = symphony_elements_action
        if user_requested_to_join_room is not None:
            self.user_requested_to_join_room = user_requested_to_join_room

    @property
    def message_sent(self):
        """Gets the message_sent of this V4Payload.  # noqa: E501


        :return: The message_sent of this V4Payload.  # noqa: E501
        :rtype: V4MessageSent
        """
        return self._message_sent

    @message_sent.setter
    def message_sent(self, message_sent):
        """Sets the message_sent of this V4Payload.


        :param message_sent: The message_sent of this V4Payload.  # noqa: E501
        :type: V4MessageSent
        """

        self._message_sent = message_sent

    @property
    def shared_post(self):
        """Gets the shared_post of this V4Payload.  # noqa: E501


        :return: The shared_post of this V4Payload.  # noqa: E501
        :rtype: V4SharedPost
        """
        return self._shared_post

    @shared_post.setter
    def shared_post(self, shared_post):
        """Sets the shared_post of this V4Payload.


        :param shared_post: The shared_post of this V4Payload.  # noqa: E501
        :type: V4SharedPost
        """

        self._shared_post = shared_post

    @property
    def instant_message_created(self):
        """Gets the instant_message_created of this V4Payload.  # noqa: E501


        :return: The instant_message_created of this V4Payload.  # noqa: E501
        :rtype: V4InstantMessageCreated
        """
        return self._instant_message_created

    @instant_message_created.setter
    def instant_message_created(self, instant_message_created):
        """Sets the instant_message_created of this V4Payload.


        :param instant_message_created: The instant_message_created of this V4Payload.  # noqa: E501
        :type: V4InstantMessageCreated
        """

        self._instant_message_created = instant_message_created

    @property
    def room_created(self):
        """Gets the room_created of this V4Payload.  # noqa: E501


        :return: The room_created of this V4Payload.  # noqa: E501
        :rtype: V4RoomCreated
        """
        return self._room_created

    @room_created.setter
    def room_created(self, room_created):
        """Sets the room_created of this V4Payload.


        :param room_created: The room_created of this V4Payload.  # noqa: E501
        :type: V4RoomCreated
        """

        self._room_created = room_created

    @property
    def room_updated(self):
        """Gets the room_updated of this V4Payload.  # noqa: E501


        :return: The room_updated of this V4Payload.  # noqa: E501
        :rtype: V4RoomUpdated
        """
        return self._room_updated

    @room_updated.setter
    def room_updated(self, room_updated):
        """Sets the room_updated of this V4Payload.


        :param room_updated: The room_updated of this V4Payload.  # noqa: E501
        :type: V4RoomUpdated
        """

        self._room_updated = room_updated

    @property
    def room_deactivated(self):
        """Gets the room_deactivated of this V4Payload.  # noqa: E501


        :return: The room_deactivated of this V4Payload.  # noqa: E501
        :rtype: V4RoomDeactivated
        """
        return self._room_deactivated

    @room_deactivated.setter
    def room_deactivated(self, room_deactivated):
        """Sets the room_deactivated of this V4Payload.


        :param room_deactivated: The room_deactivated of this V4Payload.  # noqa: E501
        :type: V4RoomDeactivated
        """

        self._room_deactivated = room_deactivated

    @property
    def room_reactivated(self):
        """Gets the room_reactivated of this V4Payload.  # noqa: E501


        :return: The room_reactivated of this V4Payload.  # noqa: E501
        :rtype: V4RoomReactivated
        """
        return self._room_reactivated

    @room_reactivated.setter
    def room_reactivated(self, room_reactivated):
        """Sets the room_reactivated of this V4Payload.


        :param room_reactivated: The room_reactivated of this V4Payload.  # noqa: E501
        :type: V4RoomReactivated
        """

        self._room_reactivated = room_reactivated

    @property
    def user_joined_room(self):
        """Gets the user_joined_room of this V4Payload.  # noqa: E501


        :return: The user_joined_room of this V4Payload.  # noqa: E501
        :rtype: V4UserJoinedRoom
        """
        return self._user_joined_room

    @user_joined_room.setter
    def user_joined_room(self, user_joined_room):
        """Sets the user_joined_room of this V4Payload.


        :param user_joined_room: The user_joined_room of this V4Payload.  # noqa: E501
        :type: V4UserJoinedRoom
        """

        self._user_joined_room = user_joined_room

    @property
    def user_left_room(self):
        """Gets the user_left_room of this V4Payload.  # noqa: E501


        :return: The user_left_room of this V4Payload.  # noqa: E501
        :rtype: V4UserLeftRoom
        """
        return self._user_left_room

    @user_left_room.setter
    def user_left_room(self, user_left_room):
        """Sets the user_left_room of this V4Payload.


        :param user_left_room: The user_left_room of this V4Payload.  # noqa: E501
        :type: V4UserLeftRoom
        """

        self._user_left_room = user_left_room

    @property
    def room_member_promoted_to_owner(self):
        """Gets the room_member_promoted_to_owner of this V4Payload.  # noqa: E501


        :return: The room_member_promoted_to_owner of this V4Payload.  # noqa: E501
        :rtype: V4RoomMemberPromotedToOwner
        """
        return self._room_member_promoted_to_owner

    @room_member_promoted_to_owner.setter
    def room_member_promoted_to_owner(self, room_member_promoted_to_owner):
        """Sets the room_member_promoted_to_owner of this V4Payload.


        :param room_member_promoted_to_owner: The room_member_promoted_to_owner of this V4Payload.  # noqa: E501
        :type: V4RoomMemberPromotedToOwner
        """

        self._room_member_promoted_to_owner = room_member_promoted_to_owner

    @property
    def room_member_demoted_from_owner(self):
        """Gets the room_member_demoted_from_owner of this V4Payload.  # noqa: E501


        :return: The room_member_demoted_from_owner of this V4Payload.  # noqa: E501
        :rtype: V4RoomMemberDemotedFromOwner
        """
        return self._room_member_demoted_from_owner

    @room_member_demoted_from_owner.setter
    def room_member_demoted_from_owner(self, room_member_demoted_from_owner):
        """Sets the room_member_demoted_from_owner of this V4Payload.


        :param room_member_demoted_from_owner: The room_member_demoted_from_owner of this V4Payload.  # noqa: E501
        :type: V4RoomMemberDemotedFromOwner
        """

        self._room_member_demoted_from_owner = room_member_demoted_from_owner

    @property
    def connection_requested(self):
        """Gets the connection_requested of this V4Payload.  # noqa: E501


        :return: The connection_requested of this V4Payload.  # noqa: E501
        :rtype: V4ConnectionRequested
        """
        return self._connection_requested

    @connection_requested.setter
    def connection_requested(self, connection_requested):
        """Sets the connection_requested of this V4Payload.


        :param connection_requested: The connection_requested of this V4Payload.  # noqa: E501
        :type: V4ConnectionRequested
        """

        self._connection_requested = connection_requested

    @property
    def connection_accepted(self):
        """Gets the connection_accepted of this V4Payload.  # noqa: E501


        :return: The connection_accepted of this V4Payload.  # noqa: E501
        :rtype: V4ConnectionAccepted
        """
        return self._connection_accepted

    @connection_accepted.setter
    def connection_accepted(self, connection_accepted):
        """Sets the connection_accepted of this V4Payload.


        :param connection_accepted: The connection_accepted of this V4Payload.  # noqa: E501
        :type: V4ConnectionAccepted
        """

        self._connection_accepted = connection_accepted

    @property
    def message_suppressed(self):
        """Gets the message_suppressed of this V4Payload.  # noqa: E501


        :return: The message_suppressed of this V4Payload.  # noqa: E501
        :rtype: V4MessageSuppressed
        """
        return self._message_suppressed

    @message_suppressed.setter
    def message_suppressed(self, message_suppressed):
        """Sets the message_suppressed of this V4Payload.


        :param message_suppressed: The message_suppressed of this V4Payload.  # noqa: E501
        :type: V4MessageSuppressed
        """

        self._message_suppressed = message_suppressed

    @property
    def symphony_elements_action(self):
        """Gets the symphony_elements_action of this V4Payload.  # noqa: E501


        :return: The symphony_elements_action of this V4Payload.  # noqa: E501
        :rtype: V4SymphonyElementsAction
        """
        return self._symphony_elements_action

    @symphony_elements_action.setter
    def symphony_elements_action(self, symphony_elements_action):
        """Sets the symphony_elements_action of this V4Payload.


        :param symphony_elements_action: The symphony_elements_action of this V4Payload.  # noqa: E501
        :type: V4SymphonyElementsAction
        """

        self._symphony_elements_action = symphony_elements_action

    @property
    def user_requested_to_join_room(self):
        """Gets the user_requested_to_join_room of this V4Payload.  # noqa: E501


        :return: The user_requested_to_join_room of this V4Payload.  # noqa: E501
        :rtype: V4UserRequestedToJoinRoom
        """
        return self._user_requested_to_join_room

    @user_requested_to_join_room.setter
    def user_requested_to_join_room(self, user_requested_to_join_room):
        """Sets the user_requested_to_join_room of this V4Payload.


        :param user_requested_to_join_room: The user_requested_to_join_room of this V4Payload.  # noqa: E501
        :type: V4UserRequestedToJoinRoom
        """

        self._user_requested_to_join_room = user_requested_to_join_room

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
        if not isinstance(other, V4Payload):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V4Payload):
            return True

        return self.to_dict() != other.to_dict()
