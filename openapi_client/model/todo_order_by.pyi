# coding: utf-8

"""
    Puupee API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
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

from openapi_client import schemas  # noqa: F401


class TodoOrderBy(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    
    @schemas.classproperty
    def CREATION_TIME(cls):
        return cls("CreationTime")
    
    @schemas.classproperty
    def CREATION_TIME_DESC(cls):
        return cls("CreationTimeDesc")
    
    @schemas.classproperty
    def LAST_MODIFICATION_TIME(cls):
        return cls("LastModificationTime")
    
    @schemas.classproperty
    def LAST_MODIFICATION_TIME_DESC(cls):
        return cls("LastModificationTimeDesc")
    
    @schemas.classproperty
    def TITLE(cls):
        return cls("Title")
    
    @schemas.classproperty
    def TITLE_DESC(cls):
        return cls("TitleDesc")
    
    @schemas.classproperty
    def PRIORITY(cls):
        return cls("Priority")
    
    @schemas.classproperty
    def PRIORITY_DESC(cls):
        return cls("PriorityDesc")
    
    @schemas.classproperty
    def TAG(cls):
        return cls("Tag")
    
    @schemas.classproperty
    def TAG_DESC(cls):
        return cls("TagDesc")
