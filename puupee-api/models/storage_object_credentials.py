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


class StorageObjectCredentials(object):
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
        'storage_class': 'str',
        'end_point': 'str',
        'protocal': 'str',
        'bucket_name': 'str',
        'region_id': 'str',
        'security_token': 'str',
        'access_key_id': 'str',
        'access_key_secret': 'str',
        'expiration': 'str',
        'expired_time': 'int',
        'app_id': 'str'
    }

    attribute_map = {
        'storage_class': 'storageClass',
        'end_point': 'endPoint',
        'protocal': 'protocal',
        'bucket_name': 'bucketName',
        'region_id': 'regionId',
        'security_token': 'securityToken',
        'access_key_id': 'accessKeyId',
        'access_key_secret': 'accessKeySecret',
        'expiration': 'expiration',
        'expired_time': 'expiredTime',
        'app_id': 'appId'
    }

    def __init__(self, storage_class=None, end_point=None, protocal=None, bucket_name=None, region_id=None, security_token=None, access_key_id=None, access_key_secret=None, expiration=None, expired_time=None, app_id=None, local_vars_configuration=None):  # noqa: E501
        """StorageObjectCredentials - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._storage_class = None
        self._end_point = None
        self._protocal = None
        self._bucket_name = None
        self._region_id = None
        self._security_token = None
        self._access_key_id = None
        self._access_key_secret = None
        self._expiration = None
        self._expired_time = None
        self._app_id = None
        self.discriminator = None

        self.storage_class = storage_class
        self.end_point = end_point
        self.protocal = protocal
        self.bucket_name = bucket_name
        self.region_id = region_id
        self.security_token = security_token
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.expiration = expiration
        if expired_time is not None:
            self.expired_time = expired_time
        self.app_id = app_id

    @property
    def storage_class(self):
        """Gets the storage_class of this StorageObjectCredentials.  # noqa: E501


        :return: The storage_class of this StorageObjectCredentials.  # noqa: E501
        :rtype: str
        """
        return self._storage_class

    @storage_class.setter
    def storage_class(self, storage_class):
        """Sets the storage_class of this StorageObjectCredentials.


        :param storage_class: The storage_class of this StorageObjectCredentials.  # noqa: E501
        :type storage_class: str
        """

        self._storage_class = storage_class

    @property
    def end_point(self):
        """Gets the end_point of this StorageObjectCredentials.  # noqa: E501


        :return: The end_point of this StorageObjectCredentials.  # noqa: E501
        :rtype: str
        """
        return self._end_point

    @end_point.setter
    def end_point(self, end_point):
        """Sets the end_point of this StorageObjectCredentials.


        :param end_point: The end_point of this StorageObjectCredentials.  # noqa: E501
        :type end_point: str
        """

        self._end_point = end_point

    @property
    def protocal(self):
        """Gets the protocal of this StorageObjectCredentials.  # noqa: E501


        :return: The protocal of this StorageObjectCredentials.  # noqa: E501
        :rtype: str
        """
        return self._protocal

    @protocal.setter
    def protocal(self, protocal):
        """Sets the protocal of this StorageObjectCredentials.


        :param protocal: The protocal of this StorageObjectCredentials.  # noqa: E501
        :type protocal: str
        """

        self._protocal = protocal

    @property
    def bucket_name(self):
        """Gets the bucket_name of this StorageObjectCredentials.  # noqa: E501


        :return: The bucket_name of this StorageObjectCredentials.  # noqa: E501
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """Sets the bucket_name of this StorageObjectCredentials.


        :param bucket_name: The bucket_name of this StorageObjectCredentials.  # noqa: E501
        :type bucket_name: str
        """

        self._bucket_name = bucket_name

    @property
    def region_id(self):
        """Gets the region_id of this StorageObjectCredentials.  # noqa: E501


        :return: The region_id of this StorageObjectCredentials.  # noqa: E501
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this StorageObjectCredentials.


        :param region_id: The region_id of this StorageObjectCredentials.  # noqa: E501
        :type region_id: str
        """

        self._region_id = region_id

    @property
    def security_token(self):
        """Gets the security_token of this StorageObjectCredentials.  # noqa: E501


        :return: The security_token of this StorageObjectCredentials.  # noqa: E501
        :rtype: str
        """
        return self._security_token

    @security_token.setter
    def security_token(self, security_token):
        """Sets the security_token of this StorageObjectCredentials.


        :param security_token: The security_token of this StorageObjectCredentials.  # noqa: E501
        :type security_token: str
        """

        self._security_token = security_token

    @property
    def access_key_id(self):
        """Gets the access_key_id of this StorageObjectCredentials.  # noqa: E501


        :return: The access_key_id of this StorageObjectCredentials.  # noqa: E501
        :rtype: str
        """
        return self._access_key_id

    @access_key_id.setter
    def access_key_id(self, access_key_id):
        """Sets the access_key_id of this StorageObjectCredentials.


        :param access_key_id: The access_key_id of this StorageObjectCredentials.  # noqa: E501
        :type access_key_id: str
        """

        self._access_key_id = access_key_id

    @property
    def access_key_secret(self):
        """Gets the access_key_secret of this StorageObjectCredentials.  # noqa: E501


        :return: The access_key_secret of this StorageObjectCredentials.  # noqa: E501
        :rtype: str
        """
        return self._access_key_secret

    @access_key_secret.setter
    def access_key_secret(self, access_key_secret):
        """Sets the access_key_secret of this StorageObjectCredentials.


        :param access_key_secret: The access_key_secret of this StorageObjectCredentials.  # noqa: E501
        :type access_key_secret: str
        """

        self._access_key_secret = access_key_secret

    @property
    def expiration(self):
        """Gets the expiration of this StorageObjectCredentials.  # noqa: E501


        :return: The expiration of this StorageObjectCredentials.  # noqa: E501
        :rtype: str
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        """Sets the expiration of this StorageObjectCredentials.


        :param expiration: The expiration of this StorageObjectCredentials.  # noqa: E501
        :type expiration: str
        """

        self._expiration = expiration

    @property
    def expired_time(self):
        """Gets the expired_time of this StorageObjectCredentials.  # noqa: E501


        :return: The expired_time of this StorageObjectCredentials.  # noqa: E501
        :rtype: int
        """
        return self._expired_time

    @expired_time.setter
    def expired_time(self, expired_time):
        """Sets the expired_time of this StorageObjectCredentials.


        :param expired_time: The expired_time of this StorageObjectCredentials.  # noqa: E501
        :type expired_time: int
        """

        self._expired_time = expired_time

    @property
    def app_id(self):
        """Gets the app_id of this StorageObjectCredentials.  # noqa: E501


        :return: The app_id of this StorageObjectCredentials.  # noqa: E501
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this StorageObjectCredentials.


        :param app_id: The app_id of this StorageObjectCredentials.  # noqa: E501
        :type app_id: str
        """

        self._app_id = app_id

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
        if not isinstance(other, StorageObjectCredentials):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StorageObjectCredentials):
            return True

        return self.to_dict() != other.to_dict()
