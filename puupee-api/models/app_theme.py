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


class AppTheme(object):
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
        'source_color': 'str',
        'theme_mode': 'AppThemeMode'
    }

    attribute_map = {
        'source_color': 'sourceColor',
        'theme_mode': 'themeMode'
    }

    def __init__(self, source_color=None, theme_mode=None, local_vars_configuration=None):  # noqa: E501
        """AppTheme - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._source_color = None
        self._theme_mode = None
        self.discriminator = None

        self.source_color = source_color
        if theme_mode is not None:
            self.theme_mode = theme_mode

    @property
    def source_color(self):
        """Gets the source_color of this AppTheme.  # noqa: E501


        :return: The source_color of this AppTheme.  # noqa: E501
        :rtype: str
        """
        return self._source_color

    @source_color.setter
    def source_color(self, source_color):
        """Sets the source_color of this AppTheme.


        :param source_color: The source_color of this AppTheme.  # noqa: E501
        :type source_color: str
        """

        self._source_color = source_color

    @property
    def theme_mode(self):
        """Gets the theme_mode of this AppTheme.  # noqa: E501


        :return: The theme_mode of this AppTheme.  # noqa: E501
        :rtype: AppThemeMode
        """
        return self._theme_mode

    @theme_mode.setter
    def theme_mode(self, theme_mode):
        """Sets the theme_mode of this AppTheme.


        :param theme_mode: The theme_mode of this AppTheme.  # noqa: E501
        :type theme_mode: AppThemeMode
        """

        self._theme_mode = theme_mode

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
        if not isinstance(other, AppTheme):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AppTheme):
            return True

        return self.to_dict() != other.to_dict()
