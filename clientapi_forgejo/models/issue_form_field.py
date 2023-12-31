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


from typing import Any, Dict, Optional
from pydantic import BaseModel, StrictStr

class IssueFormField(BaseModel):
    """
    IssueFormField represents a form field  # noqa: E501
    """
    attributes: Optional[Dict[str, Dict[str, Any]]] = None
    id: Optional[StrictStr] = None
    type: Optional[StrictStr] = None
    validations: Optional[Dict[str, Dict[str, Any]]] = None
    __properties = ["attributes", "id", "type", "validations"]

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
    def from_json(cls, json_str: str) -> IssueFormField:
        """Create an instance of IssueFormField from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IssueFormField:
        """Create an instance of IssueFormField from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return IssueFormField.parse_obj(obj)

        _obj = IssueFormField.parse_obj({
            "attributes": obj.get("attributes"),
            "id": obj.get("id"),
            "type": obj.get("type"),
            "validations": obj.get("validations")
        })
        return _obj


