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
from pydantic import BaseModel, Field, StrictInt, StrictStr

class PackageFile(BaseModel):
    """
    PackageFile represents a package file  # noqa: E501
    """
    size: Optional[StrictInt] = Field(None, alias="Size")
    id: Optional[StrictInt] = None
    md5: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    sha1: Optional[StrictStr] = None
    sha256: Optional[StrictStr] = None
    sha512: Optional[StrictStr] = None
    __properties = ["Size", "id", "md5", "name", "sha1", "sha256", "sha512"]

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
    def from_json(cls, json_str: str) -> PackageFile:
        """Create an instance of PackageFile from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PackageFile:
        """Create an instance of PackageFile from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PackageFile.parse_obj(obj)

        _obj = PackageFile.parse_obj({
            "size": obj.get("Size"),
            "id": obj.get("id"),
            "md5": obj.get("md5"),
            "name": obj.get("name"),
            "sha1": obj.get("sha1"),
            "sha256": obj.get("sha256"),
            "sha512": obj.get("sha512")
        })
        return _obj


