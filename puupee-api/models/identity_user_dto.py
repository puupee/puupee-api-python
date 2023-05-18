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


class IdentityUserDto(object):
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
        'id': 'str',
        'creation_time': 'datetime',
        'creator_id': 'str',
        'last_modification_time': 'datetime',
        'last_modifier_id': 'str',
        'is_deleted': 'bool',
        'deleter_id': 'str',
        'deletion_time': 'datetime',
        'tenant_id': 'str',
        'user_name': 'str',
        'name': 'str',
        'surname': 'str',
        'email': 'str',
        'email_confirmed': 'bool',
        'phone_number': 'str',
        'phone_number_confirmed': 'bool',
        'is_active': 'bool',
        'lockout_enabled': 'bool',
        'lockout_end': 'datetime',
        'concurrency_stamp': 'str',
        'entity_version': 'int'
    }

    attribute_map = {
        'extra_properties': 'extraProperties',
        'id': 'id',
        'creation_time': 'creationTime',
        'creator_id': 'creatorId',
        'last_modification_time': 'lastModificationTime',
        'last_modifier_id': 'lastModifierId',
        'is_deleted': 'isDeleted',
        'deleter_id': 'deleterId',
        'deletion_time': 'deletionTime',
        'tenant_id': 'tenantId',
        'user_name': 'userName',
        'name': 'name',
        'surname': 'surname',
        'email': 'email',
        'email_confirmed': 'emailConfirmed',
        'phone_number': 'phoneNumber',
        'phone_number_confirmed': 'phoneNumberConfirmed',
        'is_active': 'isActive',
        'lockout_enabled': 'lockoutEnabled',
        'lockout_end': 'lockoutEnd',
        'concurrency_stamp': 'concurrencyStamp',
        'entity_version': 'entityVersion'
    }

    def __init__(self, extra_properties=None, id=None, creation_time=None, creator_id=None, last_modification_time=None, last_modifier_id=None, is_deleted=None, deleter_id=None, deletion_time=None, tenant_id=None, user_name=None, name=None, surname=None, email=None, email_confirmed=None, phone_number=None, phone_number_confirmed=None, is_active=None, lockout_enabled=None, lockout_end=None, concurrency_stamp=None, entity_version=None, local_vars_configuration=None):  # noqa: E501
        """IdentityUserDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._extra_properties = None
        self._id = None
        self._creation_time = None
        self._creator_id = None
        self._last_modification_time = None
        self._last_modifier_id = None
        self._is_deleted = None
        self._deleter_id = None
        self._deletion_time = None
        self._tenant_id = None
        self._user_name = None
        self._name = None
        self._surname = None
        self._email = None
        self._email_confirmed = None
        self._phone_number = None
        self._phone_number_confirmed = None
        self._is_active = None
        self._lockout_enabled = None
        self._lockout_end = None
        self._concurrency_stamp = None
        self._entity_version = None
        self.discriminator = None

        self.extra_properties = extra_properties
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
        self.tenant_id = tenant_id
        self.user_name = user_name
        self.name = name
        self.surname = surname
        self.email = email
        if email_confirmed is not None:
            self.email_confirmed = email_confirmed
        self.phone_number = phone_number
        if phone_number_confirmed is not None:
            self.phone_number_confirmed = phone_number_confirmed
        if is_active is not None:
            self.is_active = is_active
        if lockout_enabled is not None:
            self.lockout_enabled = lockout_enabled
        self.lockout_end = lockout_end
        self.concurrency_stamp = concurrency_stamp
        if entity_version is not None:
            self.entity_version = entity_version

    @property
    def extra_properties(self):
        """Gets the extra_properties of this IdentityUserDto.  # noqa: E501


        :return: The extra_properties of this IdentityUserDto.  # noqa: E501
        :rtype: dict[str, object]
        """
        return self._extra_properties

    @extra_properties.setter
    def extra_properties(self, extra_properties):
        """Sets the extra_properties of this IdentityUserDto.


        :param extra_properties: The extra_properties of this IdentityUserDto.  # noqa: E501
        :type extra_properties: dict[str, object]
        """

        self._extra_properties = extra_properties

    @property
    def id(self):
        """Gets the id of this IdentityUserDto.  # noqa: E501


        :return: The id of this IdentityUserDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IdentityUserDto.


        :param id: The id of this IdentityUserDto.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def creation_time(self):
        """Gets the creation_time of this IdentityUserDto.  # noqa: E501


        :return: The creation_time of this IdentityUserDto.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this IdentityUserDto.


        :param creation_time: The creation_time of this IdentityUserDto.  # noqa: E501
        :type creation_time: datetime
        """

        self._creation_time = creation_time

    @property
    def creator_id(self):
        """Gets the creator_id of this IdentityUserDto.  # noqa: E501


        :return: The creator_id of this IdentityUserDto.  # noqa: E501
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this IdentityUserDto.


        :param creator_id: The creator_id of this IdentityUserDto.  # noqa: E501
        :type creator_id: str
        """

        self._creator_id = creator_id

    @property
    def last_modification_time(self):
        """Gets the last_modification_time of this IdentityUserDto.  # noqa: E501


        :return: The last_modification_time of this IdentityUserDto.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modification_time

    @last_modification_time.setter
    def last_modification_time(self, last_modification_time):
        """Sets the last_modification_time of this IdentityUserDto.


        :param last_modification_time: The last_modification_time of this IdentityUserDto.  # noqa: E501
        :type last_modification_time: datetime
        """

        self._last_modification_time = last_modification_time

    @property
    def last_modifier_id(self):
        """Gets the last_modifier_id of this IdentityUserDto.  # noqa: E501


        :return: The last_modifier_id of this IdentityUserDto.  # noqa: E501
        :rtype: str
        """
        return self._last_modifier_id

    @last_modifier_id.setter
    def last_modifier_id(self, last_modifier_id):
        """Sets the last_modifier_id of this IdentityUserDto.


        :param last_modifier_id: The last_modifier_id of this IdentityUserDto.  # noqa: E501
        :type last_modifier_id: str
        """

        self._last_modifier_id = last_modifier_id

    @property
    def is_deleted(self):
        """Gets the is_deleted of this IdentityUserDto.  # noqa: E501


        :return: The is_deleted of this IdentityUserDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        """Sets the is_deleted of this IdentityUserDto.


        :param is_deleted: The is_deleted of this IdentityUserDto.  # noqa: E501
        :type is_deleted: bool
        """

        self._is_deleted = is_deleted

    @property
    def deleter_id(self):
        """Gets the deleter_id of this IdentityUserDto.  # noqa: E501


        :return: The deleter_id of this IdentityUserDto.  # noqa: E501
        :rtype: str
        """
        return self._deleter_id

    @deleter_id.setter
    def deleter_id(self, deleter_id):
        """Sets the deleter_id of this IdentityUserDto.


        :param deleter_id: The deleter_id of this IdentityUserDto.  # noqa: E501
        :type deleter_id: str
        """

        self._deleter_id = deleter_id

    @property
    def deletion_time(self):
        """Gets the deletion_time of this IdentityUserDto.  # noqa: E501


        :return: The deletion_time of this IdentityUserDto.  # noqa: E501
        :rtype: datetime
        """
        return self._deletion_time

    @deletion_time.setter
    def deletion_time(self, deletion_time):
        """Sets the deletion_time of this IdentityUserDto.


        :param deletion_time: The deletion_time of this IdentityUserDto.  # noqa: E501
        :type deletion_time: datetime
        """

        self._deletion_time = deletion_time

    @property
    def tenant_id(self):
        """Gets the tenant_id of this IdentityUserDto.  # noqa: E501


        :return: The tenant_id of this IdentityUserDto.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this IdentityUserDto.


        :param tenant_id: The tenant_id of this IdentityUserDto.  # noqa: E501
        :type tenant_id: str
        """

        self._tenant_id = tenant_id

    @property
    def user_name(self):
        """Gets the user_name of this IdentityUserDto.  # noqa: E501


        :return: The user_name of this IdentityUserDto.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this IdentityUserDto.


        :param user_name: The user_name of this IdentityUserDto.  # noqa: E501
        :type user_name: str
        """

        self._user_name = user_name

    @property
    def name(self):
        """Gets the name of this IdentityUserDto.  # noqa: E501


        :return: The name of this IdentityUserDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IdentityUserDto.


        :param name: The name of this IdentityUserDto.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def surname(self):
        """Gets the surname of this IdentityUserDto.  # noqa: E501


        :return: The surname of this IdentityUserDto.  # noqa: E501
        :rtype: str
        """
        return self._surname

    @surname.setter
    def surname(self, surname):
        """Sets the surname of this IdentityUserDto.


        :param surname: The surname of this IdentityUserDto.  # noqa: E501
        :type surname: str
        """

        self._surname = surname

    @property
    def email(self):
        """Gets the email of this IdentityUserDto.  # noqa: E501


        :return: The email of this IdentityUserDto.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this IdentityUserDto.


        :param email: The email of this IdentityUserDto.  # noqa: E501
        :type email: str
        """

        self._email = email

    @property
    def email_confirmed(self):
        """Gets the email_confirmed of this IdentityUserDto.  # noqa: E501


        :return: The email_confirmed of this IdentityUserDto.  # noqa: E501
        :rtype: bool
        """
        return self._email_confirmed

    @email_confirmed.setter
    def email_confirmed(self, email_confirmed):
        """Sets the email_confirmed of this IdentityUserDto.


        :param email_confirmed: The email_confirmed of this IdentityUserDto.  # noqa: E501
        :type email_confirmed: bool
        """

        self._email_confirmed = email_confirmed

    @property
    def phone_number(self):
        """Gets the phone_number of this IdentityUserDto.  # noqa: E501


        :return: The phone_number of this IdentityUserDto.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this IdentityUserDto.


        :param phone_number: The phone_number of this IdentityUserDto.  # noqa: E501
        :type phone_number: str
        """

        self._phone_number = phone_number

    @property
    def phone_number_confirmed(self):
        """Gets the phone_number_confirmed of this IdentityUserDto.  # noqa: E501


        :return: The phone_number_confirmed of this IdentityUserDto.  # noqa: E501
        :rtype: bool
        """
        return self._phone_number_confirmed

    @phone_number_confirmed.setter
    def phone_number_confirmed(self, phone_number_confirmed):
        """Sets the phone_number_confirmed of this IdentityUserDto.


        :param phone_number_confirmed: The phone_number_confirmed of this IdentityUserDto.  # noqa: E501
        :type phone_number_confirmed: bool
        """

        self._phone_number_confirmed = phone_number_confirmed

    @property
    def is_active(self):
        """Gets the is_active of this IdentityUserDto.  # noqa: E501


        :return: The is_active of this IdentityUserDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this IdentityUserDto.


        :param is_active: The is_active of this IdentityUserDto.  # noqa: E501
        :type is_active: bool
        """

        self._is_active = is_active

    @property
    def lockout_enabled(self):
        """Gets the lockout_enabled of this IdentityUserDto.  # noqa: E501


        :return: The lockout_enabled of this IdentityUserDto.  # noqa: E501
        :rtype: bool
        """
        return self._lockout_enabled

    @lockout_enabled.setter
    def lockout_enabled(self, lockout_enabled):
        """Sets the lockout_enabled of this IdentityUserDto.


        :param lockout_enabled: The lockout_enabled of this IdentityUserDto.  # noqa: E501
        :type lockout_enabled: bool
        """

        self._lockout_enabled = lockout_enabled

    @property
    def lockout_end(self):
        """Gets the lockout_end of this IdentityUserDto.  # noqa: E501


        :return: The lockout_end of this IdentityUserDto.  # noqa: E501
        :rtype: datetime
        """
        return self._lockout_end

    @lockout_end.setter
    def lockout_end(self, lockout_end):
        """Sets the lockout_end of this IdentityUserDto.


        :param lockout_end: The lockout_end of this IdentityUserDto.  # noqa: E501
        :type lockout_end: datetime
        """

        self._lockout_end = lockout_end

    @property
    def concurrency_stamp(self):
        """Gets the concurrency_stamp of this IdentityUserDto.  # noqa: E501


        :return: The concurrency_stamp of this IdentityUserDto.  # noqa: E501
        :rtype: str
        """
        return self._concurrency_stamp

    @concurrency_stamp.setter
    def concurrency_stamp(self, concurrency_stamp):
        """Sets the concurrency_stamp of this IdentityUserDto.


        :param concurrency_stamp: The concurrency_stamp of this IdentityUserDto.  # noqa: E501
        :type concurrency_stamp: str
        """

        self._concurrency_stamp = concurrency_stamp

    @property
    def entity_version(self):
        """Gets the entity_version of this IdentityUserDto.  # noqa: E501


        :return: The entity_version of this IdentityUserDto.  # noqa: E501
        :rtype: int
        """
        return self._entity_version

    @entity_version.setter
    def entity_version(self, entity_version):
        """Sets the entity_version of this IdentityUserDto.


        :param entity_version: The entity_version of this IdentityUserDto.  # noqa: E501
        :type entity_version: int
        """

        self._entity_version = entity_version

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
        if not isinstance(other, IdentityUserDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IdentityUserDto):
            return True

        return self.to_dict() != other.to_dict()