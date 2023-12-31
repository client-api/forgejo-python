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
from pydantic import BaseModel, Field, StrictBool, StrictStr

class CreateReleaseOption(BaseModel):
    """
    CreateReleaseOption options when creating a release  # noqa: E501
    """
    body: Optional[StrictStr] = None
    draft: Optional[StrictBool] = None
    name: Optional[StrictStr] = None
    prerelease: Optional[StrictBool] = None
    tag_name: StrictStr = Field(...)
    target_commitish: Optional[StrictStr] = None
    __properties = ["body", "draft", "name", "prerelease", "tag_name", "target_commitish"]

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
    def from_json(cls, json_str: str) -> CreateReleaseOption:
        """Create an instance of CreateReleaseOption from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateReleaseOption:
        """Create an instance of CreateReleaseOption from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateReleaseOption.parse_obj(obj)

        _obj = CreateReleaseOption.parse_obj({
            "body": obj.get("body"),
            "draft": obj.get("draft"),
            "name": obj.get("name"),
            "prerelease": obj.get("prerelease"),
            "tag_name": obj.get("tag_name"),
            "target_commitish": obj.get("target_commitish")
        })
        return _obj


