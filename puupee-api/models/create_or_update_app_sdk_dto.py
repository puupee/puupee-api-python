# coding: utf-8

"""
    Puupee API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0.0
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from puupee-api.configuration import Configuration


class CreateOrUpdateAppSdkDto(object):
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
        'description': 'str',
        'privacy': 'str',
        'privacy_url': 'str',
        'home_page': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'privacy': 'privacy',
        'privacy_url': 'privacyUrl',
        'home_page': 'homePage'
    }

    def __init__(self, name=None, description=None, privacy=None, privacy_url=None, home_page=None, local_vars_configuration=None):  # noqa: E501
        """CreateOrUpdateAppSdkDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._description = None
        self._privacy = None
        self._privacy_url = None
        self._home_page = None
        self.discriminator = None

        self.name = name
        self.description = description
        self.privacy = privacy
        self.privacy_url = privacy_url
        self.home_page = home_page

    @property
    def name(self):
        """Gets the name of this CreateOrUpdateAppSdkDto.  # noqa: E501


        :return: The name of this CreateOrUpdateAppSdkDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateOrUpdateAppSdkDto.


        :param name: The name of this CreateOrUpdateAppSdkDto.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateOrUpdateAppSdkDto.  # noqa: E501


        :return: The description of this CreateOrUpdateAppSdkDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateOrUpdateAppSdkDto.


        :param description: The description of this CreateOrUpdateAppSdkDto.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def privacy(self):
        """Gets the privacy of this CreateOrUpdateAppSdkDto.  # noqa: E501


        :return: The privacy of this CreateOrUpdateAppSdkDto.  # noqa: E501
        :rtype: str
        """
        return self._privacy

    @privacy.setter
    def privacy(self, privacy):
        """Sets the privacy of this CreateOrUpdateAppSdkDto.


        :param privacy: The privacy of this CreateOrUpdateAppSdkDto.  # noqa: E501
        :type privacy: str
        """

        self._privacy = privacy

    @property
    def privacy_url(self):
        """Gets the privacy_url of this CreateOrUpdateAppSdkDto.  # noqa: E501


        :return: The privacy_url of this CreateOrUpdateAppSdkDto.  # noqa: E501
        :rtype: str
        """
        return self._privacy_url

    @privacy_url.setter
    def privacy_url(self, privacy_url):
        """Sets the privacy_url of this CreateOrUpdateAppSdkDto.


        :param privacy_url: The privacy_url of this CreateOrUpdateAppSdkDto.  # noqa: E501
        :type privacy_url: str
        """

        self._privacy_url = privacy_url

    @property
    def home_page(self):
        """Gets the home_page of this CreateOrUpdateAppSdkDto.  # noqa: E501


        :return: The home_page of this CreateOrUpdateAppSdkDto.  # noqa: E501
        :rtype: str
        """
        return self._home_page

    @home_page.setter
    def home_page(self, home_page):
        """Sets the home_page of this CreateOrUpdateAppSdkDto.


        :param home_page: The home_page of this CreateOrUpdateAppSdkDto.  # noqa: E501
        :type home_page: str
        """

        self._home_page = home_page

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateOrUpdateAppSdkDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateOrUpdateAppSdkDto):
            return True

        return self.to_dict() != other.to_dict()
