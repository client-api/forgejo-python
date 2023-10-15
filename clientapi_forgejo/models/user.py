# coding: utf-8

"""
    Forgejo API.

    This documentation describes the Forgejo API.

    The version of the OpenAPI document: 1.20.5+0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr

class User(BaseModel):
    """
    User represents a user  # noqa: E501
    """
    active: Optional[StrictBool] = Field(None, description="Is user active")
    avatar_url: Optional[StrictStr] = Field(None, description="URL to the user's avatar")
    created: Optional[datetime] = None
    description: Optional[StrictStr] = Field(None, description="the user's description")
    email: Optional[StrictStr] = None
    followers_count: Optional[StrictInt] = Field(None, description="user counts")
    following_count: Optional[StrictInt] = None
    full_name: Optional[StrictStr] = Field(None, description="the user's full name")
    id: Optional[StrictInt] = Field(None, description="the user's id")
    is_admin: Optional[StrictBool] = Field(None, description="Is the user an administrator")
    language: Optional[StrictStr] = Field(None, description="User locale")
    last_login: Optional[datetime] = None
    location: Optional[StrictStr] = Field(None, description="the user's location")
    login: Optional[StrictStr] = Field(None, description="the user's username")
    login_name: Optional[StrictStr] = Field('empty', description="the user's authentication sign-in name.")
    prohibit_login: Optional[StrictBool] = Field(None, description="Is user login prohibited")
    restricted: Optional[StrictBool] = Field(None, description="Is user restricted")
    starred_repos_count: Optional[StrictInt] = None
    visibility: Optional[StrictStr] = Field(None, description="User visibility level option: public, limited, private")
    website: Optional[StrictStr] = Field(None, description="the user's website")
    __properties = ["active", "avatar_url", "created", "description", "email", "followers_count", "following_count", "full_name", "id", "is_admin", "language", "last_login", "location", "login", "login_name", "prohibit_login", "restricted", "starred_repos_count", "visibility", "website"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> User:
        """Create an instance of User from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> User:
        """Create an instance of User from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return User.parse_obj(obj)

        _obj = User.parse_obj({
            "active": obj.get("active"),
            "avatar_url": obj.get("avatar_url"),
            "created": obj.get("created"),
            "description": obj.get("description"),
            "email": obj.get("email"),
            "followers_count": obj.get("followers_count"),
            "following_count": obj.get("following_count"),
            "full_name": obj.get("full_name"),
            "id": obj.get("id"),
            "is_admin": obj.get("is_admin"),
            "language": obj.get("language"),
            "last_login": obj.get("last_login"),
            "location": obj.get("location"),
            "login": obj.get("login"),
            "login_name": obj.get("login_name") if obj.get("login_name") is not None else 'empty',
            "prohibit_login": obj.get("prohibit_login"),
            "restricted": obj.get("restricted"),
            "starred_repos_count": obj.get("starred_repos_count"),
            "visibility": obj.get("visibility"),
            "website": obj.get("website")
        })
        return _obj


