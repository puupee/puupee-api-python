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


class ModuleExtensionDto(object):
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
        'entities': 'dict[str, EntityExtensionDto]',
        'configuration': 'dict[str, object]'
    }

    attribute_map = {
        'entities': 'entities',
        'configuration': 'configuration'
    }

    def __init__(self, entities=None, configuration=None, local_vars_configuration=None):  # noqa: E501
        """ModuleExtensionDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._entities = None
        self._configuration = None
        self.discriminator = None

        self.entities = entities
        self.configuration = configuration

    @property
    def entities(self):
        """Gets the entities of this ModuleExtensionDto.  # noqa: E501


        :return: The entities of this ModuleExtensionDto.  # noqa: E501
        :rtype: dict[str, EntityExtensionDto]
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """Sets the entities of this ModuleExtensionDto.


        :param entities: The entities of this ModuleExtensionDto.  # noqa: E501
        :type entities: dict[str, EntityExtensionDto]
        """

        self._entities = entities

    @property
    def configuration(self):
        """Gets the configuration of this ModuleExtensionDto.  # noqa: E501


        :return: The configuration of this ModuleExtensionDto.  # noqa: E501
        :rtype: dict[str, object]
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this ModuleExtensionDto.


        :param configuration: The configuration of this ModuleExtensionDto.  # noqa: E501
        :type configuration: dict[str, object]
        """

        self._configuration = configuration

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
        if not isinstance(other, ModuleExtensionDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModuleExtensionDto):
            return True

        return self.to_dict() != other.to_dict()
