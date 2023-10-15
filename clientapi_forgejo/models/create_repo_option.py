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
from pydantic import BaseModel, Field, StrictBool, StrictStr, validator

class CreateRepoOption(BaseModel):
    """
    CreateRepoOption options when creating repository  # noqa: E501
    """
    auto_init: Optional[StrictBool] = Field(None, description="Whether the repository should be auto-initialized?")
    default_branch: Optional[StrictStr] = Field(None, description="DefaultBranch of the repository (used when initializes and in template)")
    description: Optional[StrictStr] = Field(None, description="Description of the repository to create")
    gitignores: Optional[StrictStr] = Field(None, description="Gitignores to use")
    issue_labels: Optional[StrictStr] = Field(None, description="Label-Set to use")
    license: Optional[StrictStr] = Field(None, description="License to use")
    name: StrictStr = Field(..., description="Name of the repository to create")
    private: Optional[StrictBool] = Field(None, description="Whether the repository is private")
    readme: Optional[StrictStr] = Field(None, description="Readme of the repository to create")
    template: Optional[StrictBool] = Field(None, description="Whether the repository is template")
    trust_model: Optional[StrictStr] = Field(None, description="TrustModel of the repository")
    __properties = ["auto_init", "default_branch", "description", "gitignores", "issue_labels", "license", "name", "private", "readme", "template", "trust_model"]

    @validator('trust_model')
    def trust_model_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('default', 'collaborator', 'committer', 'collaboratorcommitter'):
            raise ValueError("must be one of enum values ('default', 'collaborator', 'committer', 'collaboratorcommitter')")
        return value

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
    def from_json(cls, json_str: str) -> CreateRepoOption:
        """Create an instance of CreateRepoOption from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateRepoOption:
        """Create an instance of CreateRepoOption from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateRepoOption.parse_obj(obj)

        _obj = CreateRepoOption.parse_obj({
            "auto_init": obj.get("auto_init"),
            "default_branch": obj.get("default_branch"),
            "description": obj.get("description"),
            "gitignores": obj.get("gitignores"),
            "issue_labels": obj.get("issue_labels"),
            "license": obj.get("license"),
            "name": obj.get("name"),
            "private": obj.get("private"),
            "readme": obj.get("readme"),
            "template": obj.get("template"),
            "trust_model": obj.get("trust_model")
        })
        return _obj


