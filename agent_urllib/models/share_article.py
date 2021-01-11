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


class ShareArticle(object):
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
        'article_id': 'str',
        'title': 'str',
        'sub_title': 'str',
        'message': 'str',
        'publisher': 'str',
        'publish_date': 'int',
        'thumbnail_url': 'str',
        'author': 'str',
        'article_url': 'str',
        'summary': 'str',
        'app_id': 'str',
        'app_name': 'str',
        'app_icon_url': 'str'
    }

    attribute_map = {
        'article_id': 'articleId',
        'title': 'title',
        'sub_title': 'subTitle',
        'message': 'message',
        'publisher': 'publisher',
        'publish_date': 'publishDate',
        'thumbnail_url': 'thumbnailUrl',
        'author': 'author',
        'article_url': 'articleUrl',
        'summary': 'summary',
        'app_id': 'appId',
        'app_name': 'appName',
        'app_icon_url': 'appIconUrl'
    }

    def __init__(self, article_id=None, title=None, sub_title=None, message=None, publisher=None, publish_date=None, thumbnail_url=None, author=None, article_url=None, summary=None, app_id=None, app_name=None, app_icon_url=None, local_vars_configuration=None):  # noqa: E501
        """ShareArticle - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._article_id = None
        self._title = None
        self._sub_title = None
        self._message = None
        self._publisher = None
        self._publish_date = None
        self._thumbnail_url = None
        self._author = None
        self._article_url = None
        self._summary = None
        self._app_id = None
        self._app_name = None
        self._app_icon_url = None
        self.discriminator = None

        if article_id is not None:
            self.article_id = article_id
        self.title = title
        if sub_title is not None:
            self.sub_title = sub_title
        if message is not None:
            self.message = message
        self.publisher = publisher
        if publish_date is not None:
            self.publish_date = publish_date
        if thumbnail_url is not None:
            self.thumbnail_url = thumbnail_url
        self.author = author
        if article_url is not None:
            self.article_url = article_url
        if summary is not None:
            self.summary = summary
        self.app_id = app_id
        if app_name is not None:
            self.app_name = app_name
        if app_icon_url is not None:
            self.app_icon_url = app_icon_url

    @property
    def article_id(self):
        """Gets the article_id of this ShareArticle.  # noqa: E501

        An ID for this article that should be unique to the calling application. Either an articleId or an articleUrl is required.  # noqa: E501

        :return: The article_id of this ShareArticle.  # noqa: E501
        :rtype: str
        """
        return self._article_id

    @article_id.setter
    def article_id(self, article_id):
        """Sets the article_id of this ShareArticle.

        An ID for this article that should be unique to the calling application. Either an articleId or an articleUrl is required.  # noqa: E501

        :param article_id: The article_id of this ShareArticle.  # noqa: E501
        :type: str
        """

        self._article_id = article_id

    @property
    def title(self):
        """Gets the title of this ShareArticle.  # noqa: E501

        The title of the article  # noqa: E501

        :return: The title of this ShareArticle.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ShareArticle.

        The title of the article  # noqa: E501

        :param title: The title of this ShareArticle.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and title is None:  # noqa: E501
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def sub_title(self):
        """Gets the sub_title of this ShareArticle.  # noqa: E501

        The subtitle of the article  # noqa: E501

        :return: The sub_title of this ShareArticle.  # noqa: E501
        :rtype: str
        """
        return self._sub_title

    @sub_title.setter
    def sub_title(self, sub_title):
        """Sets the sub_title of this ShareArticle.

        The subtitle of the article  # noqa: E501

        :param sub_title: The sub_title of this ShareArticle.  # noqa: E501
        :type: str
        """

        self._sub_title = sub_title

    @property
    def message(self):
        """Gets the message of this ShareArticle.  # noqa: E501

        The message text that can be send along with the shared article  # noqa: E501

        :return: The message of this ShareArticle.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ShareArticle.

        The message text that can be send along with the shared article  # noqa: E501

        :param message: The message of this ShareArticle.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def publisher(self):
        """Gets the publisher of this ShareArticle.  # noqa: E501

        Publisher of the article  # noqa: E501

        :return: The publisher of this ShareArticle.  # noqa: E501
        :rtype: str
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        """Sets the publisher of this ShareArticle.

        Publisher of the article  # noqa: E501

        :param publisher: The publisher of this ShareArticle.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and publisher is None:  # noqa: E501
            raise ValueError("Invalid value for `publisher`, must not be `None`")  # noqa: E501

        self._publisher = publisher

    @property
    def publish_date(self):
        """Gets the publish_date of this ShareArticle.  # noqa: E501

        Article publish date in unix timestamp  # noqa: E501

        :return: The publish_date of this ShareArticle.  # noqa: E501
        :rtype: int
        """
        return self._publish_date

    @publish_date.setter
    def publish_date(self, publish_date):
        """Sets the publish_date of this ShareArticle.

        Article publish date in unix timestamp  # noqa: E501

        :param publish_date: The publish_date of this ShareArticle.  # noqa: E501
        :type: int
        """

        self._publish_date = publish_date

    @property
    def thumbnail_url(self):
        """Gets the thumbnail_url of this ShareArticle.  # noqa: E501

        Url to the thumbnail image  # noqa: E501

        :return: The thumbnail_url of this ShareArticle.  # noqa: E501
        :rtype: str
        """
        return self._thumbnail_url

    @thumbnail_url.setter
    def thumbnail_url(self, thumbnail_url):
        """Sets the thumbnail_url of this ShareArticle.

        Url to the thumbnail image  # noqa: E501

        :param thumbnail_url: The thumbnail_url of this ShareArticle.  # noqa: E501
        :type: str
        """

        self._thumbnail_url = thumbnail_url

    @property
    def author(self):
        """Gets the author of this ShareArticle.  # noqa: E501

        Author of the article  # noqa: E501

        :return: The author of this ShareArticle.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this ShareArticle.

        Author of the article  # noqa: E501

        :param author: The author of this ShareArticle.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and author is None:  # noqa: E501
            raise ValueError("Invalid value for `author`, must not be `None`")  # noqa: E501

        self._author = author

    @property
    def article_url(self):
        """Gets the article_url of this ShareArticle.  # noqa: E501

        Url to the article  # noqa: E501

        :return: The article_url of this ShareArticle.  # noqa: E501
        :rtype: str
        """
        return self._article_url

    @article_url.setter
    def article_url(self, article_url):
        """Sets the article_url of this ShareArticle.

        Url to the article  # noqa: E501

        :param article_url: The article_url of this ShareArticle.  # noqa: E501
        :type: str
        """

        self._article_url = article_url

    @property
    def summary(self):
        """Gets the summary of this ShareArticle.  # noqa: E501

        Preview summary of the article  # noqa: E501

        :return: The summary of this ShareArticle.  # noqa: E501
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this ShareArticle.

        Preview summary of the article  # noqa: E501

        :param summary: The summary of this ShareArticle.  # noqa: E501
        :type: str
        """

        self._summary = summary

    @property
    def app_id(self):
        """Gets the app_id of this ShareArticle.  # noqa: E501

        App ID of the calling application  # noqa: E501

        :return: The app_id of this ShareArticle.  # noqa: E501
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ShareArticle.

        App ID of the calling application  # noqa: E501

        :param app_id: The app_id of this ShareArticle.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and app_id is None:  # noqa: E501
            raise ValueError("Invalid value for `app_id`, must not be `None`")  # noqa: E501

        self._app_id = app_id

    @property
    def app_name(self):
        """Gets the app_name of this ShareArticle.  # noqa: E501

        App name of the calling application  # noqa: E501

        :return: The app_name of this ShareArticle.  # noqa: E501
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this ShareArticle.

        App name of the calling application  # noqa: E501

        :param app_name: The app_name of this ShareArticle.  # noqa: E501
        :type: str
        """

        self._app_name = app_name

    @property
    def app_icon_url(self):
        """Gets the app_icon_url of this ShareArticle.  # noqa: E501

        App icon url of the calling application  # noqa: E501

        :return: The app_icon_url of this ShareArticle.  # noqa: E501
        :rtype: str
        """
        return self._app_icon_url

    @app_icon_url.setter
    def app_icon_url(self, app_icon_url):
        """Sets the app_icon_url of this ShareArticle.

        App icon url of the calling application  # noqa: E501

        :param app_icon_url: The app_icon_url of this ShareArticle.  # noqa: E501
        :type: str
        """

        self._app_icon_url = app_icon_url

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
        if not isinstance(other, ShareArticle):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ShareArticle):
            return True

        return self.to_dict() != other.to_dict()
