# coding: utf-8

"""
    Puupee API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from puupee-api import schemas  # noqa: F401


class LoginResultType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    
    @schemas.classproperty
    def SUCCESS(cls):
        return cls("Success")
    
    @schemas.classproperty
    def INVALID_USER_NAME_OR_PASSWORD(cls):
        return cls("InvalidUserNameOrPassword")
    
    @schemas.classproperty
    def NOT_ALLOWED(cls):
        return cls("NotAllowed")
    
    @schemas.classproperty
    def LOCKED_OUT(cls):
        return cls("LockedOut")
    
    @schemas.classproperty
    def REQUIRES_TWO_FACTOR(cls):
        return cls("RequiresTwoFactor")