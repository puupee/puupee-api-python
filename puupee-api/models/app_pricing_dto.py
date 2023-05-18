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


class AppPricingDto(object):
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
        'naming': 'str',
        'month_product_id': 'str',
        'year_product_id': 'str',
        'description': 'str',
        'app_id': 'str',
        'month_price': 'float',
        'month_discount': 'float',
        'month_discount_price': 'float',
        'month_discount_start_at': 'datetime',
        'month_discount_end_at': 'datetime',
        'year_price': 'float',
        'year_discount': 'float',
        'year_discount_price': 'float',
        'year_discount_start_at': 'datetime',
        'year_discount_end_at': 'datetime',
        'sort_index': 'int',
        'items': 'list[AppPricingItemDto]'
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
        'naming': 'naming',
        'month_product_id': 'monthProductId',
        'year_product_id': 'yearProductId',
        'description': 'description',
        'app_id': 'appId',
        'month_price': 'monthPrice',
        'month_discount': 'monthDiscount',
        'month_discount_price': 'monthDiscountPrice',
        'month_discount_start_at': 'monthDiscountStartAt',
        'month_discount_end_at': 'monthDiscountEndAt',
        'year_price': 'yearPrice',
        'year_discount': 'yearDiscount',
        'year_discount_price': 'yearDiscountPrice',
        'year_discount_start_at': 'yearDiscountStartAt',
        'year_discount_end_at': 'yearDiscountEndAt',
        'sort_index': 'sortIndex',
        'items': 'items'
    }

    def __init__(self, id=None, creation_time=None, creator_id=None, last_modification_time=None, last_modifier_id=None, is_deleted=None, deleter_id=None, deletion_time=None, naming=None, month_product_id=None, year_product_id=None, description=None, app_id=None, month_price=None, month_discount=None, month_discount_price=None, month_discount_start_at=None, month_discount_end_at=None, year_price=None, year_discount=None, year_discount_price=None, year_discount_start_at=None, year_discount_end_at=None, sort_index=None, items=None, local_vars_configuration=None):  # noqa: E501
        """AppPricingDto - a model defined in OpenAPI"""  # noqa: E501
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
        self._naming = None
        self._month_product_id = None
        self._year_product_id = None
        self._description = None
        self._app_id = None
        self._month_price = None
        self._month_discount = None
        self._month_discount_price = None
        self._month_discount_start_at = None
        self._month_discount_end_at = None
        self._year_price = None
        self._year_discount = None
        self._year_discount_price = None
        self._year_discount_start_at = None
        self._year_discount_end_at = None
        self._sort_index = None
        self._items = None
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
        self.naming = naming
        self.month_product_id = month_product_id
        self.year_product_id = year_product_id
        self.description = description
        if app_id is not None:
            self.app_id = app_id
        if month_price is not None:
            self.month_price = month_price
        self.month_discount = month_discount
        self.month_discount_price = month_discount_price
        self.month_discount_start_at = month_discount_start_at
        self.month_discount_end_at = month_discount_end_at
        if year_price is not None:
            self.year_price = year_price
        self.year_discount = year_discount
        self.year_discount_price = year_discount_price
        self.year_discount_start_at = year_discount_start_at
        self.year_discount_end_at = year_discount_end_at
        if sort_index is not None:
            self.sort_index = sort_index
        self.items = items

    @property
    def id(self):
        """Gets the id of this AppPricingDto.  # noqa: E501


        :return: The id of this AppPricingDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AppPricingDto.


        :param id: The id of this AppPricingDto.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def creation_time(self):
        """Gets the creation_time of this AppPricingDto.  # noqa: E501


        :return: The creation_time of this AppPricingDto.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this AppPricingDto.


        :param creation_time: The creation_time of this AppPricingDto.  # noqa: E501
        :type creation_time: datetime
        """

        self._creation_time = creation_time

    @property
    def creator_id(self):
        """Gets the creator_id of this AppPricingDto.  # noqa: E501


        :return: The creator_id of this AppPricingDto.  # noqa: E501
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this AppPricingDto.


        :param creator_id: The creator_id of this AppPricingDto.  # noqa: E501
        :type creator_id: str
        """

        self._creator_id = creator_id

    @property
    def last_modification_time(self):
        """Gets the last_modification_time of this AppPricingDto.  # noqa: E501


        :return: The last_modification_time of this AppPricingDto.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modification_time

    @last_modification_time.setter
    def last_modification_time(self, last_modification_time):
        """Sets the last_modification_time of this AppPricingDto.


        :param last_modification_time: The last_modification_time of this AppPricingDto.  # noqa: E501
        :type last_modification_time: datetime
        """

        self._last_modification_time = last_modification_time

    @property
    def last_modifier_id(self):
        """Gets the last_modifier_id of this AppPricingDto.  # noqa: E501


        :return: The last_modifier_id of this AppPricingDto.  # noqa: E501
        :rtype: str
        """
        return self._last_modifier_id

    @last_modifier_id.setter
    def last_modifier_id(self, last_modifier_id):
        """Sets the last_modifier_id of this AppPricingDto.


        :param last_modifier_id: The last_modifier_id of this AppPricingDto.  # noqa: E501
        :type last_modifier_id: str
        """

        self._last_modifier_id = last_modifier_id

    @property
    def is_deleted(self):
        """Gets the is_deleted of this AppPricingDto.  # noqa: E501


        :return: The is_deleted of this AppPricingDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        """Sets the is_deleted of this AppPricingDto.


        :param is_deleted: The is_deleted of this AppPricingDto.  # noqa: E501
        :type is_deleted: bool
        """

        self._is_deleted = is_deleted

    @property
    def deleter_id(self):
        """Gets the deleter_id of this AppPricingDto.  # noqa: E501


        :return: The deleter_id of this AppPricingDto.  # noqa: E501
        :rtype: str
        """
        return self._deleter_id

    @deleter_id.setter
    def deleter_id(self, deleter_id):
        """Sets the deleter_id of this AppPricingDto.


        :param deleter_id: The deleter_id of this AppPricingDto.  # noqa: E501
        :type deleter_id: str
        """

        self._deleter_id = deleter_id

    @property
    def deletion_time(self):
        """Gets the deletion_time of this AppPricingDto.  # noqa: E501


        :return: The deletion_time of this AppPricingDto.  # noqa: E501
        :rtype: datetime
        """
        return self._deletion_time

    @deletion_time.setter
    def deletion_time(self, deletion_time):
        """Sets the deletion_time of this AppPricingDto.


        :param deletion_time: The deletion_time of this AppPricingDto.  # noqa: E501
        :type deletion_time: datetime
        """

        self._deletion_time = deletion_time

    @property
    def naming(self):
        """Gets the naming of this AppPricingDto.  # noqa: E501


        :return: The naming of this AppPricingDto.  # noqa: E501
        :rtype: str
        """
        return self._naming

    @naming.setter
    def naming(self, naming):
        """Sets the naming of this AppPricingDto.


        :param naming: The naming of this AppPricingDto.  # noqa: E501
        :type naming: str
        """

        self._naming = naming

    @property
    def month_product_id(self):
        """Gets the month_product_id of this AppPricingDto.  # noqa: E501


        :return: The month_product_id of this AppPricingDto.  # noqa: E501
        :rtype: str
        """
        return self._month_product_id

    @month_product_id.setter
    def month_product_id(self, month_product_id):
        """Sets the month_product_id of this AppPricingDto.


        :param month_product_id: The month_product_id of this AppPricingDto.  # noqa: E501
        :type month_product_id: str
        """

        self._month_product_id = month_product_id

    @property
    def year_product_id(self):
        """Gets the year_product_id of this AppPricingDto.  # noqa: E501


        :return: The year_product_id of this AppPricingDto.  # noqa: E501
        :rtype: str
        """
        return self._year_product_id

    @year_product_id.setter
    def year_product_id(self, year_product_id):
        """Sets the year_product_id of this AppPricingDto.


        :param year_product_id: The year_product_id of this AppPricingDto.  # noqa: E501
        :type year_product_id: str
        """

        self._year_product_id = year_product_id

    @property
    def description(self):
        """Gets the description of this AppPricingDto.  # noqa: E501


        :return: The description of this AppPricingDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AppPricingDto.


        :param description: The description of this AppPricingDto.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def app_id(self):
        """Gets the app_id of this AppPricingDto.  # noqa: E501


        :return: The app_id of this AppPricingDto.  # noqa: E501
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this AppPricingDto.


        :param app_id: The app_id of this AppPricingDto.  # noqa: E501
        :type app_id: str
        """

        self._app_id = app_id

    @property
    def month_price(self):
        """Gets the month_price of this AppPricingDto.  # noqa: E501


        :return: The month_price of this AppPricingDto.  # noqa: E501
        :rtype: float
        """
        return self._month_price

    @month_price.setter
    def month_price(self, month_price):
        """Sets the month_price of this AppPricingDto.


        :param month_price: The month_price of this AppPricingDto.  # noqa: E501
        :type month_price: float
        """

        self._month_price = month_price

    @property
    def month_discount(self):
        """Gets the month_discount of this AppPricingDto.  # noqa: E501


        :return: The month_discount of this AppPricingDto.  # noqa: E501
        :rtype: float
        """
        return self._month_discount

    @month_discount.setter
    def month_discount(self, month_discount):
        """Sets the month_discount of this AppPricingDto.


        :param month_discount: The month_discount of this AppPricingDto.  # noqa: E501
        :type month_discount: float
        """

        self._month_discount = month_discount

    @property
    def month_discount_price(self):
        """Gets the month_discount_price of this AppPricingDto.  # noqa: E501


        :return: The month_discount_price of this AppPricingDto.  # noqa: E501
        :rtype: float
        """
        return self._month_discount_price

    @month_discount_price.setter
    def month_discount_price(self, month_discount_price):
        """Sets the month_discount_price of this AppPricingDto.


        :param month_discount_price: The month_discount_price of this AppPricingDto.  # noqa: E501
        :type month_discount_price: float
        """

        self._month_discount_price = month_discount_price

    @property
    def month_discount_start_at(self):
        """Gets the month_discount_start_at of this AppPricingDto.  # noqa: E501


        :return: The month_discount_start_at of this AppPricingDto.  # noqa: E501
        :rtype: datetime
        """
        return self._month_discount_start_at

    @month_discount_start_at.setter
    def month_discount_start_at(self, month_discount_start_at):
        """Sets the month_discount_start_at of this AppPricingDto.


        :param month_discount_start_at: The month_discount_start_at of this AppPricingDto.  # noqa: E501
        :type month_discount_start_at: datetime
        """

        self._month_discount_start_at = month_discount_start_at

    @property
    def month_discount_end_at(self):
        """Gets the month_discount_end_at of this AppPricingDto.  # noqa: E501


        :return: The month_discount_end_at of this AppPricingDto.  # noqa: E501
        :rtype: datetime
        """
        return self._month_discount_end_at

    @month_discount_end_at.setter
    def month_discount_end_at(self, month_discount_end_at):
        """Sets the month_discount_end_at of this AppPricingDto.


        :param month_discount_end_at: The month_discount_end_at of this AppPricingDto.  # noqa: E501
        :type month_discount_end_at: datetime
        """

        self._month_discount_end_at = month_discount_end_at

    @property
    def year_price(self):
        """Gets the year_price of this AppPricingDto.  # noqa: E501


        :return: The year_price of this AppPricingDto.  # noqa: E501
        :rtype: float
        """
        return self._year_price

    @year_price.setter
    def year_price(self, year_price):
        """Sets the year_price of this AppPricingDto.


        :param year_price: The year_price of this AppPricingDto.  # noqa: E501
        :type year_price: float
        """

        self._year_price = year_price

    @property
    def year_discount(self):
        """Gets the year_discount of this AppPricingDto.  # noqa: E501


        :return: The year_discount of this AppPricingDto.  # noqa: E501
        :rtype: float
        """
        return self._year_discount

    @year_discount.setter
    def year_discount(self, year_discount):
        """Sets the year_discount of this AppPricingDto.


        :param year_discount: The year_discount of this AppPricingDto.  # noqa: E501
        :type year_discount: float
        """

        self._year_discount = year_discount

    @property
    def year_discount_price(self):
        """Gets the year_discount_price of this AppPricingDto.  # noqa: E501


        :return: The year_discount_price of this AppPricingDto.  # noqa: E501
        :rtype: float
        """
        return self._year_discount_price

    @year_discount_price.setter
    def year_discount_price(self, year_discount_price):
        """Sets the year_discount_price of this AppPricingDto.


        :param year_discount_price: The year_discount_price of this AppPricingDto.  # noqa: E501
        :type year_discount_price: float
        """

        self._year_discount_price = year_discount_price

    @property
    def year_discount_start_at(self):
        """Gets the year_discount_start_at of this AppPricingDto.  # noqa: E501


        :return: The year_discount_start_at of this AppPricingDto.  # noqa: E501
        :rtype: datetime
        """
        return self._year_discount_start_at

    @year_discount_start_at.setter
    def year_discount_start_at(self, year_discount_start_at):
        """Sets the year_discount_start_at of this AppPricingDto.


        :param year_discount_start_at: The year_discount_start_at of this AppPricingDto.  # noqa: E501
        :type year_discount_start_at: datetime
        """

        self._year_discount_start_at = year_discount_start_at

    @property
    def year_discount_end_at(self):
        """Gets the year_discount_end_at of this AppPricingDto.  # noqa: E501


        :return: The year_discount_end_at of this AppPricingDto.  # noqa: E501
        :rtype: datetime
        """
        return self._year_discount_end_at

    @year_discount_end_at.setter
    def year_discount_end_at(self, year_discount_end_at):
        """Sets the year_discount_end_at of this AppPricingDto.


        :param year_discount_end_at: The year_discount_end_at of this AppPricingDto.  # noqa: E501
        :type year_discount_end_at: datetime
        """

        self._year_discount_end_at = year_discount_end_at

    @property
    def sort_index(self):
        """Gets the sort_index of this AppPricingDto.  # noqa: E501


        :return: The sort_index of this AppPricingDto.  # noqa: E501
        :rtype: int
        """
        return self._sort_index

    @sort_index.setter
    def sort_index(self, sort_index):
        """Sets the sort_index of this AppPricingDto.


        :param sort_index: The sort_index of this AppPricingDto.  # noqa: E501
        :type sort_index: int
        """

        self._sort_index = sort_index

    @property
    def items(self):
        """Gets the items of this AppPricingDto.  # noqa: E501


        :return: The items of this AppPricingDto.  # noqa: E501
        :rtype: list[AppPricingItemDto]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this AppPricingDto.


        :param items: The items of this AppPricingDto.  # noqa: E501
        :type items: list[AppPricingItemDto]
        """

        self._items = items

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
        if not isinstance(other, AppPricingDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AppPricingDto):
            return True

        return self.to_dict() != other.to_dict()