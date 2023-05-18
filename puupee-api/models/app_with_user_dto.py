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


class AppWithUserDto(object):
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
        'display_name': 'str',
        'framework': 'str',
        'app_type': 'str',
        'description': 'str',
        'icon': 'str',
        'home_page': 'str',
        'sort_index': 'int',
        'git_repository': 'str',
        'git_repository_type': 'str',
        'is_enabled': 'bool',
        'is_published': 'bool',
        'webhook_url': 'str',
        'business_domain': 'str',
        'business_url': 'str',
        'subscription_platforms': 'str',
        'free_platforms': 'str',
        'spec_json_schema': 'str',
        'latest_releases': 'list[AppReleaseDto]',
        'creator': 'IdentityUserDto',
        'features': 'list[AppFeatureDto]',
        'sdks': 'list[AppSdkDto]',
        'subscribed': 'bool'
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
        'display_name': 'displayName',
        'framework': 'framework',
        'app_type': 'appType',
        'description': 'description',
        'icon': 'icon',
        'home_page': 'homePage',
        'sort_index': 'sortIndex',
        'git_repository': 'gitRepository',
        'git_repository_type': 'gitRepositoryType',
        'is_enabled': 'isEnabled',
        'is_published': 'isPublished',
        'webhook_url': 'webhookUrl',
        'business_domain': 'businessDomain',
        'business_url': 'businessUrl',
        'subscription_platforms': 'subscriptionPlatforms',
        'free_platforms': 'freePlatforms',
        'spec_json_schema': 'specJsonSchema',
        'latest_releases': 'latestReleases',
        'creator': 'creator',
        'features': 'features',
        'sdks': 'sdks',
        'subscribed': 'subscribed'
    }

    def __init__(self, id=None, creation_time=None, creator_id=None, last_modification_time=None, last_modifier_id=None, is_deleted=None, deleter_id=None, deletion_time=None, name=None, display_name=None, framework=None, app_type=None, description=None, icon=None, home_page=None, sort_index=None, git_repository=None, git_repository_type=None, is_enabled=None, is_published=None, webhook_url=None, business_domain=None, business_url=None, subscription_platforms=None, free_platforms=None, spec_json_schema=None, latest_releases=None, creator=None, features=None, sdks=None, subscribed=None, local_vars_configuration=None):  # noqa: E501
        """AppWithUserDto - a model defined in OpenAPI"""  # noqa: E501
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
        self._display_name = None
        self._framework = None
        self._app_type = None
        self._description = None
        self._icon = None
        self._home_page = None
        self._sort_index = None
        self._git_repository = None
        self._git_repository_type = None
        self._is_enabled = None
        self._is_published = None
        self._webhook_url = None
        self._business_domain = None
        self._business_url = None
        self._subscription_platforms = None
        self._free_platforms = None
        self._spec_json_schema = None
        self._latest_releases = None
        self._creator = None
        self._features = None
        self._sdks = None
        self._subscribed = None
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
        self.display_name = display_name
        self.framework = framework
        self.app_type = app_type
        self.description = description
        self.icon = icon
        self.home_page = home_page
        if sort_index is not None:
            self.sort_index = sort_index
        self.git_repository = git_repository
        self.git_repository_type = git_repository_type
        if is_enabled is not None:
            self.is_enabled = is_enabled
        if is_published is not None:
            self.is_published = is_published
        self.webhook_url = webhook_url
        self.business_domain = business_domain
        self.business_url = business_url
        self.subscription_platforms = subscription_platforms
        self.free_platforms = free_platforms
        self.spec_json_schema = spec_json_schema
        self.latest_releases = latest_releases
        if creator is not None:
            self.creator = creator
        self.features = features
        self.sdks = sdks
        if subscribed is not None:
            self.subscribed = subscribed

    @property
    def id(self):
        """Gets the id of this AppWithUserDto.  # noqa: E501


        :return: The id of this AppWithUserDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AppWithUserDto.


        :param id: The id of this AppWithUserDto.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def creation_time(self):
        """Gets the creation_time of this AppWithUserDto.  # noqa: E501


        :return: The creation_time of this AppWithUserDto.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this AppWithUserDto.


        :param creation_time: The creation_time of this AppWithUserDto.  # noqa: E501
        :type creation_time: datetime
        """

        self._creation_time = creation_time

    @property
    def creator_id(self):
        """Gets the creator_id of this AppWithUserDto.  # noqa: E501


        :return: The creator_id of this AppWithUserDto.  # noqa: E501
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this AppWithUserDto.


        :param creator_id: The creator_id of this AppWithUserDto.  # noqa: E501
        :type creator_id: str
        """

        self._creator_id = creator_id

    @property
    def last_modification_time(self):
        """Gets the last_modification_time of this AppWithUserDto.  # noqa: E501


        :return: The last_modification_time of this AppWithUserDto.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modification_time

    @last_modification_time.setter
    def last_modification_time(self, last_modification_time):
        """Sets the last_modification_time of this AppWithUserDto.


        :param last_modification_time: The last_modification_time of this AppWithUserDto.  # noqa: E501
        :type last_modification_time: datetime
        """

        self._last_modification_time = last_modification_time

    @property
    def last_modifier_id(self):
        """Gets the last_modifier_id of this AppWithUserDto.  # noqa: E501


        :return: The last_modifier_id of this AppWithUserDto.  # noqa: E501
        :rtype: str
        """
        return self._last_modifier_id

    @last_modifier_id.setter
    def last_modifier_id(self, last_modifier_id):
        """Sets the last_modifier_id of this AppWithUserDto.


        :param last_modifier_id: The last_modifier_id of this AppWithUserDto.  # noqa: E501
        :type last_modifier_id: str
        """

        self._last_modifier_id = last_modifier_id

    @property
    def is_deleted(self):
        """Gets the is_deleted of this AppWithUserDto.  # noqa: E501


        :return: The is_deleted of this AppWithUserDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        """Sets the is_deleted of this AppWithUserDto.


        :param is_deleted: The is_deleted of this AppWithUserDto.  # noqa: E501
        :type is_deleted: bool
        """

        self._is_deleted = is_deleted

    @property
    def deleter_id(self):
        """Gets the deleter_id of this AppWithUserDto.  # noqa: E501


        :return: The deleter_id of this AppWithUserDto.  # noqa: E501
        :rtype: str
        """
        return self._deleter_id

    @deleter_id.setter
    def deleter_id(self, deleter_id):
        """Sets the deleter_id of this AppWithUserDto.


        :param deleter_id: The deleter_id of this AppWithUserDto.  # noqa: E501
        :type deleter_id: str
        """

        self._deleter_id = deleter_id

    @property
    def deletion_time(self):
        """Gets the deletion_time of this AppWithUserDto.  # noqa: E501


        :return: The deletion_time of this AppWithUserDto.  # noqa: E501
        :rtype: datetime
        """
        return self._deletion_time

    @deletion_time.setter
    def deletion_time(self, deletion_time):
        """Sets the deletion_time of this AppWithUserDto.


        :param deletion_time: The deletion_time of this AppWithUserDto.  # noqa: E501
        :type deletion_time: datetime
        """

        self._deletion_time = deletion_time

    @property
    def name(self):
        """Gets the name of this AppWithUserDto.  # noqa: E501


        :return: The name of this AppWithUserDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AppWithUserDto.


        :param name: The name of this AppWithUserDto.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def display_name(self):
        """Gets the display_name of this AppWithUserDto.  # noqa: E501


        :return: The display_name of this AppWithUserDto.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this AppWithUserDto.


        :param display_name: The display_name of this AppWithUserDto.  # noqa: E501
        :type display_name: str
        """

        self._display_name = display_name

    @property
    def framework(self):
        """Gets the framework of this AppWithUserDto.  # noqa: E501


        :return: The framework of this AppWithUserDto.  # noqa: E501
        :rtype: str
        """
        return self._framework

    @framework.setter
    def framework(self, framework):
        """Sets the framework of this AppWithUserDto.


        :param framework: The framework of this AppWithUserDto.  # noqa: E501
        :type framework: str
        """

        self._framework = framework

    @property
    def app_type(self):
        """Gets the app_type of this AppWithUserDto.  # noqa: E501


        :return: The app_type of this AppWithUserDto.  # noqa: E501
        :rtype: str
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        """Sets the app_type of this AppWithUserDto.


        :param app_type: The app_type of this AppWithUserDto.  # noqa: E501
        :type app_type: str
        """

        self._app_type = app_type

    @property
    def description(self):
        """Gets the description of this AppWithUserDto.  # noqa: E501


        :return: The description of this AppWithUserDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AppWithUserDto.


        :param description: The description of this AppWithUserDto.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def icon(self):
        """Gets the icon of this AppWithUserDto.  # noqa: E501


        :return: The icon of this AppWithUserDto.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this AppWithUserDto.


        :param icon: The icon of this AppWithUserDto.  # noqa: E501
        :type icon: str
        """

        self._icon = icon

    @property
    def home_page(self):
        """Gets the home_page of this AppWithUserDto.  # noqa: E501


        :return: The home_page of this AppWithUserDto.  # noqa: E501
        :rtype: str
        """
        return self._home_page

    @home_page.setter
    def home_page(self, home_page):
        """Sets the home_page of this AppWithUserDto.


        :param home_page: The home_page of this AppWithUserDto.  # noqa: E501
        :type home_page: str
        """

        self._home_page = home_page

    @property
    def sort_index(self):
        """Gets the sort_index of this AppWithUserDto.  # noqa: E501


        :return: The sort_index of this AppWithUserDto.  # noqa: E501
        :rtype: int
        """
        return self._sort_index

    @sort_index.setter
    def sort_index(self, sort_index):
        """Sets the sort_index of this AppWithUserDto.


        :param sort_index: The sort_index of this AppWithUserDto.  # noqa: E501
        :type sort_index: int
        """

        self._sort_index = sort_index

    @property
    def git_repository(self):
        """Gets the git_repository of this AppWithUserDto.  # noqa: E501


        :return: The git_repository of this AppWithUserDto.  # noqa: E501
        :rtype: str
        """
        return self._git_repository

    @git_repository.setter
    def git_repository(self, git_repository):
        """Sets the git_repository of this AppWithUserDto.


        :param git_repository: The git_repository of this AppWithUserDto.  # noqa: E501
        :type git_repository: str
        """

        self._git_repository = git_repository

    @property
    def git_repository_type(self):
        """Gets the git_repository_type of this AppWithUserDto.  # noqa: E501


        :return: The git_repository_type of this AppWithUserDto.  # noqa: E501
        :rtype: str
        """
        return self._git_repository_type

    @git_repository_type.setter
    def git_repository_type(self, git_repository_type):
        """Sets the git_repository_type of this AppWithUserDto.


        :param git_repository_type: The git_repository_type of this AppWithUserDto.  # noqa: E501
        :type git_repository_type: str
        """

        self._git_repository_type = git_repository_type

    @property
    def is_enabled(self):
        """Gets the is_enabled of this AppWithUserDto.  # noqa: E501


        :return: The is_enabled of this AppWithUserDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """Sets the is_enabled of this AppWithUserDto.


        :param is_enabled: The is_enabled of this AppWithUserDto.  # noqa: E501
        :type is_enabled: bool
        """

        self._is_enabled = is_enabled

    @property
    def is_published(self):
        """Gets the is_published of this AppWithUserDto.  # noqa: E501


        :return: The is_published of this AppWithUserDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_published

    @is_published.setter
    def is_published(self, is_published):
        """Sets the is_published of this AppWithUserDto.


        :param is_published: The is_published of this AppWithUserDto.  # noqa: E501
        :type is_published: bool
        """

        self._is_published = is_published

    @property
    def webhook_url(self):
        """Gets the webhook_url of this AppWithUserDto.  # noqa: E501


        :return: The webhook_url of this AppWithUserDto.  # noqa: E501
        :rtype: str
        """
        return self._webhook_url

    @webhook_url.setter
    def webhook_url(self, webhook_url):
        """Sets the webhook_url of this AppWithUserDto.


        :param webhook_url: The webhook_url of this AppWithUserDto.  # noqa: E501
        :type webhook_url: str
        """

        self._webhook_url = webhook_url

    @property
    def business_domain(self):
        """Gets the business_domain of this AppWithUserDto.  # noqa: E501


        :return: The business_domain of this AppWithUserDto.  # noqa: E501
        :rtype: str
        """
        return self._business_domain

    @business_domain.setter
    def business_domain(self, business_domain):
        """Sets the business_domain of this AppWithUserDto.


        :param business_domain: The business_domain of this AppWithUserDto.  # noqa: E501
        :type business_domain: str
        """

        self._business_domain = business_domain

    @property
    def business_url(self):
        """Gets the business_url of this AppWithUserDto.  # noqa: E501


        :return: The business_url of this AppWithUserDto.  # noqa: E501
        :rtype: str
        """
        return self._business_url

    @business_url.setter
    def business_url(self, business_url):
        """Sets the business_url of this AppWithUserDto.


        :param business_url: The business_url of this AppWithUserDto.  # noqa: E501
        :type business_url: str
        """

        self._business_url = business_url

    @property
    def subscription_platforms(self):
        """Gets the subscription_platforms of this AppWithUserDto.  # noqa: E501


        :return: The subscription_platforms of this AppWithUserDto.  # noqa: E501
        :rtype: str
        """
        return self._subscription_platforms

    @subscription_platforms.setter
    def subscription_platforms(self, subscription_platforms):
        """Sets the subscription_platforms of this AppWithUserDto.


        :param subscription_platforms: The subscription_platforms of this AppWithUserDto.  # noqa: E501
        :type subscription_platforms: str
        """

        self._subscription_platforms = subscription_platforms

    @property
    def free_platforms(self):
        """Gets the free_platforms of this AppWithUserDto.  # noqa: E501


        :return: The free_platforms of this AppWithUserDto.  # noqa: E501
        :rtype: str
        """
        return self._free_platforms

    @free_platforms.setter
    def free_platforms(self, free_platforms):
        """Sets the free_platforms of this AppWithUserDto.


        :param free_platforms: The free_platforms of this AppWithUserDto.  # noqa: E501
        :type free_platforms: str
        """

        self._free_platforms = free_platforms

    @property
    def spec_json_schema(self):
        """Gets the spec_json_schema of this AppWithUserDto.  # noqa: E501


        :return: The spec_json_schema of this AppWithUserDto.  # noqa: E501
        :rtype: str
        """
        return self._spec_json_schema

    @spec_json_schema.setter
    def spec_json_schema(self, spec_json_schema):
        """Sets the spec_json_schema of this AppWithUserDto.


        :param spec_json_schema: The spec_json_schema of this AppWithUserDto.  # noqa: E501
        :type spec_json_schema: str
        """

        self._spec_json_schema = spec_json_schema

    @property
    def latest_releases(self):
        """Gets the latest_releases of this AppWithUserDto.  # noqa: E501


        :return: The latest_releases of this AppWithUserDto.  # noqa: E501
        :rtype: list[AppReleaseDto]
        """
        return self._latest_releases

    @latest_releases.setter
    def latest_releases(self, latest_releases):
        """Sets the latest_releases of this AppWithUserDto.


        :param latest_releases: The latest_releases of this AppWithUserDto.  # noqa: E501
        :type latest_releases: list[AppReleaseDto]
        """

        self._latest_releases = latest_releases

    @property
    def creator(self):
        """Gets the creator of this AppWithUserDto.  # noqa: E501


        :return: The creator of this AppWithUserDto.  # noqa: E501
        :rtype: IdentityUserDto
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this AppWithUserDto.


        :param creator: The creator of this AppWithUserDto.  # noqa: E501
        :type creator: IdentityUserDto
        """

        self._creator = creator

    @property
    def features(self):
        """Gets the features of this AppWithUserDto.  # noqa: E501


        :return: The features of this AppWithUserDto.  # noqa: E501
        :rtype: list[AppFeatureDto]
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this AppWithUserDto.


        :param features: The features of this AppWithUserDto.  # noqa: E501
        :type features: list[AppFeatureDto]
        """

        self._features = features

    @property
    def sdks(self):
        """Gets the sdks of this AppWithUserDto.  # noqa: E501


        :return: The sdks of this AppWithUserDto.  # noqa: E501
        :rtype: list[AppSdkDto]
        """
        return self._sdks

    @sdks.setter
    def sdks(self, sdks):
        """Sets the sdks of this AppWithUserDto.


        :param sdks: The sdks of this AppWithUserDto.  # noqa: E501
        :type sdks: list[AppSdkDto]
        """

        self._sdks = sdks

    @property
    def subscribed(self):
        """Gets the subscribed of this AppWithUserDto.  # noqa: E501


        :return: The subscribed of this AppWithUserDto.  # noqa: E501
        :rtype: bool
        """
        return self._subscribed

    @subscribed.setter
    def subscribed(self, subscribed):
        """Sets the subscribed of this AppWithUserDto.


        :param subscribed: The subscribed of this AppWithUserDto.  # noqa: E501
        :type subscribed: bool
        """

        self._subscribed = subscribed

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
        if not isinstance(other, AppWithUserDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AppWithUserDto):
            return True

        return self.to_dict() != other.to_dict()
