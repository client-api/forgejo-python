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
from pydantic import BaseModel, Field, StrictInt, StrictStr
from clientapi_forgejo.models.issue import Issue

class TrackedTime(BaseModel):
    """
    TrackedTime worked time for an issue / pr  # noqa: E501
    """
    created: Optional[datetime] = None
    id: Optional[StrictInt] = None
    issue: Optional[Issue] = None
    issue_id: Optional[StrictInt] = Field(None, description="deprecated (only for backwards compatibility)")
    time: Optional[StrictInt] = Field(None, description="Time in seconds")
    user_id: Optional[StrictInt] = Field(None, description="deprecated (only for backwards compatibility)")
    user_name: Optional[StrictStr] = None
    __properties = ["created", "id", "issue", "issue_id", "time", "user_id", "user_name"]

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
    def from_json(cls, json_str: str) -> TrackedTime:
        """Create an instance of TrackedTime from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of issue
        if self.issue:
            _dict['issue'] = self.issue.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TrackedTime:
        """Create an instance of TrackedTime from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TrackedTime.parse_obj(obj)

        _obj = TrackedTime.parse_obj({
            "created": obj.get("created"),
            "id": obj.get("id"),
            "issue": Issue.from_dict(obj.get("issue")) if obj.get("issue") is not None else None,
            "issue_id": obj.get("issue_id"),
            "time": obj.get("time"),
            "user_id": obj.get("user_id"),
            "user_name": obj.get("user_name")
        })
        return _obj


