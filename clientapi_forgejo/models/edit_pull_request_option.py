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
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class EditPullRequestOption(BaseModel):
    """
    EditPullRequestOption options when modify pull request
    """ # noqa: E501
    allow_maintainer_edit: Optional[StrictBool] = None
    assignee: Optional[StrictStr] = None
    assignees: Optional[List[StrictStr]] = None
    base: Optional[StrictStr] = None
    body: Optional[StrictStr] = None
    due_date: Optional[datetime] = None
    labels: Optional[List[StrictInt]] = None
    milestone: Optional[StrictInt] = None
    state: Optional[StrictStr] = None
    title: Optional[StrictStr] = None
    unset_due_date: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["allow_maintainer_edit", "assignee", "assignees", "base", "body", "due_date", "labels", "milestone", "state", "title", "unset_due_date"]

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
        """Create an instance of EditPullRequestOption from a JSON string"""
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
        """Create an instance of EditPullRequestOption from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "allow_maintainer_edit": obj.get("allow_maintainer_edit"),
            "assignee": obj.get("assignee"),
            "assignees": obj.get("assignees"),
            "base": obj.get("base"),
            "body": obj.get("body"),
            "due_date": obj.get("due_date"),
            "labels": obj.get("labels"),
            "milestone": obj.get("milestone"),
            "state": obj.get("state"),
            "title": obj.get("title"),
            "unset_due_date": obj.get("unset_due_date")
        })
        return _obj


