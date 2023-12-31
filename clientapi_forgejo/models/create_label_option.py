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

class CreateLabelOption(BaseModel):
    """
    CreateLabelOption options for creating a label  # noqa: E501
    """
    color: StrictStr = Field(...)
    description: Optional[StrictStr] = None
    exclusive: Optional[StrictBool] = None
    name: StrictStr = Field(...)
    __properties = ["color", "description", "exclusive", "name"]

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
    def from_json(cls, json_str: str) -> CreateLabelOption:
        """Create an instance of CreateLabelOption from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateLabelOption:
        """Create an instance of CreateLabelOption from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateLabelOption.parse_obj(obj)

        _obj = CreateLabelOption.parse_obj({
            "color": obj.get("color"),
            "description": obj.get("description"),
            "exclusive": obj.get("exclusive"),
            "name": obj.get("name")
        })
        return _obj


