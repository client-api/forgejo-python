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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Hook(BaseModel):
    """
    Hook a hook is a web hook when one repository changed
    """ # noqa: E501
    active: Optional[StrictBool] = None
    authorization_header: Optional[StrictStr] = None
    branch_filter: Optional[StrictStr] = None
    config: Optional[Dict[str, StrictStr]] = Field(default=None, description="Deprecated: use Metadata instead")
    content_type: Optional[StrictStr] = None
    created_at: Optional[datetime] = None
    events: Optional[List[StrictStr]] = None
    id: Optional[StrictInt] = None
    metadata: Optional[Dict[str, Any]] = None
    type: Optional[StrictStr] = None
    updated_at: Optional[datetime] = None
    url: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["active", "authorization_header", "branch_filter", "config", "content_type", "created_at", "events", "id", "metadata", "type", "updated_at", "url"]

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
        """Create an instance of Hook from a JSON string"""
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
        """Create an instance of Hook from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "active": obj.get("active"),
            "authorization_header": obj.get("authorization_header"),
            "branch_filter": obj.get("branch_filter"),
            "config": obj.get("config"),
            "content_type": obj.get("content_type"),
            "created_at": obj.get("created_at"),
            "events": obj.get("events"),
            "id": obj.get("id"),
            "metadata": obj.get("metadata"),
            "type": obj.get("type"),
            "updated_at": obj.get("updated_at"),
            "url": obj.get("url")
        })
        return _obj


