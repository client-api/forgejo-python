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
from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist

class CreateIssueOption(BaseModel):
    """
    CreateIssueOption options to create one issue  # noqa: E501
    """
    assignee: Optional[StrictStr] = Field(None, description="deprecated")
    assignees: Optional[conlist(StrictStr)] = None
    body: Optional[StrictStr] = None
    closed: Optional[StrictBool] = None
    due_date: Optional[datetime] = None
    labels: Optional[conlist(StrictInt)] = Field(None, description="list of label ids")
    milestone: Optional[StrictInt] = Field(None, description="milestone id")
    ref: Optional[StrictStr] = None
    title: StrictStr = Field(...)
    __properties = ["assignee", "assignees", "body", "closed", "due_date", "labels", "milestone", "ref", "title"]

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
    def from_json(cls, json_str: str) -> CreateIssueOption:
        """Create an instance of CreateIssueOption from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateIssueOption:
        """Create an instance of CreateIssueOption from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateIssueOption.parse_obj(obj)

        _obj = CreateIssueOption.parse_obj({
            "assignee": obj.get("assignee"),
            "assignees": obj.get("assignees"),
            "body": obj.get("body"),
            "closed": obj.get("closed"),
            "due_date": obj.get("due_date"),
            "labels": obj.get("labels"),
            "milestone": obj.get("milestone"),
            "ref": obj.get("ref"),
            "title": obj.get("title")
        })
        return _obj

