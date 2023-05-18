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


class Int32KeyValue(object):
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
        'value': 'int',
        'duration_seconds': 'float',
        'expired_at': 'datetime',
        'created_at': 'datetime'
    }

    attribute_map = {
        'value': 'value',
        'duration_seconds': 'durationSeconds',
        'expired_at': 'expiredAt',
        'created_at': 'createdAt'
    }

    def __init__(self, value=None, duration_seconds=None, expired_at=None, created_at=None, local_vars_configuration=None):  # noqa: E501
        """Int32KeyValue - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._value = None
        self._duration_seconds = None
        self._expired_at = None
        self._created_at = None
        self.discriminator = None

        if value is not None:
            self.value = value
        self.duration_seconds = duration_seconds
        self.expired_at = expired_at
        self.created_at = created_at

    @property
    def value(self):
        """Gets the value of this Int32KeyValue.  # noqa: E501


        :return: The value of this Int32KeyValue.  # noqa: E501
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Int32KeyValue.


        :param value: The value of this Int32KeyValue.  # noqa: E501
        :type value: int
        """

        self._value = value

    @property
    def duration_seconds(self):
        """Gets the duration_seconds of this Int32KeyValue.  # noqa: E501


        :return: The duration_seconds of this Int32KeyValue.  # noqa: E501
        :rtype: float
        """
        return self._duration_seconds

    @duration_seconds.setter
    def duration_seconds(self, duration_seconds):
        """Sets the duration_seconds of this Int32KeyValue.


        :param duration_seconds: The duration_seconds of this Int32KeyValue.  # noqa: E501
        :type duration_seconds: float
        """

        self._duration_seconds = duration_seconds

    @property
    def expired_at(self):
        """Gets the expired_at of this Int32KeyValue.  # noqa: E501


        :return: The expired_at of this Int32KeyValue.  # noqa: E501
        :rtype: datetime
        """
        return self._expired_at

    @expired_at.setter
    def expired_at(self, expired_at):
        """Sets the expired_at of this Int32KeyValue.


        :param expired_at: The expired_at of this Int32KeyValue.  # noqa: E501
        :type expired_at: datetime
        """

        self._expired_at = expired_at

    @property
    def created_at(self):
        """Gets the created_at of this Int32KeyValue.  # noqa: E501


        :return: The created_at of this Int32KeyValue.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Int32KeyValue.


        :param created_at: The created_at of this Int32KeyValue.  # noqa: E501
        :type created_at: datetime
        """

        self._created_at = created_at

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
        if not isinstance(other, Int32KeyValue):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Int32KeyValue):
            return True

        return self.to_dict() != other.to_dict()
