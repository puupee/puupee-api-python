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


class MessageTemplateDto(object):
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
        'latest_version': 'int'
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
        'latest_version': 'latestVersion'
    }

    def __init__(self, id=None, creation_time=None, creator_id=None, last_modification_time=None, last_modifier_id=None, is_deleted=None, deleter_id=None, deletion_time=None, name=None, description=None, latest_version=None, local_vars_configuration=None):  # noqa: E501
        """MessageTemplateDto - a model defined in OpenAPI"""  # noqa: E501
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
        self._latest_version = None
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
        if latest_version is not None:
            self.latest_version = latest_version

    @property
    def id(self):
        """Gets the id of this MessageTemplateDto.  # noqa: E501


        :return: The id of this MessageTemplateDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MessageTemplateDto.


        :param id: The id of this MessageTemplateDto.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def creation_time(self):
        """Gets the creation_time of this MessageTemplateDto.  # noqa: E501


        :return: The creation_time of this MessageTemplateDto.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this MessageTemplateDto.


        :param creation_time: The creation_time of this MessageTemplateDto.  # noqa: E501
        :type creation_time: datetime
        """

        self._creation_time = creation_time

    @property
    def creator_id(self):
        """Gets the creator_id of this MessageTemplateDto.  # noqa: E501


        :return: The creator_id of this MessageTemplateDto.  # noqa: E501
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this MessageTemplateDto.


        :param creator_id: The creator_id of this MessageTemplateDto.  # noqa: E501
        :type creator_id: str
        """

        self._creator_id = creator_id

    @property
    def last_modification_time(self):
        """Gets the last_modification_time of this MessageTemplateDto.  # noqa: E501


        :return: The last_modification_time of this MessageTemplateDto.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modification_time

    @last_modification_time.setter
    def last_modification_time(self, last_modification_time):
        """Sets the last_modification_time of this MessageTemplateDto.


        :param last_modification_time: The last_modification_time of this MessageTemplateDto.  # noqa: E501
        :type last_modification_time: datetime
        """

        self._last_modification_time = last_modification_time

    @property
    def last_modifier_id(self):
        """Gets the last_modifier_id of this MessageTemplateDto.  # noqa: E501


        :return: The last_modifier_id of this MessageTemplateDto.  # noqa: E501
        :rtype: str
        """
        return self._last_modifier_id

    @last_modifier_id.setter
    def last_modifier_id(self, last_modifier_id):
        """Sets the last_modifier_id of this MessageTemplateDto.


        :param last_modifier_id: The last_modifier_id of this MessageTemplateDto.  # noqa: E501
        :type last_modifier_id: str
        """

        self._last_modifier_id = last_modifier_id

    @property
    def is_deleted(self):
        """Gets the is_deleted of this MessageTemplateDto.  # noqa: E501


        :return: The is_deleted of this MessageTemplateDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        """Sets the is_deleted of this MessageTemplateDto.


        :param is_deleted: The is_deleted of this MessageTemplateDto.  # noqa: E501
        :type is_deleted: bool
        """

        self._is_deleted = is_deleted

    @property
    def deleter_id(self):
        """Gets the deleter_id of this MessageTemplateDto.  # noqa: E501


        :return: The deleter_id of this MessageTemplateDto.  # noqa: E501
        :rtype: str
        """
        return self._deleter_id

    @deleter_id.setter
    def deleter_id(self, deleter_id):
        """Sets the deleter_id of this MessageTemplateDto.


        :param deleter_id: The deleter_id of this MessageTemplateDto.  # noqa: E501
        :type deleter_id: str
        """

        self._deleter_id = deleter_id

    @property
    def deletion_time(self):
        """Gets the deletion_time of this MessageTemplateDto.  # noqa: E501


        :return: The deletion_time of this MessageTemplateDto.  # noqa: E501
        :rtype: datetime
        """
        return self._deletion_time

    @deletion_time.setter
    def deletion_time(self, deletion_time):
        """Sets the deletion_time of this MessageTemplateDto.


        :param deletion_time: The deletion_time of this MessageTemplateDto.  # noqa: E501
        :type deletion_time: datetime
        """

        self._deletion_time = deletion_time

    @property
    def name(self):
        """Gets the name of this MessageTemplateDto.  # noqa: E501


        :return: The name of this MessageTemplateDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MessageTemplateDto.


        :param name: The name of this MessageTemplateDto.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this MessageTemplateDto.  # noqa: E501


        :return: The description of this MessageTemplateDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this MessageTemplateDto.


        :param description: The description of this MessageTemplateDto.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def latest_version(self):
        """Gets the latest_version of this MessageTemplateDto.  # noqa: E501


        :return: The latest_version of this MessageTemplateDto.  # noqa: E501
        :rtype: int
        """
        return self._latest_version

    @latest_version.setter
    def latest_version(self, latest_version):
        """Sets the latest_version of this MessageTemplateDto.


        :param latest_version: The latest_version of this MessageTemplateDto.  # noqa: E501
        :type latest_version: int
        """

        self._latest_version = latest_version

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
        if not isinstance(other, MessageTemplateDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MessageTemplateDto):
            return True

        return self.to_dict() != other.to_dict()
