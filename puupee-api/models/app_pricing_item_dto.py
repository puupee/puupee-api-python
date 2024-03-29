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


class AppPricingItemDto(object):
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
        'id': 'str',
        'creation_time': 'datetime',
        'creator_id': 'str',
        'last_modification_time': 'datetime',
        'last_modifier_id': 'str',
        'is_deleted': 'bool',
        'deleter_id': 'str',
        'deletion_time': 'datetime',
        'name': 'str',
        'description': 'str',
        'link_url': 'str',
        'display': 'str',
        'values': 'list[str]',
        'app_id': 'str',
        'is_available': 'bool',
        'has_value': 'bool',
        'sort_index': 'int'
    }

    attribute_map = {
        'id': 'id',
        'creation_time': 'creationTime',
        'creator_id': 'creatorId',
        'last_modification_time': 'lastModificationTime',
        'last_modifier_id': 'lastModifierId',
        'is_deleted': 'isDeleted',
        'deleter_id': 'deleterId',
        'deletion_time': 'deletionTime',
        'name': 'name',
        'description': 'description',
        'link_url': 'linkUrl',
        'display': 'display',
        'values': 'values',
        'app_id': 'appId',
        'is_available': 'isAvailable',
        'has_value': 'hasValue',
        'sort_index': 'sortIndex'
    }

    def __init__(self, id=None, creation_time=None, creator_id=None, last_modification_time=None, last_modifier_id=None, is_deleted=None, deleter_id=None, deletion_time=None, name=None, description=None, link_url=None, display=None, values=None, app_id=None, is_available=None, has_value=None, sort_index=None, local_vars_configuration=None):  # noqa: E501
        """AppPricingItemDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._creation_time = None
        self._creator_id = None
        self._last_modification_time = None
        self._last_modifier_id = None
        self._is_deleted = None
        self._deleter_id = None
        self._deletion_time = None
        self._name = None
        self._description = None
        self._link_url = None
        self._display = None
        self._values = None
        self._app_id = None
        self._is_available = None
        self._has_value = None
        self._sort_index = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if creation_time is not None:
            self.creation_time = creation_time
        self.creator_id = creator_id
        self.last_modification_time = last_modification_time
        self.last_modifier_id = last_modifier_id
        if is_deleted is not None:
            self.is_deleted = is_deleted
        self.deleter_id = deleter_id
        self.deletion_time = deletion_time
        self.name = name
        self.description = description
        self.link_url = link_url
        self.display = display
        self.values = values
        if app_id is not None:
            self.app_id = app_id
        if is_available is not None:
            self.is_available = is_available
        if has_value is not None:
            self.has_value = has_value
        if sort_index is not None:
            self.sort_index = sort_index

    @property
    def id(self):
        """Gets the id of this AppPricingItemDto.  # noqa: E501


        :return: The id of this AppPricingItemDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AppPricingItemDto.


        :param id: The id of this AppPricingItemDto.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def creation_time(self):
        """Gets the creation_time of this AppPricingItemDto.  # noqa: E501


        :return: The creation_time of this AppPricingItemDto.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this AppPricingItemDto.


        :param creation_time: The creation_time of this AppPricingItemDto.  # noqa: E501
        :type creation_time: datetime
        """

        self._creation_time = creation_time

    @property
    def creator_id(self):
        """Gets the creator_id of this AppPricingItemDto.  # noqa: E501


        :return: The creator_id of this AppPricingItemDto.  # noqa: E501
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this AppPricingItemDto.


        :param creator_id: The creator_id of this AppPricingItemDto.  # noqa: E501
        :type creator_id: str
        """

        self._creator_id = creator_id

    @property
    def last_modification_time(self):
        """Gets the last_modification_time of this AppPricingItemDto.  # noqa: E501


        :return: The last_modification_time of this AppPricingItemDto.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modification_time

    @last_modification_time.setter
    def last_modification_time(self, last_modification_time):
        """Sets the last_modification_time of this AppPricingItemDto.


        :param last_modification_time: The last_modification_time of this AppPricingItemDto.  # noqa: E501
        :type last_modification_time: datetime
        """

        self._last_modification_time = last_modification_time

    @property
    def last_modifier_id(self):
        """Gets the last_modifier_id of this AppPricingItemDto.  # noqa: E501


        :return: The last_modifier_id of this AppPricingItemDto.  # noqa: E501
        :rtype: str
        """
        return self._last_modifier_id

    @last_modifier_id.setter
    def last_modifier_id(self, last_modifier_id):
        """Sets the last_modifier_id of this AppPricingItemDto.


        :param last_modifier_id: The last_modifier_id of this AppPricingItemDto.  # noqa: E501
        :type last_modifier_id: str
        """

        self._last_modifier_id = last_modifier_id

    @property
    def is_deleted(self):
        """Gets the is_deleted of this AppPricingItemDto.  # noqa: E501


        :return: The is_deleted of this AppPricingItemDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        """Sets the is_deleted of this AppPricingItemDto.


        :param is_deleted: The is_deleted of this AppPricingItemDto.  # noqa: E501
        :type is_deleted: bool
        """

        self._is_deleted = is_deleted

    @property
    def deleter_id(self):
        """Gets the deleter_id of this AppPricingItemDto.  # noqa: E501


        :return: The deleter_id of this AppPricingItemDto.  # noqa: E501
        :rtype: str
        """
        return self._deleter_id

    @deleter_id.setter
    def deleter_id(self, deleter_id):
        """Sets the deleter_id of this AppPricingItemDto.


        :param deleter_id: The deleter_id of this AppPricingItemDto.  # noqa: E501
        :type deleter_id: str
        """

        self._deleter_id = deleter_id

    @property
    def deletion_time(self):
        """Gets the deletion_time of this AppPricingItemDto.  # noqa: E501


        :return: The deletion_time of this AppPricingItemDto.  # noqa: E501
        :rtype: datetime
        """
        return self._deletion_time

    @deletion_time.setter
    def deletion_time(self, deletion_time):
        """Sets the deletion_time of this AppPricingItemDto.


        :param deletion_time: The deletion_time of this AppPricingItemDto.  # noqa: E501
        :type deletion_time: datetime
        """

        self._deletion_time = deletion_time

    @property
    def name(self):
        """Gets the name of this AppPricingItemDto.  # noqa: E501


        :return: The name of this AppPricingItemDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AppPricingItemDto.


        :param name: The name of this AppPricingItemDto.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this AppPricingItemDto.  # noqa: E501


        :return: The description of this AppPricingItemDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AppPricingItemDto.


        :param description: The description of this AppPricingItemDto.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def link_url(self):
        """Gets the link_url of this AppPricingItemDto.  # noqa: E501


        :return: The link_url of this AppPricingItemDto.  # noqa: E501
        :rtype: str
        """
        return self._link_url

    @link_url.setter
    def link_url(self, link_url):
        """Sets the link_url of this AppPricingItemDto.


        :param link_url: The link_url of this AppPricingItemDto.  # noqa: E501
        :type link_url: str
        """

        self._link_url = link_url

    @property
    def display(self):
        """Gets the display of this AppPricingItemDto.  # noqa: E501


        :return: The display of this AppPricingItemDto.  # noqa: E501
        :rtype: str
        """
        return self._display

    @display.setter
    def display(self, display):
        """Sets the display of this AppPricingItemDto.


        :param display: The display of this AppPricingItemDto.  # noqa: E501
        :type display: str
        """

        self._display = display

    @property
    def values(self):
        """Gets the values of this AppPricingItemDto.  # noqa: E501


        :return: The values of this AppPricingItemDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this AppPricingItemDto.


        :param values: The values of this AppPricingItemDto.  # noqa: E501
        :type values: list[str]
        """

        self._values = values

    @property
    def app_id(self):
        """Gets the app_id of this AppPricingItemDto.  # noqa: E501


        :return: The app_id of this AppPricingItemDto.  # noqa: E501
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this AppPricingItemDto.


        :param app_id: The app_id of this AppPricingItemDto.  # noqa: E501
        :type app_id: str
        """

        self._app_id = app_id

    @property
    def is_available(self):
        """Gets the is_available of this AppPricingItemDto.  # noqa: E501


        :return: The is_available of this AppPricingItemDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_available

    @is_available.setter
    def is_available(self, is_available):
        """Sets the is_available of this AppPricingItemDto.


        :param is_available: The is_available of this AppPricingItemDto.  # noqa: E501
        :type is_available: bool
        """

        self._is_available = is_available

    @property
    def has_value(self):
        """Gets the has_value of this AppPricingItemDto.  # noqa: E501


        :return: The has_value of this AppPricingItemDto.  # noqa: E501
        :rtype: bool
        """
        return self._has_value

    @has_value.setter
    def has_value(self, has_value):
        """Sets the has_value of this AppPricingItemDto.


        :param has_value: The has_value of this AppPricingItemDto.  # noqa: E501
        :type has_value: bool
        """

        self._has_value = has_value

    @property
    def sort_index(self):
        """Gets the sort_index of this AppPricingItemDto.  # noqa: E501


        :return: The sort_index of this AppPricingItemDto.  # noqa: E501
        :rtype: int
        """
        return self._sort_index

    @sort_index.setter
    def sort_index(self, sort_index):
        """Sets the sort_index of this AppPricingItemDto.


        :param sort_index: The sort_index of this AppPricingItemDto.  # noqa: E501
        :type sort_index: int
        """

        self._sort_index = sort_index

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
        if not isinstance(other, AppPricingItemDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AppPricingItemDto):
            return True

        return self.to_dict() != other.to_dict()
