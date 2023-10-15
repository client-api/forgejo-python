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


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, validator

class EditOrgOption(BaseModel):
    """
    EditOrgOption options for editing an organization  # noqa: E501
    """
    description: Optional[StrictStr] = None
    full_name: Optional[StrictStr] = None
    location: Optional[StrictStr] = None
    repo_admin_change_team_access: Optional[StrictBool] = None
    visibility: Optional[StrictStr] = Field(None, description="possible values are `public`, `limited` or `private`")
    website: Optional[StrictStr] = None
    __properties = ["description", "full_name", "location", "repo_admin_change_team_access", "visibility", "website"]

    @validator('visibility')
    def visibility_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('public', 'limited', 'private'):
            raise ValueError("must be one of enum values ('public', 'limited', 'private')")
        return value

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
    def from_json(cls, json_str: str) -> EditOrgOption:
        """Create an instance of EditOrgOption from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EditOrgOption:
        """Create an instance of EditOrgOption from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EditOrgOption.parse_obj(obj)

        _obj = EditOrgOption.parse_obj({
            "description": obj.get("description"),
            "full_name": obj.get("full_name"),
            "location": obj.get("location"),
            "repo_admin_change_team_access": obj.get("repo_admin_change_team_access"),
            "visibility": obj.get("visibility"),
            "website": obj.get("website")
        })
        return _obj


