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


class AppleVerifyReceiptResult(object):
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
        'environment': 'str',
        'is_retryable': 'bool',
        'status': 'AppleVerifyRecceiptStatus',
        'latest_receipt_info': 'list[LatestReceiptInfo]',
        'latest_receipt': 'str',
        'pending_renewal_info': 'list[PendingRenewalInfo]',
        'receipt': 'Receipt'
    }

    attribute_map = {
        'environment': 'environment',
        'is_retryable': 'is_retryable',
        'status': 'status',
        'latest_receipt_info': 'latest_receipt_info',
        'latest_receipt': 'latest_receipt',
        'pending_renewal_info': 'pending_renewal_info',
        'receipt': 'receipt'
    }

    def __init__(self, environment=None, is_retryable=None, status=None, latest_receipt_info=None, latest_receipt=None, pending_renewal_info=None, receipt=None, local_vars_configuration=None):  # noqa: E501
        """AppleVerifyReceiptResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._environment = None
        self._is_retryable = None
        self._status = None
        self._latest_receipt_info = None
        self._latest_receipt = None
        self._pending_renewal_info = None
        self._receipt = None
        self.discriminator = None

        self.environment = environment
        if is_retryable is not None:
            self.is_retryable = is_retryable
        if status is not None:
            self.status = status
        self.latest_receipt_info = latest_receipt_info
        self.latest_receipt = latest_receipt
        self.pending_renewal_info = pending_renewal_info
        if receipt is not None:
            self.receipt = receipt

    @property
    def environment(self):
        """Gets the environment of this AppleVerifyReceiptResult.  # noqa: E501


        :return: The environment of this AppleVerifyReceiptResult.  # noqa: E501
        :rtype: str
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this AppleVerifyReceiptResult.


        :param environment: The environment of this AppleVerifyReceiptResult.  # noqa: E501
        :type environment: str
        """

        self._environment = environment

    @property
    def is_retryable(self):
        """Gets the is_retryable of this AppleVerifyReceiptResult.  # noqa: E501


        :return: The is_retryable of this AppleVerifyReceiptResult.  # noqa: E501
        :rtype: bool
        """
        return self._is_retryable

    @is_retryable.setter
    def is_retryable(self, is_retryable):
        """Sets the is_retryable of this AppleVerifyReceiptResult.


        :param is_retryable: The is_retryable of this AppleVerifyReceiptResult.  # noqa: E501
        :type is_retryable: bool
        """

        self._is_retryable = is_retryable

    @property
    def status(self):
        """Gets the status of this AppleVerifyReceiptResult.  # noqa: E501


        :return: The status of this AppleVerifyReceiptResult.  # noqa: E501
        :rtype: AppleVerifyRecceiptStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AppleVerifyReceiptResult.


        :param status: The status of this AppleVerifyReceiptResult.  # noqa: E501
        :type status: AppleVerifyRecceiptStatus
        """

        self._status = status

    @property
    def latest_receipt_info(self):
        """Gets the latest_receipt_info of this AppleVerifyReceiptResult.  # noqa: E501


        :return: The latest_receipt_info of this AppleVerifyReceiptResult.  # noqa: E501
        :rtype: list[LatestReceiptInfo]
        """
        return self._latest_receipt_info

    @latest_receipt_info.setter
    def latest_receipt_info(self, latest_receipt_info):
        """Sets the latest_receipt_info of this AppleVerifyReceiptResult.


        :param latest_receipt_info: The latest_receipt_info of this AppleVerifyReceiptResult.  # noqa: E501
        :type latest_receipt_info: list[LatestReceiptInfo]
        """

        self._latest_receipt_info = latest_receipt_info

    @property
    def latest_receipt(self):
        """Gets the latest_receipt of this AppleVerifyReceiptResult.  # noqa: E501


        :return: The latest_receipt of this AppleVerifyReceiptResult.  # noqa: E501
        :rtype: str
        """
        return self._latest_receipt

    @latest_receipt.setter
    def latest_receipt(self, latest_receipt):
        """Sets the latest_receipt of this AppleVerifyReceiptResult.


        :param latest_receipt: The latest_receipt of this AppleVerifyReceiptResult.  # noqa: E501
        :type latest_receipt: str
        """

        self._latest_receipt = latest_receipt

    @property
    def pending_renewal_info(self):
        """Gets the pending_renewal_info of this AppleVerifyReceiptResult.  # noqa: E501


        :return: The pending_renewal_info of this AppleVerifyReceiptResult.  # noqa: E501
        :rtype: list[PendingRenewalInfo]
        """
        return self._pending_renewal_info

    @pending_renewal_info.setter
    def pending_renewal_info(self, pending_renewal_info):
        """Sets the pending_renewal_info of this AppleVerifyReceiptResult.


        :param pending_renewal_info: The pending_renewal_info of this AppleVerifyReceiptResult.  # noqa: E501
        :type pending_renewal_info: list[PendingRenewalInfo]
        """

        self._pending_renewal_info = pending_renewal_info

    @property
    def receipt(self):
        """Gets the receipt of this AppleVerifyReceiptResult.  # noqa: E501


        :return: The receipt of this AppleVerifyReceiptResult.  # noqa: E501
        :rtype: Receipt
        """
        return self._receipt

    @receipt.setter
    def receipt(self, receipt):
        """Sets the receipt of this AppleVerifyReceiptResult.


        :param receipt: The receipt of this AppleVerifyReceiptResult.  # noqa: E501
        :type receipt: Receipt
        """

        self._receipt = receipt

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
        if not isinstance(other, AppleVerifyReceiptResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AppleVerifyReceiptResult):
            return True

        return self.to_dict() != other.to_dict()
