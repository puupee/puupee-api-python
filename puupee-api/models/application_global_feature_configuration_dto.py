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


class ApplicationGlobalFeatureConfigurationDto(object):
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
        'enabled_features': 'list[str]'
    }

    attribute_map = {
        'enabled_features': 'enabledFeatures'
    }

    def __init__(self, enabled_features=None, local_vars_configuration=None):  # noqa: E501
        """ApplicationGlobalFeatureConfigurationDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._enabled_features = None
        self.discriminator = None

        self.enabled_features = enabled_features

    @property
    def enabled_features(self):
        """Gets the enabled_features of this ApplicationGlobalFeatureConfigurationDto.  # noqa: E501


        :return: The enabled_features of this ApplicationGlobalFeatureConfigurationDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._enabled_features

    @enabled_features.setter
    def enabled_features(self, enabled_features):
        """Sets the enabled_features of this ApplicationGlobalFeatureConfigurationDto.


        :param enabled_features: The enabled_features of this ApplicationGlobalFeatureConfigurationDto.  # noqa: E501
        :type enabled_features: list[str]
        """

        self._enabled_features = enabled_features

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
        if not isinstance(other, ApplicationGlobalFeatureConfigurationDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApplicationGlobalFeatureConfigurationDto):
            return True

        return self.to_dict() != other.to_dict()
