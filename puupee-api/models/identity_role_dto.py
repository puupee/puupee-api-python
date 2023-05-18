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


class IdentityRoleDto(object):
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
        'id': 'str',
        'name': 'str',
        'is_default': 'bool',
        'is_static': 'bool',
        'is_public': 'bool',
        'concurrency_stamp': 'str'
    }

    attribute_map = {
        'extra_properties': 'extraProperties',
        'id': 'id',
        'name': 'name',
        'is_default': 'isDefault',
        'is_static': 'isStatic',
        'is_public': 'isPublic',
        'concurrency_stamp': 'concurrencyStamp'
    }

    def __init__(self, extra_properties=None, id=None, name=None, is_default=None, is_static=None, is_public=None, concurrency_stamp=None, local_vars_configuration=None):  # noqa: E501
        """IdentityRoleDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._extra_properties = None
        self._id = None
        self._name = None
        self._is_default = None
        self._is_static = None
        self._is_public = None
        self._concurrency_stamp = None
        self.discriminator = None

        self.extra_properties = extra_properties
        if id is not None:
            self.id = id
        self.name = name
        if is_default is not None:
            self.is_default = is_default
        if is_static is not None:
            self.is_static = is_static
        if is_public is not None:
            self.is_public = is_public
        self.concurrency_stamp = concurrency_stamp

    @property
    def extra_properties(self):
        """Gets the extra_properties of this IdentityRoleDto.  # noqa: E501


        :return: The extra_properties of this IdentityRoleDto.  # noqa: E501
        :rtype: dict[str, object]
        """
        return self._extra_properties

    @extra_properties.setter
    def extra_properties(self, extra_properties):
        """Sets the extra_properties of this IdentityRoleDto.


        :param extra_properties: The extra_properties of this IdentityRoleDto.  # noqa: E501
        :type extra_properties: dict[str, object]
        """

        self._extra_properties = extra_properties

    @property
    def id(self):
        """Gets the id of this IdentityRoleDto.  # noqa: E501


        :return: The id of this IdentityRoleDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IdentityRoleDto.


        :param id: The id of this IdentityRoleDto.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this IdentityRoleDto.  # noqa: E501


        :return: The name of this IdentityRoleDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IdentityRoleDto.


        :param name: The name of this IdentityRoleDto.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def is_default(self):
        """Gets the is_default of this IdentityRoleDto.  # noqa: E501


        :return: The is_default of this IdentityRoleDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this IdentityRoleDto.


        :param is_default: The is_default of this IdentityRoleDto.  # noqa: E501
        :type is_default: bool
        """

        self._is_default = is_default

    @property
    def is_static(self):
        """Gets the is_static of this IdentityRoleDto.  # noqa: E501


        :return: The is_static of this IdentityRoleDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_static

    @is_static.setter
    def is_static(self, is_static):
        """Sets the is_static of this IdentityRoleDto.


        :param is_static: The is_static of this IdentityRoleDto.  # noqa: E501
        :type is_static: bool
        """

        self._is_static = is_static

    @property
    def is_public(self):
        """Gets the is_public of this IdentityRoleDto.  # noqa: E501


        :return: The is_public of this IdentityRoleDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """Sets the is_public of this IdentityRoleDto.


        :param is_public: The is_public of this IdentityRoleDto.  # noqa: E501
        :type is_public: bool
        """

        self._is_public = is_public

    @property
    def concurrency_stamp(self):
        """Gets the concurrency_stamp of this IdentityRoleDto.  # noqa: E501


        :return: The concurrency_stamp of this IdentityRoleDto.  # noqa: E501
        :rtype: str
        """
        return self._concurrency_stamp

    @concurrency_stamp.setter
    def concurrency_stamp(self, concurrency_stamp):
        """Sets the concurrency_stamp of this IdentityRoleDto.


        :param concurrency_stamp: The concurrency_stamp of this IdentityRoleDto.  # noqa: E501
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
        if not isinstance(other, IdentityRoleDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IdentityRoleDto):
            return True

        return self.to_dict() != other.to_dict()
