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


class UserLoginInfo(object):
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
        'user_name_or_email_address': 'str',
        'password': 'str',
        'remember_me': 'bool'
    }

    attribute_map = {
        'user_name_or_email_address': 'userNameOrEmailAddress',
        'password': 'password',
        'remember_me': 'rememberMe'
    }

    def __init__(self, user_name_or_email_address=None, password=None, remember_me=None, local_vars_configuration=None):  # noqa: E501
        """UserLoginInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._user_name_or_email_address = None
        self._password = None
        self._remember_me = None
        self.discriminator = None

        self.user_name_or_email_address = user_name_or_email_address
        self.password = password
        if remember_me is not None:
            self.remember_me = remember_me

    @property
    def user_name_or_email_address(self):
        """Gets the user_name_or_email_address of this UserLoginInfo.  # noqa: E501


        :return: The user_name_or_email_address of this UserLoginInfo.  # noqa: E501
        :rtype: str
        """
        return self._user_name_or_email_address

    @user_name_or_email_address.setter
    def user_name_or_email_address(self, user_name_or_email_address):
        """Sets the user_name_or_email_address of this UserLoginInfo.


        :param user_name_or_email_address: The user_name_or_email_address of this UserLoginInfo.  # noqa: E501
        :type user_name_or_email_address: str
        """
        if self.local_vars_configuration.client_side_validation and user_name_or_email_address is None:  # noqa: E501
            raise ValueError("Invalid value for `user_name_or_email_address`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                user_name_or_email_address is not None and len(user_name_or_email_address) > 255):
            raise ValueError("Invalid value for `user_name_or_email_address`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                user_name_or_email_address is not None and len(user_name_or_email_address) < 0):
            raise ValueError("Invalid value for `user_name_or_email_address`, length must be greater than or equal to `0`")  # noqa: E501

        self._user_name_or_email_address = user_name_or_email_address

    @property
    def password(self):
        """Gets the password of this UserLoginInfo.  # noqa: E501


        :return: The password of this UserLoginInfo.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this UserLoginInfo.


        :param password: The password of this UserLoginInfo.  # noqa: E501
        :type password: str
        """
        if self.local_vars_configuration.client_side_validation and password is None:  # noqa: E501
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                password is not None and len(password) > 32):
            raise ValueError("Invalid value for `password`, length must be less than or equal to `32`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                password is not None and len(password) < 0):
            raise ValueError("Invalid value for `password`, length must be greater than or equal to `0`")  # noqa: E501

        self._password = password

    @property
    def remember_me(self):
        """Gets the remember_me of this UserLoginInfo.  # noqa: E501


        :return: The remember_me of this UserLoginInfo.  # noqa: E501
        :rtype: bool
        """
        return self._remember_me

    @remember_me.setter
    def remember_me(self, remember_me):
        """Sets the remember_me of this UserLoginInfo.


        :param remember_me: The remember_me of this UserLoginInfo.  # noqa: E501
        :type remember_me: bool
        """

        self._remember_me = remember_me

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
        if not isinstance(other, UserLoginInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserLoginInfo):
            return True

        return self.to_dict() != other.to_dict()
