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


class TypeApiDescriptionModel(object):
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
        'base_type': 'str',
        'is_enum': 'bool',
        'enum_names': 'list[str]',
        'enum_values': 'list[object]',
        'generic_arguments': 'list[str]',
        'properties': 'list[PropertyApiDescriptionModel]'
    }

    attribute_map = {
        'base_type': 'baseType',
        'is_enum': 'isEnum',
        'enum_names': 'enumNames',
        'enum_values': 'enumValues',
        'generic_arguments': 'genericArguments',
        'properties': 'properties'
    }

    def __init__(self, base_type=None, is_enum=None, enum_names=None, enum_values=None, generic_arguments=None, properties=None, local_vars_configuration=None):  # noqa: E501
        """TypeApiDescriptionModel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._base_type = None
        self._is_enum = None
        self._enum_names = None
        self._enum_values = None
        self._generic_arguments = None
        self._properties = None
        self.discriminator = None

        self.base_type = base_type
        if is_enum is not None:
            self.is_enum = is_enum
        self.enum_names = enum_names
        self.enum_values = enum_values
        self.generic_arguments = generic_arguments
        self.properties = properties

    @property
    def base_type(self):
        """Gets the base_type of this TypeApiDescriptionModel.  # noqa: E501


        :return: The base_type of this TypeApiDescriptionModel.  # noqa: E501
        :rtype: str
        """
        return self._base_type

    @base_type.setter
    def base_type(self, base_type):
        """Sets the base_type of this TypeApiDescriptionModel.


        :param base_type: The base_type of this TypeApiDescriptionModel.  # noqa: E501
        :type base_type: str
        """

        self._base_type = base_type

    @property
    def is_enum(self):
        """Gets the is_enum of this TypeApiDescriptionModel.  # noqa: E501


        :return: The is_enum of this TypeApiDescriptionModel.  # noqa: E501
        :rtype: bool
        """
        return self._is_enum

    @is_enum.setter
    def is_enum(self, is_enum):
        """Sets the is_enum of this TypeApiDescriptionModel.


        :param is_enum: The is_enum of this TypeApiDescriptionModel.  # noqa: E501
        :type is_enum: bool
        """

        self._is_enum = is_enum

    @property
    def enum_names(self):
        """Gets the enum_names of this TypeApiDescriptionModel.  # noqa: E501


        :return: The enum_names of this TypeApiDescriptionModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._enum_names

    @enum_names.setter
    def enum_names(self, enum_names):
        """Sets the enum_names of this TypeApiDescriptionModel.


        :param enum_names: The enum_names of this TypeApiDescriptionModel.  # noqa: E501
        :type enum_names: list[str]
        """

        self._enum_names = enum_names

    @property
    def enum_values(self):
        """Gets the enum_values of this TypeApiDescriptionModel.  # noqa: E501


        :return: The enum_values of this TypeApiDescriptionModel.  # noqa: E501
        :rtype: list[object]
        """
        return self._enum_values

    @enum_values.setter
    def enum_values(self, enum_values):
        """Sets the enum_values of this TypeApiDescriptionModel.


        :param enum_values: The enum_values of this TypeApiDescriptionModel.  # noqa: E501
        :type enum_values: list[object]
        """

        self._enum_values = enum_values

    @property
    def generic_arguments(self):
        """Gets the generic_arguments of this TypeApiDescriptionModel.  # noqa: E501


        :return: The generic_arguments of this TypeApiDescriptionModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._generic_arguments

    @generic_arguments.setter
    def generic_arguments(self, generic_arguments):
        """Sets the generic_arguments of this TypeApiDescriptionModel.


        :param generic_arguments: The generic_arguments of this TypeApiDescriptionModel.  # noqa: E501
        :type generic_arguments: list[str]
        """

        self._generic_arguments = generic_arguments

    @property
    def properties(self):
        """Gets the properties of this TypeApiDescriptionModel.  # noqa: E501


        :return: The properties of this TypeApiDescriptionModel.  # noqa: E501
        :rtype: list[PropertyApiDescriptionModel]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this TypeApiDescriptionModel.


        :param properties: The properties of this TypeApiDescriptionModel.  # noqa: E501
        :type properties: list[PropertyApiDescriptionModel]
        """

        self._properties = properties

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
        if not isinstance(other, TypeApiDescriptionModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TypeApiDescriptionModel):
            return True

        return self.to_dict() != other.to_dict()
