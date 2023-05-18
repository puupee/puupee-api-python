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


class CurrentCultureDto(object):
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
        'display_name': 'str',
        'english_name': 'str',
        'three_letter_iso_language_name': 'str',
        'two_letter_iso_language_name': 'str',
        'is_right_to_left': 'bool',
        'culture_name': 'str',
        'name': 'str',
        'native_name': 'str',
        'date_time_format': 'DateTimeFormatDto'
    }

    attribute_map = {
        'display_name': 'displayName',
        'english_name': 'englishName',
        'three_letter_iso_language_name': 'threeLetterIsoLanguageName',
        'two_letter_iso_language_name': 'twoLetterIsoLanguageName',
        'is_right_to_left': 'isRightToLeft',
        'culture_name': 'cultureName',
        'name': 'name',
        'native_name': 'nativeName',
        'date_time_format': 'dateTimeFormat'
    }

    def __init__(self, display_name=None, english_name=None, three_letter_iso_language_name=None, two_letter_iso_language_name=None, is_right_to_left=None, culture_name=None, name=None, native_name=None, date_time_format=None, local_vars_configuration=None):  # noqa: E501
        """CurrentCultureDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._display_name = None
        self._english_name = None
        self._three_letter_iso_language_name = None
        self._two_letter_iso_language_name = None
        self._is_right_to_left = None
        self._culture_name = None
        self._name = None
        self._native_name = None
        self._date_time_format = None
        self.discriminator = None

        self.display_name = display_name
        self.english_name = english_name
        self.three_letter_iso_language_name = three_letter_iso_language_name
        self.two_letter_iso_language_name = two_letter_iso_language_name
        if is_right_to_left is not None:
            self.is_right_to_left = is_right_to_left
        self.culture_name = culture_name
        self.name = name
        self.native_name = native_name
        if date_time_format is not None:
            self.date_time_format = date_time_format

    @property
    def display_name(self):
        """Gets the display_name of this CurrentCultureDto.  # noqa: E501


        :return: The display_name of this CurrentCultureDto.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this CurrentCultureDto.


        :param display_name: The display_name of this CurrentCultureDto.  # noqa: E501
        :type display_name: str
        """

        self._display_name = display_name

    @property
    def english_name(self):
        """Gets the english_name of this CurrentCultureDto.  # noqa: E501


        :return: The english_name of this CurrentCultureDto.  # noqa: E501
        :rtype: str
        """
        return self._english_name

    @english_name.setter
    def english_name(self, english_name):
        """Sets the english_name of this CurrentCultureDto.


        :param english_name: The english_name of this CurrentCultureDto.  # noqa: E501
        :type english_name: str
        """

        self._english_name = english_name

    @property
    def three_letter_iso_language_name(self):
        """Gets the three_letter_iso_language_name of this CurrentCultureDto.  # noqa: E501


        :return: The three_letter_iso_language_name of this CurrentCultureDto.  # noqa: E501
        :rtype: str
        """
        return self._three_letter_iso_language_name

    @three_letter_iso_language_name.setter
    def three_letter_iso_language_name(self, three_letter_iso_language_name):
        """Sets the three_letter_iso_language_name of this CurrentCultureDto.


        :param three_letter_iso_language_name: The three_letter_iso_language_name of this CurrentCultureDto.  # noqa: E501
        :type three_letter_iso_language_name: str
        """

        self._three_letter_iso_language_name = three_letter_iso_language_name

    @property
    def two_letter_iso_language_name(self):
        """Gets the two_letter_iso_language_name of this CurrentCultureDto.  # noqa: E501


        :return: The two_letter_iso_language_name of this CurrentCultureDto.  # noqa: E501
        :rtype: str
        """
        return self._two_letter_iso_language_name

    @two_letter_iso_language_name.setter
    def two_letter_iso_language_name(self, two_letter_iso_language_name):
        """Sets the two_letter_iso_language_name of this CurrentCultureDto.


        :param two_letter_iso_language_name: The two_letter_iso_language_name of this CurrentCultureDto.  # noqa: E501
        :type two_letter_iso_language_name: str
        """

        self._two_letter_iso_language_name = two_letter_iso_language_name

    @property
    def is_right_to_left(self):
        """Gets the is_right_to_left of this CurrentCultureDto.  # noqa: E501


        :return: The is_right_to_left of this CurrentCultureDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_right_to_left

    @is_right_to_left.setter
    def is_right_to_left(self, is_right_to_left):
        """Sets the is_right_to_left of this CurrentCultureDto.


        :param is_right_to_left: The is_right_to_left of this CurrentCultureDto.  # noqa: E501
        :type is_right_to_left: bool
        """

        self._is_right_to_left = is_right_to_left

    @property
    def culture_name(self):
        """Gets the culture_name of this CurrentCultureDto.  # noqa: E501


        :return: The culture_name of this CurrentCultureDto.  # noqa: E501
        :rtype: str
        """
        return self._culture_name

    @culture_name.setter
    def culture_name(self, culture_name):
        """Sets the culture_name of this CurrentCultureDto.


        :param culture_name: The culture_name of this CurrentCultureDto.  # noqa: E501
        :type culture_name: str
        """

        self._culture_name = culture_name

    @property
    def name(self):
        """Gets the name of this CurrentCultureDto.  # noqa: E501


        :return: The name of this CurrentCultureDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CurrentCultureDto.


        :param name: The name of this CurrentCultureDto.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def native_name(self):
        """Gets the native_name of this CurrentCultureDto.  # noqa: E501


        :return: The native_name of this CurrentCultureDto.  # noqa: E501
        :rtype: str
        """
        return self._native_name

    @native_name.setter
    def native_name(self, native_name):
        """Sets the native_name of this CurrentCultureDto.


        :param native_name: The native_name of this CurrentCultureDto.  # noqa: E501
        :type native_name: str
        """

        self._native_name = native_name

    @property
    def date_time_format(self):
        """Gets the date_time_format of this CurrentCultureDto.  # noqa: E501


        :return: The date_time_format of this CurrentCultureDto.  # noqa: E501
        :rtype: DateTimeFormatDto
        """
        return self._date_time_format

    @date_time_format.setter
    def date_time_format(self, date_time_format):
        """Sets the date_time_format of this CurrentCultureDto.


        :param date_time_format: The date_time_format of this CurrentCultureDto.  # noqa: E501
        :type date_time_format: DateTimeFormatDto
        """

        self._date_time_format = date_time_format

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
        if not isinstance(other, CurrentCultureDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CurrentCultureDto):
            return True

        return self.to_dict() != other.to_dict()
