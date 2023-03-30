# coding: utf-8

"""
    Puupee API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0.0
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


class CreateOpenIddictApplicationDto(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            type = schemas.StrSchema
            displayName = schemas.StrSchema
            displayNames = schemas.StrSchema
            
            
            class permissions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'permissions':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            postLogoutRedirectUris = schemas.StrSchema
            properties = schemas.StrSchema
            redirectUris = schemas.StrSchema
            requirements = schemas.StrSchema
            clientUri = schemas.StrSchema
            logoUri = schemas.StrSchema
            
            
            class grantTypes(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'grantTypes':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class scopes(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'scopes':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "type": type,
                "displayName": displayName,
                "displayNames": displayNames,
                "permissions": permissions,
                "postLogoutRedirectUris": postLogoutRedirectUris,
                "properties": properties,
                "redirectUris": redirectUris,
                "requirements": requirements,
                "clientUri": clientUri,
                "logoUri": logoUri,
                "grantTypes": grantTypes,
                "scopes": scopes,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["displayName"]) -> MetaOapg.properties.displayName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["displayNames"]) -> MetaOapg.properties.displayNames: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["permissions"]) -> MetaOapg.properties.permissions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["postLogoutRedirectUris"]) -> MetaOapg.properties.postLogoutRedirectUris: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["properties"]) -> MetaOapg.properties.properties: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["redirectUris"]) -> MetaOapg.properties.redirectUris: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requirements"]) -> MetaOapg.properties.requirements: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clientUri"]) -> MetaOapg.properties.clientUri: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["logoUri"]) -> MetaOapg.properties.logoUri: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["grantTypes"]) -> MetaOapg.properties.grantTypes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scopes"]) -> MetaOapg.properties.scopes: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "displayName", "displayNames", "permissions", "postLogoutRedirectUris", "properties", "redirectUris", "requirements", "clientUri", "logoUri", "grantTypes", "scopes", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["displayName"]) -> typing.Union[MetaOapg.properties.displayName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["displayNames"]) -> typing.Union[MetaOapg.properties.displayNames, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["permissions"]) -> typing.Union[MetaOapg.properties.permissions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["postLogoutRedirectUris"]) -> typing.Union[MetaOapg.properties.postLogoutRedirectUris, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["properties"]) -> typing.Union[MetaOapg.properties.properties, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["redirectUris"]) -> typing.Union[MetaOapg.properties.redirectUris, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requirements"]) -> typing.Union[MetaOapg.properties.requirements, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clientUri"]) -> typing.Union[MetaOapg.properties.clientUri, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["logoUri"]) -> typing.Union[MetaOapg.properties.logoUri, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["grantTypes"]) -> typing.Union[MetaOapg.properties.grantTypes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scopes"]) -> typing.Union[MetaOapg.properties.scopes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "displayName", "displayNames", "permissions", "postLogoutRedirectUris", "properties", "redirectUris", "requirements", "clientUri", "logoUri", "grantTypes", "scopes", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        displayName: typing.Union[MetaOapg.properties.displayName, str, schemas.Unset] = schemas.unset,
        displayNames: typing.Union[MetaOapg.properties.displayNames, str, schemas.Unset] = schemas.unset,
        permissions: typing.Union[MetaOapg.properties.permissions, list, tuple, schemas.Unset] = schemas.unset,
        postLogoutRedirectUris: typing.Union[MetaOapg.properties.postLogoutRedirectUris, str, schemas.Unset] = schemas.unset,
        properties: typing.Union[MetaOapg.properties.properties, str, schemas.Unset] = schemas.unset,
        redirectUris: typing.Union[MetaOapg.properties.redirectUris, str, schemas.Unset] = schemas.unset,
        requirements: typing.Union[MetaOapg.properties.requirements, str, schemas.Unset] = schemas.unset,
        clientUri: typing.Union[MetaOapg.properties.clientUri, str, schemas.Unset] = schemas.unset,
        logoUri: typing.Union[MetaOapg.properties.logoUri, str, schemas.Unset] = schemas.unset,
        grantTypes: typing.Union[MetaOapg.properties.grantTypes, list, tuple, schemas.Unset] = schemas.unset,
        scopes: typing.Union[MetaOapg.properties.scopes, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateOpenIddictApplicationDto':
        return super().__new__(
            cls,
            *args,
            type=type,
            displayName=displayName,
            displayNames=displayNames,
            permissions=permissions,
            postLogoutRedirectUris=postLogoutRedirectUris,
            properties=properties,
            redirectUris=redirectUris,
            requirements=requirements,
            clientUri=clientUri,
            logoUri=logoUri,
            grantTypes=grantTypes,
            scopes=scopes,
            _configuration=_configuration,
            **kwargs,
        )
