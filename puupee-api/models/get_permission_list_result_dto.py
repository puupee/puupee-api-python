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


class GetPermissionListResultDto(object):
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
        'entity_display_name': 'str',
        'groups': 'list[PermissionGroupDto]'
    }

    attribute_map = {
        'entity_display_name': 'entityDisplayName',
        'groups': 'groups'
    }

    def __init__(self, entity_display_name=None, groups=None, local_vars_configuration=None):  # noqa: E501
        """GetPermissionListResultDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._entity_display_name = None
        self._groups = None
        self.discriminator = None

        self.entity_display_name = entity_display_name
        self.groups = groups

    @property
    def entity_display_name(self):
        """Gets the entity_display_name of this GetPermissionListResultDto.  # noqa: E501


        :return: The entity_display_name of this GetPermissionListResultDto.  # noqa: E501
        :rtype: str
        """
        return self._entity_display_name

    @entity_display_name.setter
    def entity_display_name(self, entity_display_name):
        """Sets the entity_display_name of this GetPermissionListResultDto.


        :param entity_display_name: The entity_display_name of this GetPermissionListResultDto.  # noqa: E501
        :type entity_display_name: str
        """

        self._entity_display_name = entity_display_name

    @property
    def groups(self):
        """Gets the groups of this GetPermissionListResultDto.  # noqa: E501


        :return: The groups of this GetPermissionListResultDto.  # noqa: E501
        :rtype: list[PermissionGroupDto]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this GetPermissionListResultDto.


        :param groups: The groups of this GetPermissionListResultDto.  # noqa: E501
        :type groups: list[PermissionGroupDto]
        """

        self._groups = groups

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
        if not isinstance(other, GetPermissionListResultDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetPermissionListResultDto):
            return True

        return self.to_dict() != other.to_dict()
