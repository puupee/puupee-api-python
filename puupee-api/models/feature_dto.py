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


class FeatureDto(object):
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
        'display_name': 'str',
        'value': 'str',
        'provider': 'FeatureProviderDto',
        'description': 'str',
        'value_type': 'IStringValueType',
        'depth': 'int',
        'parent_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'display_name': 'displayName',
        'value': 'value',
        'provider': 'provider',
        'description': 'description',
        'value_type': 'valueType',
        'depth': 'depth',
        'parent_name': 'parentName'
    }

    def __init__(self, name=None, display_name=None, value=None, provider=None, description=None, value_type=None, depth=None, parent_name=None, local_vars_configuration=None):  # noqa: E501
        """FeatureDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._display_name = None
        self._value = None
        self._provider = None
        self._description = None
        self._value_type = None
        self._depth = None
        self._parent_name = None
        self.discriminator = None

        self.name = name
        self.display_name = display_name
        self.value = value
        if provider is not None:
            self.provider = provider
        self.description = description
        if value_type is not None:
            self.value_type = value_type
        if depth is not None:
            self.depth = depth
        self.parent_name = parent_name

    @property
    def name(self):
        """Gets the name of this FeatureDto.  # noqa: E501


        :return: The name of this FeatureDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FeatureDto.


        :param name: The name of this FeatureDto.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def display_name(self):
        """Gets the display_name of this FeatureDto.  # noqa: E501


        :return: The display_name of this FeatureDto.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this FeatureDto.


        :param display_name: The display_name of this FeatureDto.  # noqa: E501
        :type display_name: str
        """

        self._display_name = display_name

    @property
    def value(self):
        """Gets the value of this FeatureDto.  # noqa: E501


        :return: The value of this FeatureDto.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this FeatureDto.


        :param value: The value of this FeatureDto.  # noqa: E501
        :type value: str
        """

        self._value = value

    @property
    def provider(self):
        """Gets the provider of this FeatureDto.  # noqa: E501


        :return: The provider of this FeatureDto.  # noqa: E501
        :rtype: FeatureProviderDto
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this FeatureDto.


        :param provider: The provider of this FeatureDto.  # noqa: E501
        :type provider: FeatureProviderDto
        """

        self._provider = provider

    @property
    def description(self):
        """Gets the description of this FeatureDto.  # noqa: E501


        :return: The description of this FeatureDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FeatureDto.


        :param description: The description of this FeatureDto.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def value_type(self):
        """Gets the value_type of this FeatureDto.  # noqa: E501


        :return: The value_type of this FeatureDto.  # noqa: E501
        :rtype: IStringValueType
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """Sets the value_type of this FeatureDto.


        :param value_type: The value_type of this FeatureDto.  # noqa: E501
        :type value_type: IStringValueType
        """

        self._value_type = value_type

    @property
    def depth(self):
        """Gets the depth of this FeatureDto.  # noqa: E501


        :return: The depth of this FeatureDto.  # noqa: E501
        :rtype: int
        """
        return self._depth

    @depth.setter
    def depth(self, depth):
        """Sets the depth of this FeatureDto.


        :param depth: The depth of this FeatureDto.  # noqa: E501
        :type depth: int
        """

        self._depth = depth

    @property
    def parent_name(self):
        """Gets the parent_name of this FeatureDto.  # noqa: E501


        :return: The parent_name of this FeatureDto.  # noqa: E501
        :rtype: str
        """
        return self._parent_name

    @parent_name.setter
    def parent_name(self, parent_name):
        """Sets the parent_name of this FeatureDto.


        :param parent_name: The parent_name of this FeatureDto.  # noqa: E501
        :type parent_name: str
        """

        self._parent_name = parent_name

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
        if not isinstance(other, FeatureDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FeatureDto):
            return True

        return self.to_dict() != other.to_dict()
