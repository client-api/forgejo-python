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
from pydantic import BaseModel, StrictStr

class EditMilestoneOption(BaseModel):
    """
    EditMilestoneOption options for editing a milestone  # noqa: E501
    """
    description: Optional[StrictStr] = None
    due_on: Optional[datetime] = None
    state: Optional[StrictStr] = None
    title: Optional[StrictStr] = None
    __properties = ["description", "due_on", "state", "title"]

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
    def from_json(cls, json_str: str) -> EditMilestoneOption:
        """Create an instance of EditMilestoneOption from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EditMilestoneOption:
        """Create an instance of EditMilestoneOption from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EditMilestoneOption.parse_obj(obj)

        _obj = EditMilestoneOption.parse_obj({
            "description": obj.get("description"),
            "due_on": obj.get("due_on"),
            "state": obj.get("state"),
            "title": obj.get("title")
        })
        return _obj


