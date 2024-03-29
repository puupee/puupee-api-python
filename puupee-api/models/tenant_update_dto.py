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


class TenantUpdateDto(object):
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
        'extra_properties': 'dict[str, object]',
        'name': 'str',
        'concurrency_stamp': 'str'
    }

    attribute_map = {
        'extra_properties': 'extraProperties',
        'name': 'name',
        'concurrency_stamp': 'concurrencyStamp'
    }

    def __init__(self, extra_properties=None, name=None, concurrency_stamp=None, local_vars_configuration=None):  # noqa: E501
        """TenantUpdateDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._extra_properties = None
        self._name = None
        self._concurrency_stamp = None
        self.discriminator = None

        self.extra_properties = extra_properties
        self.name = name
        self.concurrency_stamp = concurrency_stamp

    @property
    def extra_properties(self):
        """Gets the extra_properties of this TenantUpdateDto.  # noqa: E501


        :return: The extra_properties of this TenantUpdateDto.  # noqa: E501
        :rtype: dict[str, object]
        """
        return self._extra_properties

    @extra_properties.setter
    def extra_properties(self, extra_properties):
        """Sets the extra_properties of this TenantUpdateDto.


        :param extra_properties: The extra_properties of this TenantUpdateDto.  # noqa: E501
        :type extra_properties: dict[str, object]
        """

        self._extra_properties = extra_properties

    @property
    def name(self):
        """Gets the name of this TenantUpdateDto.  # noqa: E501


        :return: The name of this TenantUpdateDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TenantUpdateDto.


        :param name: The name of this TenantUpdateDto.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 64):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 0):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501

        self._name = name

    @property
    def concurrency_stamp(self):
        """Gets the concurrency_stamp of this TenantUpdateDto.  # noqa: E501


        :return: The concurrency_stamp of this TenantUpdateDto.  # noqa: E501
        :rtype: str
        """
        return self._concurrency_stamp

    @concurrency_stamp.setter
    def concurrency_stamp(self, concurrency_stamp):
        """Sets the concurrency_stamp of this TenantUpdateDto.


        :param concurrency_stamp: The concurrency_stamp of this TenantUpdateDto.  # noqa: E501
        :type concurrency_stamp: str
        """

        self._concurrency_stamp = concurrency_stamp

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
        if not isinstance(other, TenantUpdateDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TenantUpdateDto):
            return True

        return self.to_dict() != other.to_dict()
