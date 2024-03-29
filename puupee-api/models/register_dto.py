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


class RegisterDto(object):
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
        'user_name': 'str',
        'email_address': 'str',
        'password': 'str',
        'app_name': 'str'
    }

    attribute_map = {
        'extra_properties': 'extraProperties',
        'user_name': 'userName',
        'email_address': 'emailAddress',
        'password': 'password',
        'app_name': 'appName'
    }

    def __init__(self, extra_properties=None, user_name=None, email_address=None, password=None, app_name=None, local_vars_configuration=None):  # noqa: E501
        """RegisterDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._extra_properties = None
        self._user_name = None
        self._email_address = None
        self._password = None
        self._app_name = None
        self.discriminator = None

        self.extra_properties = extra_properties
        self.user_name = user_name
        self.email_address = email_address
        self.password = password
        self.app_name = app_name

    @property
    def extra_properties(self):
        """Gets the extra_properties of this RegisterDto.  # noqa: E501


        :return: The extra_properties of this RegisterDto.  # noqa: E501
        :rtype: dict[str, object]
        """
        return self._extra_properties

    @extra_properties.setter
    def extra_properties(self, extra_properties):
        """Sets the extra_properties of this RegisterDto.


        :param extra_properties: The extra_properties of this RegisterDto.  # noqa: E501
        :type extra_properties: dict[str, object]
        """

        self._extra_properties = extra_properties

    @property
    def user_name(self):
        """Gets the user_name of this RegisterDto.  # noqa: E501


        :return: The user_name of this RegisterDto.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this RegisterDto.


        :param user_name: The user_name of this RegisterDto.  # noqa: E501
        :type user_name: str
        """
        if self.local_vars_configuration.client_side_validation and user_name is None:  # noqa: E501
            raise ValueError("Invalid value for `user_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                user_name is not None and len(user_name) > 256):
            raise ValueError("Invalid value for `user_name`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                user_name is not None and len(user_name) < 0):
            raise ValueError("Invalid value for `user_name`, length must be greater than or equal to `0`")  # noqa: E501

        self._user_name = user_name

    @property
    def email_address(self):
        """Gets the email_address of this RegisterDto.  # noqa: E501


        :return: The email_address of this RegisterDto.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this RegisterDto.


        :param email_address: The email_address of this RegisterDto.  # noqa: E501
        :type email_address: str
        """
        if self.local_vars_configuration.client_side_validation and email_address is None:  # noqa: E501
            raise ValueError("Invalid value for `email_address`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                email_address is not None and len(email_address) > 256):
            raise ValueError("Invalid value for `email_address`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                email_address is not None and len(email_address) < 0):
            raise ValueError("Invalid value for `email_address`, length must be greater than or equal to `0`")  # noqa: E501

        self._email_address = email_address

    @property
    def password(self):
        """Gets the password of this RegisterDto.  # noqa: E501


        :return: The password of this RegisterDto.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this RegisterDto.


        :param password: The password of this RegisterDto.  # noqa: E501
        :type password: str
        """
        if self.local_vars_configuration.client_side_validation and password is None:  # noqa: E501
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                password is not None and len(password) > 128):
            raise ValueError("Invalid value for `password`, length must be less than or equal to `128`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                password is not None and len(password) < 0):
            raise ValueError("Invalid value for `password`, length must be greater than or equal to `0`")  # noqa: E501

        self._password = password

    @property
    def app_name(self):
        """Gets the app_name of this RegisterDto.  # noqa: E501


        :return: The app_name of this RegisterDto.  # noqa: E501
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this RegisterDto.


        :param app_name: The app_name of this RegisterDto.  # noqa: E501
        :type app_name: str
        """
        if self.local_vars_configuration.client_side_validation and app_name is None:  # noqa: E501
            raise ValueError("Invalid value for `app_name`, must not be `None`")  # noqa: E501

        self._app_name = app_name

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
        if not isinstance(other, RegisterDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RegisterDto):
            return True

        return self.to_dict() != other.to_dict()
