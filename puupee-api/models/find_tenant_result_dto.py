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


class FindTenantResultDto(object):
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
        'success': 'bool',
        'tenant_id': 'str',
        'name': 'str',
        'is_active': 'bool'
    }

    attribute_map = {
        'success': 'success',
        'tenant_id': 'tenantId',
        'name': 'name',
        'is_active': 'isActive'
    }

    def __init__(self, success=None, tenant_id=None, name=None, is_active=None, local_vars_configuration=None):  # noqa: E501
        """FindTenantResultDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._success = None
        self._tenant_id = None
        self._name = None
        self._is_active = None
        self.discriminator = None

        if success is not None:
            self.success = success
        self.tenant_id = tenant_id
        self.name = name
        if is_active is not None:
            self.is_active = is_active

    @property
    def success(self):
        """Gets the success of this FindTenantResultDto.  # noqa: E501


        :return: The success of this FindTenantResultDto.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this FindTenantResultDto.


        :param success: The success of this FindTenantResultDto.  # noqa: E501
        :type success: bool
        """

        self._success = success

    @property
    def tenant_id(self):
        """Gets the tenant_id of this FindTenantResultDto.  # noqa: E501


        :return: The tenant_id of this FindTenantResultDto.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this FindTenantResultDto.


        :param tenant_id: The tenant_id of this FindTenantResultDto.  # noqa: E501
        :type tenant_id: str
        """

        self._tenant_id = tenant_id

    @property
    def name(self):
        """Gets the name of this FindTenantResultDto.  # noqa: E501


        :return: The name of this FindTenantResultDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FindTenantResultDto.


        :param name: The name of this FindTenantResultDto.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def is_active(self):
        """Gets the is_active of this FindTenantResultDto.  # noqa: E501


        :return: The is_active of this FindTenantResultDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this FindTenantResultDto.


        :param is_active: The is_active of this FindTenantResultDto.  # noqa: E501
        :type is_active: bool
        """

        self._is_active = is_active

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
        if not isinstance(other, FindTenantResultDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FindTenantResultDto):
            return True

        return self.to_dict() != other.to_dict()