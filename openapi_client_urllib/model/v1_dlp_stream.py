"""
    Agent API

    This document refers to Symphony API calls to send and receive messages and content. They need the on-premise Agent installed to perform decryption/encryption of content.  - sessionToken and keyManagerToken can be obtained by calling the authenticationAPI on the symphony back end and the key manager respectively. Refer to the methods described in authenticatorAPI.yaml. - Actions are defined to be atomic, ie will succeed in their entirety or fail and have changed nothing. - If it returns a 40X status then it will have sent no message to any stream even if a request to aome subset of the requested streams would have succeeded. - If this contract cannot be met for any reason then this is an error and the response code will be 50X. - MessageML is a markup language for messages. See reference here: https://rest-api.symphony.com/docs/messagemlv2 - **Real Time Events**: The following events are returned when reading from a real time messages and events stream (\"datafeed\"). These events will be returned for datafeeds created with the v5 endpoints. To know more about the endpoints, refer to Create Messages/Events Stream and Read Messages/Events Stream. Unless otherwise specified, all events were added in 1.46.   # noqa: E501

    The version of the OpenAPI document: 20.10.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

import nulltype  # noqa: F401

from openapi_client_urllib.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)


class V1DLPStream(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'name': (str,),  # noqa: E501
            'creator_pretty_name': (str,),  # noqa: E501
            'public_room': (bool,),  # noqa: E501
            'cross_pod': (bool,),  # noqa: E501
            'allow_external': (bool,),  # noqa: E501
            'creator_id': (str,),  # noqa: E501
            'room_description': (str,),  # noqa: E501
            'stream_id': (str,),  # noqa: E501
            'state': (str,),  # noqa: E501
            'type': (str,),  # noqa: E501
            'last_disabled': (int,),  # noqa: E501
            'member_add_user_enabled': (bool,),  # noqa: E501
            'active': (bool,),  # noqa: E501
            'discoverable': (bool,),  # noqa: E501
            'read_only': (bool,),  # noqa: E501
            'copy_disabled': (bool,),  # noqa: E501
            'external_owned': (bool,),  # noqa: E501
            'send_message_disabled': (bool,),  # noqa: E501
            'moderated': (bool,),  # noqa: E501
            'share_history_enabled': (bool,),  # noqa: E501
            'diagnostic': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'name': 'name',  # noqa: E501
        'creator_pretty_name': 'creatorPrettyName',  # noqa: E501
        'public_room': 'publicRoom',  # noqa: E501
        'cross_pod': 'crossPod',  # noqa: E501
        'allow_external': 'allowExternal',  # noqa: E501
        'creator_id': 'creatorId',  # noqa: E501
        'room_description': 'roomDescription',  # noqa: E501
        'stream_id': 'streamId',  # noqa: E501
        'state': 'state',  # noqa: E501
        'type': 'type',  # noqa: E501
        'last_disabled': 'lastDisabled',  # noqa: E501
        'member_add_user_enabled': 'memberAddUserEnabled',  # noqa: E501
        'active': 'active',  # noqa: E501
        'discoverable': 'discoverable',  # noqa: E501
        'read_only': 'readOnly',  # noqa: E501
        'copy_disabled': 'copyDisabled',  # noqa: E501
        'external_owned': 'externalOwned',  # noqa: E501
        'send_message_disabled': 'sendMessageDisabled',  # noqa: E501
        'moderated': 'moderated',  # noqa: E501
        'share_history_enabled': 'shareHistoryEnabled',  # noqa: E501
        'diagnostic': 'diagnostic',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """V1DLPStream - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            name (str): Name of the Stream/Room.. [optional]  # noqa: E501
            creator_pretty_name (str): Name of the creator of the Room.. [optional]  # noqa: E501
            public_room (bool): Is this a public room?. [optional]  # noqa: E501
            cross_pod (bool): Is this a cross pod scenario?. [optional]  # noqa: E501
            allow_external (bool): Is external messaging allowed. [optional]  # noqa: E501
            creator_id (str): Id of the creator of the Room.. [optional]  # noqa: E501
            room_description (str): Description of the Room.. [optional]  # noqa: E501
            stream_id (str): ThreadId of the Room.. [optional]  # noqa: E501
            state (str): State of the Room (example CREATED etc). [optional]  # noqa: E501
            type (str): Type of the Room (example ROOM (or IM or Wall)). [optional]  # noqa: E501
            last_disabled (int): Timestamp of last time the room is Disabled. [optional]  # noqa: E501
            member_add_user_enabled (bool): Is memberAddUserEnabled. [optional]  # noqa: E501
            active (bool): Is Room Active. [optional]  # noqa: E501
            discoverable (bool): Is Room discoverable. [optional]  # noqa: E501
            read_only (bool): Is Room read-only. [optional]  # noqa: E501
            copy_disabled (bool): Is Room copyDisabled. [optional]  # noqa: E501
            external_owned (bool): Is Room externalOwned. [optional]  # noqa: E501
            send_message_disabled (bool): Is sendMessage Disabled for this Room. [optional]  # noqa: E501
            moderated (bool): Is room moderated. [optional]  # noqa: E501
            share_history_enabled (bool): Is room shareHistoryEnabled. [optional]  # noqa: E501
            diagnostic (str): A diagnostic message containing an error message in the event that the stream retrieval failed. May also be present in the case of a successful call if there is useful narrative to return. . [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
