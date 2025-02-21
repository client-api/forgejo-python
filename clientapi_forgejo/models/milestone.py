# coding: utf-8

"""
    Forgejo API

    This documentation describes the Forgejo API.

    The version of the OpenAPI document: 10.0.0-93-60eedb9+gitea-1.22.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Milestone(BaseModel):
    """
    Milestone milestone is a collection of issues on one repository
    """ # noqa: E501
    closed_at: Optional[datetime] = None
    closed_issues: Optional[StrictInt] = None
    created_at: Optional[datetime] = None
    description: Optional[StrictStr] = None
    due_on: Optional[datetime] = None
    id: Optional[StrictInt] = None
    open_issues: Optional[StrictInt] = None
    state: Optional[StrictStr] = Field(default=None, description="StateType issue state type")
    title: Optional[StrictStr] = None
    updated_at: Optional[datetime] = None
    __properties: ClassVar[List[str]] = ["closed_at", "closed_issues", "created_at", "description", "due_on", "id", "open_issues", "state", "title", "updated_at"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Milestone from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Milestone from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "closed_at": obj.get("closed_at"),
            "closed_issues": obj.get("closed_issues"),
            "created_at": obj.get("created_at"),
            "description": obj.get("description"),
            "due_on": obj.get("due_on"),
            "id": obj.get("id"),
            "open_issues": obj.get("open_issues"),
            "state": obj.get("state"),
            "title": obj.get("title"),
            "updated_at": obj.get("updated_at")
        })
        return _obj


