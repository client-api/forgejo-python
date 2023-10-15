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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist

class TransferRepoOption(BaseModel):
    """
    TransferRepoOption options when transfer a repository's ownership  # noqa: E501
    """
    new_owner: StrictStr = Field(...)
    team_ids: Optional[conlist(StrictInt)] = Field(None, description="ID of the team or teams to add to the repository. Teams can only be added to organization-owned repositories.")
    __properties = ["new_owner", "team_ids"]

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
    def from_json(cls, json_str: str) -> TransferRepoOption:
        """Create an instance of TransferRepoOption from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TransferRepoOption:
        """Create an instance of TransferRepoOption from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TransferRepoOption.parse_obj(obj)

        _obj = TransferRepoOption.parse_obj({
            "new_owner": obj.get("new_owner"),
            "team_ids": obj.get("team_ids")
        })
        return _obj

