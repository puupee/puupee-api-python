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


class CreateOrUpdateAppDto(object):
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
        'webhook_url': 'str',
        'business_domain': 'str',
        'business_url': 'str',
        'subscription_platforms': 'str',
        'free_platforms': 'str',
        'spec_json_schema': 'str',
        'default_storage_size': 'int',
        'default_single_file_max_size': 'int',
        'is_published': 'bool',
        'features': 'list[AppFeatureDto]',
        'sdks': 'list[AppSdkDto]',
        'open_client': 'CreateOpenIddictApplicationDto'
    }

    attribute_map = {
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
        'webhook_url': 'webhookUrl',
        'business_domain': 'businessDomain',
        'business_url': 'businessUrl',
        'subscription_platforms': 'subscriptionPlatforms',
        'free_platforms': 'freePlatforms',
        'spec_json_schema': 'specJsonSchema',
        'default_storage_size': 'defaultStorageSize',
        'default_single_file_max_size': 'defaultSingleFileMaxSize',
        'is_published': 'isPublished',
        'features': 'features',
        'sdks': 'sdks',
        'open_client': 'openClient'
    }

    def __init__(self, name=None, display_name=None, framework=None, app_type=None, description=None, icon=None, home_page=None, sort_index=None, git_repository=None, git_repository_type=None, is_enabled=None, webhook_url=None, business_domain=None, business_url=None, subscription_platforms=None, free_platforms=None, spec_json_schema=None, default_storage_size=None, default_single_file_max_size=None, is_published=None, features=None, sdks=None, open_client=None, local_vars_configuration=None):  # noqa: E501
        """CreateOrUpdateAppDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

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
        self._webhook_url = None
        self._business_domain = None
        self._business_url = None
        self._subscription_platforms = None
        self._free_platforms = None
        self._spec_json_schema = None
        self._default_storage_size = None
        self._default_single_file_max_size = None
        self._is_published = None
        self._features = None
        self._sdks = None
        self._open_client = None
        self.discriminator = None

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
        self.webhook_url = webhook_url
        self.business_domain = business_domain
        self.business_url = business_url
        self.subscription_platforms = subscription_platforms
        self.free_platforms = free_platforms
        self.spec_json_schema = spec_json_schema
        if default_storage_size is not None:
            self.default_storage_size = default_storage_size
        if default_single_file_max_size is not None:
            self.default_single_file_max_size = default_single_file_max_size
        if is_published is not None:
            self.is_published = is_published
        self.features = features
        self.sdks = sdks
        if open_client is not None:
            self.open_client = open_client

    @property
    def name(self):
        """Gets the name of this CreateOrUpdateAppDto.  # noqa: E501


        :return: The name of this CreateOrUpdateAppDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateOrUpdateAppDto.


        :param name: The name of this CreateOrUpdateAppDto.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def display_name(self):
        """Gets the display_name of this CreateOrUpdateAppDto.  # noqa: E501


        :return: The display_name of this CreateOrUpdateAppDto.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this CreateOrUpdateAppDto.


        :param display_name: The display_name of this CreateOrUpdateAppDto.  # noqa: E501
        :type display_name: str
        """

        self._display_name = display_name

    @property
    def framework(self):
        """Gets the framework of this CreateOrUpdateAppDto.  # noqa: E501


        :return: The framework of this CreateOrUpdateAppDto.  # noqa: E501
        :rtype: str
        """
        return self._framework

    @framework.setter
    def framework(self, framework):
        """Sets the framework of this CreateOrUpdateAppDto.


        :param framework: The framework of this CreateOrUpdateAppDto.  # noqa: E501
        :type framework: str
        """

        self._framework = framework

    @property
    def app_type(self):
        """Gets the app_type of this CreateOrUpdateAppDto.  # noqa: E501


        :return: The app_type of this CreateOrUpdateAppDto.  # noqa: E501
        :rtype: str
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        """Sets the app_type of this CreateOrUpdateAppDto.


        :param app_type: The app_type of this CreateOrUpdateAppDto.  # noqa: E501
        :type app_type: str
        """

        self._app_type = app_type

    @property
    def description(self):
        """Gets the description of this CreateOrUpdateAppDto.  # noqa: E501


        :return: The description of this CreateOrUpdateAppDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateOrUpdateAppDto.


        :param description: The description of this CreateOrUpdateAppDto.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def icon(self):
        """Gets the icon of this CreateOrUpdateAppDto.  # noqa: E501


        :return: The icon of this CreateOrUpdateAppDto.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this CreateOrUpdateAppDto.


        :param icon: The icon of this CreateOrUpdateAppDto.  # noqa: E501
        :type icon: str
        """

        self._icon = icon

    @property
    def home_page(self):
        """Gets the home_page of this CreateOrUpdateAppDto.  # noqa: E501


        :return: The home_page of this CreateOrUpdateAppDto.  # noqa: E501
        :rtype: str
        """
        return self._home_page

    @home_page.setter
    def home_page(self, home_page):
        """Sets the home_page of this CreateOrUpdateAppDto.


        :param home_page: The home_page of this CreateOrUpdateAppDto.  # noqa: E501
        :type home_page: str
        """

        self._home_page = home_page

    @property
    def sort_index(self):
        """Gets the sort_index of this CreateOrUpdateAppDto.  # noqa: E501


        :return: The sort_index of this CreateOrUpdateAppDto.  # noqa: E501
        :rtype: int
        """
        return self._sort_index

    @sort_index.setter
    def sort_index(self, sort_index):
        """Sets the sort_index of this CreateOrUpdateAppDto.


        :param sort_index: The sort_index of this CreateOrUpdateAppDto.  # noqa: E501
        :type sort_index: int
        """

        self._sort_index = sort_index

    @property
    def git_repository(self):
        """Gets the git_repository of this CreateOrUpdateAppDto.  # noqa: E501


        :return: The git_repository of this CreateOrUpdateAppDto.  # noqa: E501
        :rtype: str
        """
        return self._git_repository

    @git_repository.setter
    def git_repository(self, git_repository):
        """Sets the git_repository of this CreateOrUpdateAppDto.


        :param git_repository: The git_repository of this CreateOrUpdateAppDto.  # noqa: E501
        :type git_repository: str
        """

        self._git_repository = git_repository

    @property
    def git_repository_type(self):
        """Gets the git_repository_type of this CreateOrUpdateAppDto.  # noqa: E501


        :return: The git_repository_type of this CreateOrUpdateAppDto.  # noqa: E501
        :rtype: str
        """
        return self._git_repository_type

    @git_repository_type.setter
    def git_repository_type(self, git_repository_type):
        """Sets the git_repository_type of this CreateOrUpdateAppDto.


        :param git_repository_type: The git_repository_type of this CreateOrUpdateAppDto.  # noqa: E501
        :type git_repository_type: str
        """

        self._git_repository_type = git_repository_type

    @property
    def is_enabled(self):
        """Gets the is_enabled of this CreateOrUpdateAppDto.  # noqa: E501


        :return: The is_enabled of this CreateOrUpdateAppDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """Sets the is_enabled of this CreateOrUpdateAppDto.


        :param is_enabled: The is_enabled of this CreateOrUpdateAppDto.  # noqa: E501
        :type is_enabled: bool
        """

        self._is_enabled = is_enabled

    @property
    def webhook_url(self):
        """Gets the webhook_url of this CreateOrUpdateAppDto.  # noqa: E501


        :return: The webhook_url of this CreateOrUpdateAppDto.  # noqa: E501
        :rtype: str
        """
        return self._webhook_url

    @webhook_url.setter
    def webhook_url(self, webhook_url):
        """Sets the webhook_url of this CreateOrUpdateAppDto.


        :param webhook_url: The webhook_url of this CreateOrUpdateAppDto.  # noqa: E501
        :type webhook_url: str
        """

        self._webhook_url = webhook_url

    @property
    def business_domain(self):
        """Gets the business_domain of this CreateOrUpdateAppDto.  # noqa: E501


        :return: The business_domain of this CreateOrUpdateAppDto.  # noqa: E501
        :rtype: str
        """
        return self._business_domain

    @business_domain.setter
    def business_domain(self, business_domain):
        """Sets the business_domain of this CreateOrUpdateAppDto.


        :param business_domain: The business_domain of this CreateOrUpdateAppDto.  # noqa: E501
        :type business_domain: str
        """

        self._business_domain = business_domain

    @property
    def business_url(self):
        """Gets the business_url of this CreateOrUpdateAppDto.  # noqa: E501


        :return: The business_url of this CreateOrUpdateAppDto.  # noqa: E501
        :rtype: str
        """
        return self._business_url

    @business_url.setter
    def business_url(self, business_url):
        """Sets the business_url of this CreateOrUpdateAppDto.


        :param business_url: The business_url of this CreateOrUpdateAppDto.  # noqa: E501
        :type business_url: str
        """

        self._business_url = business_url

    @property
    def subscription_platforms(self):
        """Gets the subscription_platforms of this CreateOrUpdateAppDto.  # noqa: E501


        :return: The subscription_platforms of this CreateOrUpdateAppDto.  # noqa: E501
        :rtype: str
        """
        return self._subscription_platforms

    @subscription_platforms.setter
    def subscription_platforms(self, subscription_platforms):
        """Sets the subscription_platforms of this CreateOrUpdateAppDto.


        :param subscription_platforms: The subscription_platforms of this CreateOrUpdateAppDto.  # noqa: E501
        :type subscription_platforms: str
        """

        self._subscription_platforms = subscription_platforms

    @property
    def free_platforms(self):
        """Gets the free_platforms of this CreateOrUpdateAppDto.  # noqa: E501


        :return: The free_platforms of this CreateOrUpdateAppDto.  # noqa: E501
        :rtype: str
        """
        return self._free_platforms

    @free_platforms.setter
    def free_platforms(self, free_platforms):
        """Sets the free_platforms of this CreateOrUpdateAppDto.


        :param free_platforms: The free_platforms of this CreateOrUpdateAppDto.  # noqa: E501
        :type free_platforms: str
        """

        self._free_platforms = free_platforms

    @property
    def spec_json_schema(self):
        """Gets the spec_json_schema of this CreateOrUpdateAppDto.  # noqa: E501


        :return: The spec_json_schema of this CreateOrUpdateAppDto.  # noqa: E501
        :rtype: str
        """
        return self._spec_json_schema

    @spec_json_schema.setter
    def spec_json_schema(self, spec_json_schema):
        """Sets the spec_json_schema of this CreateOrUpdateAppDto.


        :param spec_json_schema: The spec_json_schema of this CreateOrUpdateAppDto.  # noqa: E501
        :type spec_json_schema: str
        """

        self._spec_json_schema = spec_json_schema

    @property
    def default_storage_size(self):
        """Gets the default_storage_size of this CreateOrUpdateAppDto.  # noqa: E501


        :return: The default_storage_size of this CreateOrUpdateAppDto.  # noqa: E501
        :rtype: int
        """
        return self._default_storage_size

    @default_storage_size.setter
    def default_storage_size(self, default_storage_size):
        """Sets the default_storage_size of this CreateOrUpdateAppDto.


        :param default_storage_size: The default_storage_size of this CreateOrUpdateAppDto.  # noqa: E501
        :type default_storage_size: int
        """

        self._default_storage_size = default_storage_size

    @property
    def default_single_file_max_size(self):
        """Gets the default_single_file_max_size of this CreateOrUpdateAppDto.  # noqa: E501


        :return: The default_single_file_max_size of this CreateOrUpdateAppDto.  # noqa: E501
        :rtype: int
        """
        return self._default_single_file_max_size

    @default_single_file_max_size.setter
    def default_single_file_max_size(self, default_single_file_max_size):
        """Sets the default_single_file_max_size of this CreateOrUpdateAppDto.


        :param default_single_file_max_size: The default_single_file_max_size of this CreateOrUpdateAppDto.  # noqa: E501
        :type default_single_file_max_size: int
        """

        self._default_single_file_max_size = default_single_file_max_size

    @property
    def is_published(self):
        """Gets the is_published of this CreateOrUpdateAppDto.  # noqa: E501


        :return: The is_published of this CreateOrUpdateAppDto.  # noqa: E501
        :rtype: bool
        """
        return self._is_published

    @is_published.setter
    def is_published(self, is_published):
        """Sets the is_published of this CreateOrUpdateAppDto.


        :param is_published: The is_published of this CreateOrUpdateAppDto.  # noqa: E501
        :type is_published: bool
        """

        self._is_published = is_published

    @property
    def features(self):
        """Gets the features of this CreateOrUpdateAppDto.  # noqa: E501


        :return: The features of this CreateOrUpdateAppDto.  # noqa: E501
        :rtype: list[AppFeatureDto]
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this CreateOrUpdateAppDto.


        :param features: The features of this CreateOrUpdateAppDto.  # noqa: E501
        :type features: list[AppFeatureDto]
        """

        self._features = features

    @property
    def sdks(self):
        """Gets the sdks of this CreateOrUpdateAppDto.  # noqa: E501


        :return: The sdks of this CreateOrUpdateAppDto.  # noqa: E501
        :rtype: list[AppSdkDto]
        """
        return self._sdks

    @sdks.setter
    def sdks(self, sdks):
        """Sets the sdks of this CreateOrUpdateAppDto.


        :param sdks: The sdks of this CreateOrUpdateAppDto.  # noqa: E501
        :type sdks: list[AppSdkDto]
        """

        self._sdks = sdks

    @property
    def open_client(self):
        """Gets the open_client of this CreateOrUpdateAppDto.  # noqa: E501


        :return: The open_client of this CreateOrUpdateAppDto.  # noqa: E501
        :rtype: CreateOpenIddictApplicationDto
        """
        return self._open_client

    @open_client.setter
    def open_client(self, open_client):
        """Sets the open_client of this CreateOrUpdateAppDto.


        :param open_client: The open_client of this CreateOrUpdateAppDto.  # noqa: E501
        :type open_client: CreateOpenIddictApplicationDto
        """

        self._open_client = open_client

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
        if not isinstance(other, CreateOrUpdateAppDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateOrUpdateAppDto):
            return True

        return self.to_dict() != other.to_dict()
