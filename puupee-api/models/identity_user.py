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


class IdentityUser(object):
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
        'extra_properties': 'dict[str, object]',
        'concurrency_stamp': 'str',
        'creation_time': 'datetime',
        'creator_id': 'str',
        'last_modification_time': 'datetime',
        'last_modifier_id': 'str',
        'is_deleted': 'bool',
        'deleter_id': 'str',
        'deletion_time': 'datetime',
        'tenant_id': 'str',
        'user_name': 'str',
        'normalized_user_name': 'str',
        'name': 'str',
        'surname': 'str',
        'email': 'str',
        'normalized_email': 'str',
        'email_confirmed': 'bool',
        'password_hash': 'str',
        'security_stamp': 'str',
        'is_external': 'bool',
        'phone_number': 'str',
        'phone_number_confirmed': 'bool',
        'is_active': 'bool',
        'two_factor_enabled': 'bool',
        'lockout_end': 'datetime',
        'lockout_enabled': 'bool',
        'access_failed_count': 'int',
        'should_change_password_on_next_login': 'bool',
        'entity_version': 'int',
        'last_password_change_time': 'datetime',
        'roles': 'list[IdentityUserRole]',
        'claims': 'list[IdentityUserClaim]',
        'logins': 'list[IdentityUserLogin]',
        'tokens': 'list[IdentityUserToken]',
        'organization_units': 'list[IdentityUserOrganizationUnit]'
    }

    attribute_map = {
        'id': 'id',
        'extra_properties': 'extraProperties',
        'concurrency_stamp': 'concurrencyStamp',
        'creation_time': 'creationTime',
        'creator_id': 'creatorId',
        'last_modification_time': 'lastModificationTime',
        'last_modifier_id': 'lastModifierId',
        'is_deleted': 'isDeleted',
        'deleter_id': 'deleterId',
        'deletion_time': 'deletionTime',
        'tenant_id': 'tenantId',
        'user_name': 'userName',
        'normalized_user_name': 'normalizedUserName',
        'name': 'name',
        'surname': 'surname',
        'email': 'email',
        'normalized_email': 'normalizedEmail',
        'email_confirmed': 'emailConfirmed',
        'password_hash': 'passwordHash',
        'security_stamp': 'securityStamp',
        'is_external': 'isExternal',
        'phone_number': 'phoneNumber',
        'phone_number_confirmed': 'phoneNumberConfirmed',
        'is_active': 'isActive',
        'two_factor_enabled': 'twoFactorEnabled',
        'lockout_end': 'lockoutEnd',
        'lockout_enabled': 'lockoutEnabled',
        'access_failed_count': 'accessFailedCount',
        'should_change_password_on_next_login': 'shouldChangePasswordOnNextLogin',
        'entity_version': 'entityVersion',
        'last_password_change_time': 'lastPasswordChangeTime',
        'roles': 'roles',
        'claims': 'claims',
        'logins': 'logins',
        'tokens': 'tokens',
        'organization_units': 'organizationUnits'
    }

    def __init__(self, id=None, extra_properties=None, concurrency_stamp=None, creation_time=None, creator_id=None, last_modification_time=None, last_modifier_id=None, is_deleted=None, deleter_id=None, deletion_time=None, tenant_id=None, user_name=None, normalized_user_name=None, name=None, surname=None, email=None, normalized_email=None, email_confirmed=None, password_hash=None, security_stamp=None, is_external=None, phone_number=None, phone_number_confirmed=None, is_active=None, two_factor_enabled=None, lockout_end=None, lockout_enabled=None, access_failed_count=None, should_change_password_on_next_login=None, entity_version=None, last_password_change_time=None, roles=None, claims=None, logins=None, tokens=None, organization_units=None, local_vars_configuration=None):  # noqa: E501
        """IdentityUser - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._extra_properties = None
        self._concurrency_stamp = None
        self._creation_time = None
        self._creator_id = None
        self._last_modification_time = None
        self._last_modifier_id = None
        self._is_deleted = None
        self._deleter_id = None
        self._deletion_time = None
        self._tenant_id = None
        self._user_name = None
        self._normalized_user_name = None
        self._name = None
        self._surname = None
        self._email = None
        self._normalized_email = None
        self._email_confirmed = None
        self._password_hash = None
        self._security_stamp = None
        self._is_external = None
        self._phone_number = None
        self._phone_number_confirmed = None
        self._is_active = None
        self._two_factor_enabled = None
        self._lockout_end = None
        self._lockout_enabled = None
        self._access_failed_count = None
        self._should_change_password_on_next_login = None
        self._entity_version = None
        self._last_password_change_time = None
        self._roles = None
        self._claims = None
        self._logins = None
        self._tokens = None
        self._organization_units = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.extra_properties = extra_properties
        self.concurrency_stamp = concurrency_stamp
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
        self.normalized_user_name = normalized_user_name
        self.name = name
        self.surname = surname
        self.email = email
        self.normalized_email = normalized_email
        if email_confirmed is not None:
            self.email_confirmed = email_confirmed
        self.password_hash = password_hash
        self.security_stamp = security_stamp
        if is_external is not None:
            self.is_external = is_external
        self.phone_number = phone_number
        if phone_number_confirmed is not None:
            self.phone_number_confirmed = phone_number_confirmed
        if is_active is not None:
            self.is_active = is_active
        if two_factor_enabled is not None:
            self.two_factor_enabled = two_factor_enabled
        self.lockout_end = lockout_end
        if lockout_enabled is not None:
            self.lockout_enabled = lockout_enabled
        if access_failed_count is not None:
            self.access_failed_count = access_failed_count
        if should_change_password_on_next_login is not None:
            self.should_change_password_on_next_login = should_change_password_on_next_login
        if entity_version is not None:
            self.entity_version = entity_version
        self.last_password_change_time = last_password_change_time
        self.roles = roles
        self.claims = claims
        self.logins = logins
        self.tokens = tokens
        self.organization_units = organization_units

    @property
    def id(self):
        """Gets the id of this IdentityUser.  # noqa: E501


        :return: The id of this IdentityUser.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IdentityUser.


        :param id: The id of this IdentityUser.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def extra_properties(self):
        """Gets the extra_properties of this IdentityUser.  # noqa: E501


        :return: The extra_properties of this IdentityUser.  # noqa: E501
        :rtype: dict[str, object]
        """
        return self._extra_properties

    @extra_properties.setter
    def extra_properties(self, extra_properties):
        """Sets the extra_properties of this IdentityUser.


        :param extra_properties: The extra_properties of this IdentityUser.  # noqa: E501
        :type extra_properties: dict[str, object]
        """

        self._extra_properties = extra_properties

    @property
    def concurrency_stamp(self):
        """Gets the concurrency_stamp of this IdentityUser.  # noqa: E501


        :return: The concurrency_stamp of this IdentityUser.  # noqa: E501
        :rtype: str
        """
        return self._concurrency_stamp

    @concurrency_stamp.setter
    def concurrency_stamp(self, concurrency_stamp):
        """Sets the concurrency_stamp of this IdentityUser.


        :param concurrency_stamp: The concurrency_stamp of this IdentityUser.  # noqa: E501
        :type concurrency_stamp: str
        """

        self._concurrency_stamp = concurrency_stamp

    @property
    def creation_time(self):
        """Gets the creation_time of this IdentityUser.  # noqa: E501


        :return: The creation_time of this IdentityUser.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this IdentityUser.


        :param creation_time: The creation_time of this IdentityUser.  # noqa: E501
        :type creation_time: datetime
        """

        self._creation_time = creation_time

    @property
    def creator_id(self):
        """Gets the creator_id of this IdentityUser.  # noqa: E501


        :return: The creator_id of this IdentityUser.  # noqa: E501
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this IdentityUser.


        :param creator_id: The creator_id of this IdentityUser.  # noqa: E501
        :type creator_id: str
        """

        self._creator_id = creator_id

    @property
    def last_modification_time(self):
        """Gets the last_modification_time of this IdentityUser.  # noqa: E501


        :return: The last_modification_time of this IdentityUser.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modification_time

    @last_modification_time.setter
    def last_modification_time(self, last_modification_time):
        """Sets the last_modification_time of this IdentityUser.


        :param last_modification_time: The last_modification_time of this IdentityUser.  # noqa: E501
        :type last_modification_time: datetime
        """

        self._last_modification_time = last_modification_time

    @property
    def last_modifier_id(self):
        """Gets the last_modifier_id of this IdentityUser.  # noqa: E501


        :return: The last_modifier_id of this IdentityUser.  # noqa: E501
        :rtype: str
        """
        return self._last_modifier_id

    @last_modifier_id.setter
    def last_modifier_id(self, last_modifier_id):
        """Sets the last_modifier_id of this IdentityUser.


        :param last_modifier_id: The last_modifier_id of this IdentityUser.  # noqa: E501
        :type last_modifier_id: str
        """

        self._last_modifier_id = last_modifier_id

    @property
    def is_deleted(self):
        """Gets the is_deleted of this IdentityUser.  # noqa: E501


        :return: The is_deleted of this IdentityUser.  # noqa: E501
        :rtype: bool
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        """Sets the is_deleted of this IdentityUser.


        :param is_deleted: The is_deleted of this IdentityUser.  # noqa: E501
        :type is_deleted: bool
        """

        self._is_deleted = is_deleted

    @property
    def deleter_id(self):
        """Gets the deleter_id of this IdentityUser.  # noqa: E501


        :return: The deleter_id of this IdentityUser.  # noqa: E501
        :rtype: str
        """
        return self._deleter_id

    @deleter_id.setter
    def deleter_id(self, deleter_id):
        """Sets the deleter_id of this IdentityUser.


        :param deleter_id: The deleter_id of this IdentityUser.  # noqa: E501
        :type deleter_id: str
        """

        self._deleter_id = deleter_id

    @property
    def deletion_time(self):
        """Gets the deletion_time of this IdentityUser.  # noqa: E501


        :return: The deletion_time of this IdentityUser.  # noqa: E501
        :rtype: datetime
        """
        return self._deletion_time

    @deletion_time.setter
    def deletion_time(self, deletion_time):
        """Sets the deletion_time of this IdentityUser.


        :param deletion_time: The deletion_time of this IdentityUser.  # noqa: E501
        :type deletion_time: datetime
        """

        self._deletion_time = deletion_time

    @property
    def tenant_id(self):
        """Gets the tenant_id of this IdentityUser.  # noqa: E501


        :return: The tenant_id of this IdentityUser.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this IdentityUser.


        :param tenant_id: The tenant_id of this IdentityUser.  # noqa: E501
        :type tenant_id: str
        """

        self._tenant_id = tenant_id

    @property
    def user_name(self):
        """Gets the user_name of this IdentityUser.  # noqa: E501


        :return: The user_name of this IdentityUser.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this IdentityUser.


        :param user_name: The user_name of this IdentityUser.  # noqa: E501
        :type user_name: str
        """

        self._user_name = user_name

    @property
    def normalized_user_name(self):
        """Gets the normalized_user_name of this IdentityUser.  # noqa: E501


        :return: The normalized_user_name of this IdentityUser.  # noqa: E501
        :rtype: str
        """
        return self._normalized_user_name

    @normalized_user_name.setter
    def normalized_user_name(self, normalized_user_name):
        """Sets the normalized_user_name of this IdentityUser.


        :param normalized_user_name: The normalized_user_name of this IdentityUser.  # noqa: E501
        :type normalized_user_name: str
        """

        self._normalized_user_name = normalized_user_name

    @property
    def name(self):
        """Gets the name of this IdentityUser.  # noqa: E501


        :return: The name of this IdentityUser.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IdentityUser.


        :param name: The name of this IdentityUser.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def surname(self):
        """Gets the surname of this IdentityUser.  # noqa: E501


        :return: The surname of this IdentityUser.  # noqa: E501
        :rtype: str
        """
        return self._surname

    @surname.setter
    def surname(self, surname):
        """Sets the surname of this IdentityUser.


        :param surname: The surname of this IdentityUser.  # noqa: E501
        :type surname: str
        """

        self._surname = surname

    @property
    def email(self):
        """Gets the email of this IdentityUser.  # noqa: E501


        :return: The email of this IdentityUser.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this IdentityUser.


        :param email: The email of this IdentityUser.  # noqa: E501
        :type email: str
        """

        self._email = email

    @property
    def normalized_email(self):
        """Gets the normalized_email of this IdentityUser.  # noqa: E501


        :return: The normalized_email of this IdentityUser.  # noqa: E501
        :rtype: str
        """
        return self._normalized_email

    @normalized_email.setter
    def normalized_email(self, normalized_email):
        """Sets the normalized_email of this IdentityUser.


        :param normalized_email: The normalized_email of this IdentityUser.  # noqa: E501
        :type normalized_email: str
        """

        self._normalized_email = normalized_email

    @property
    def email_confirmed(self):
        """Gets the email_confirmed of this IdentityUser.  # noqa: E501


        :return: The email_confirmed of this IdentityUser.  # noqa: E501
        :rtype: bool
        """
        return self._email_confirmed

    @email_confirmed.setter
    def email_confirmed(self, email_confirmed):
        """Sets the email_confirmed of this IdentityUser.


        :param email_confirmed: The email_confirmed of this IdentityUser.  # noqa: E501
        :type email_confirmed: bool
        """

        self._email_confirmed = email_confirmed

    @property
    def password_hash(self):
        """Gets the password_hash of this IdentityUser.  # noqa: E501


        :return: The password_hash of this IdentityUser.  # noqa: E501
        :rtype: str
        """
        return self._password_hash

    @password_hash.setter
    def password_hash(self, password_hash):
        """Sets the password_hash of this IdentityUser.


        :param password_hash: The password_hash of this IdentityUser.  # noqa: E501
        :type password_hash: str
        """

        self._password_hash = password_hash

    @property
    def security_stamp(self):
        """Gets the security_stamp of this IdentityUser.  # noqa: E501


        :return: The security_stamp of this IdentityUser.  # noqa: E501
        :rtype: str
        """
        return self._security_stamp

    @security_stamp.setter
    def security_stamp(self, security_stamp):
        """Sets the security_stamp of this IdentityUser.


        :param security_stamp: The security_stamp of this IdentityUser.  # noqa: E501
        :type security_stamp: str
        """

        self._security_stamp = security_stamp

    @property
    def is_external(self):
        """Gets the is_external of this IdentityUser.  # noqa: E501


        :return: The is_external of this IdentityUser.  # noqa: E501
        :rtype: bool
        """
        return self._is_external

    @is_external.setter
    def is_external(self, is_external):
        """Sets the is_external of this IdentityUser.


        :param is_external: The is_external of this IdentityUser.  # noqa: E501
        :type is_external: bool
        """

        self._is_external = is_external

    @property
    def phone_number(self):
        """Gets the phone_number of this IdentityUser.  # noqa: E501


        :return: The phone_number of this IdentityUser.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this IdentityUser.


        :param phone_number: The phone_number of this IdentityUser.  # noqa: E501
        :type phone_number: str
        """

        self._phone_number = phone_number

    @property
    def phone_number_confirmed(self):
        """Gets the phone_number_confirmed of this IdentityUser.  # noqa: E501


        :return: The phone_number_confirmed of this IdentityUser.  # noqa: E501
        :rtype: bool
        """
        return self._phone_number_confirmed

    @phone_number_confirmed.setter
    def phone_number_confirmed(self, phone_number_confirmed):
        """Sets the phone_number_confirmed of this IdentityUser.


        :param phone_number_confirmed: The phone_number_confirmed of this IdentityUser.  # noqa: E501
        :type phone_number_confirmed: bool
        """

        self._phone_number_confirmed = phone_number_confirmed

    @property
    def is_active(self):
        """Gets the is_active of this IdentityUser.  # noqa: E501


        :return: The is_active of this IdentityUser.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this IdentityUser.


        :param is_active: The is_active of this IdentityUser.  # noqa: E501
        :type is_active: bool
        """

        self._is_active = is_active

    @property
    def two_factor_enabled(self):
        """Gets the two_factor_enabled of this IdentityUser.  # noqa: E501


        :return: The two_factor_enabled of this IdentityUser.  # noqa: E501
        :rtype: bool
        """
        return self._two_factor_enabled

    @two_factor_enabled.setter
    def two_factor_enabled(self, two_factor_enabled):
        """Sets the two_factor_enabled of this IdentityUser.


        :param two_factor_enabled: The two_factor_enabled of this IdentityUser.  # noqa: E501
        :type two_factor_enabled: bool
        """

        self._two_factor_enabled = two_factor_enabled

    @property
    def lockout_end(self):
        """Gets the lockout_end of this IdentityUser.  # noqa: E501


        :return: The lockout_end of this IdentityUser.  # noqa: E501
        :rtype: datetime
        """
        return self._lockout_end

    @lockout_end.setter
    def lockout_end(self, lockout_end):
        """Sets the lockout_end of this IdentityUser.


        :param lockout_end: The lockout_end of this IdentityUser.  # noqa: E501
        :type lockout_end: datetime
        """

        self._lockout_end = lockout_end

    @property
    def lockout_enabled(self):
        """Gets the lockout_enabled of this IdentityUser.  # noqa: E501


        :return: The lockout_enabled of this IdentityUser.  # noqa: E501
        :rtype: bool
        """
        return self._lockout_enabled

    @lockout_enabled.setter
    def lockout_enabled(self, lockout_enabled):
        """Sets the lockout_enabled of this IdentityUser.


        :param lockout_enabled: The lockout_enabled of this IdentityUser.  # noqa: E501
        :type lockout_enabled: bool
        """

        self._lockout_enabled = lockout_enabled

    @property
    def access_failed_count(self):
        """Gets the access_failed_count of this IdentityUser.  # noqa: E501


        :return: The access_failed_count of this IdentityUser.  # noqa: E501
        :rtype: int
        """
        return self._access_failed_count

    @access_failed_count.setter
    def access_failed_count(self, access_failed_count):
        """Sets the access_failed_count of this IdentityUser.


        :param access_failed_count: The access_failed_count of this IdentityUser.  # noqa: E501
        :type access_failed_count: int
        """

        self._access_failed_count = access_failed_count

    @property
    def should_change_password_on_next_login(self):
        """Gets the should_change_password_on_next_login of this IdentityUser.  # noqa: E501


        :return: The should_change_password_on_next_login of this IdentityUser.  # noqa: E501
        :rtype: bool
        """
        return self._should_change_password_on_next_login

    @should_change_password_on_next_login.setter
    def should_change_password_on_next_login(self, should_change_password_on_next_login):
        """Sets the should_change_password_on_next_login of this IdentityUser.


        :param should_change_password_on_next_login: The should_change_password_on_next_login of this IdentityUser.  # noqa: E501
        :type should_change_password_on_next_login: bool
        """

        self._should_change_password_on_next_login = should_change_password_on_next_login

    @property
    def entity_version(self):
        """Gets the entity_version of this IdentityUser.  # noqa: E501


        :return: The entity_version of this IdentityUser.  # noqa: E501
        :rtype: int
        """
        return self._entity_version

    @entity_version.setter
    def entity_version(self, entity_version):
        """Sets the entity_version of this IdentityUser.


        :param entity_version: The entity_version of this IdentityUser.  # noqa: E501
        :type entity_version: int
        """

        self._entity_version = entity_version

    @property
    def last_password_change_time(self):
        """Gets the last_password_change_time of this IdentityUser.  # noqa: E501


        :return: The last_password_change_time of this IdentityUser.  # noqa: E501
        :rtype: datetime
        """
        return self._last_password_change_time

    @last_password_change_time.setter
    def last_password_change_time(self, last_password_change_time):
        """Sets the last_password_change_time of this IdentityUser.


        :param last_password_change_time: The last_password_change_time of this IdentityUser.  # noqa: E501
        :type last_password_change_time: datetime
        """

        self._last_password_change_time = last_password_change_time

    @property
    def roles(self):
        """Gets the roles of this IdentityUser.  # noqa: E501


        :return: The roles of this IdentityUser.  # noqa: E501
        :rtype: list[IdentityUserRole]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this IdentityUser.


        :param roles: The roles of this IdentityUser.  # noqa: E501
        :type roles: list[IdentityUserRole]
        """

        self._roles = roles

    @property
    def claims(self):
        """Gets the claims of this IdentityUser.  # noqa: E501


        :return: The claims of this IdentityUser.  # noqa: E501
        :rtype: list[IdentityUserClaim]
        """
        return self._claims

    @claims.setter
    def claims(self, claims):
        """Sets the claims of this IdentityUser.


        :param claims: The claims of this IdentityUser.  # noqa: E501
        :type claims: list[IdentityUserClaim]
        """

        self._claims = claims

    @property
    def logins(self):
        """Gets the logins of this IdentityUser.  # noqa: E501


        :return: The logins of this IdentityUser.  # noqa: E501
        :rtype: list[IdentityUserLogin]
        """
        return self._logins

    @logins.setter
    def logins(self, logins):
        """Sets the logins of this IdentityUser.


        :param logins: The logins of this IdentityUser.  # noqa: E501
        :type logins: list[IdentityUserLogin]
        """

        self._logins = logins

    @property
    def tokens(self):
        """Gets the tokens of this IdentityUser.  # noqa: E501


        :return: The tokens of this IdentityUser.  # noqa: E501
        :rtype: list[IdentityUserToken]
        """
        return self._tokens

    @tokens.setter
    def tokens(self, tokens):
        """Sets the tokens of this IdentityUser.


        :param tokens: The tokens of this IdentityUser.  # noqa: E501
        :type tokens: list[IdentityUserToken]
        """

        self._tokens = tokens

    @property
    def organization_units(self):
        """Gets the organization_units of this IdentityUser.  # noqa: E501


        :return: The organization_units of this IdentityUser.  # noqa: E501
        :rtype: list[IdentityUserOrganizationUnit]
        """
        return self._organization_units

    @organization_units.setter
    def organization_units(self, organization_units):
        """Sets the organization_units of this IdentityUser.


        :param organization_units: The organization_units of this IdentityUser.  # noqa: E501
        :type organization_units: list[IdentityUserOrganizationUnit]
        """

        self._organization_units = organization_units

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
        if not isinstance(other, IdentityUser):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IdentityUser):
            return True

        return self.to_dict() != other.to_dict()
