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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class CreateRepoOption(BaseModel):
    """
    CreateRepoOption options when creating repository
    """ # noqa: E501
    auto_init: Optional[StrictBool] = Field(default=None, description="Whether the repository should be auto-initialized?")
    default_branch: Optional[StrictStr] = Field(default=None, description="DefaultBranch of the repository (used when initializes and in template)")
    description: Optional[StrictStr] = Field(default=None, description="Description of the repository to create")
    gitignores: Optional[StrictStr] = Field(default=None, description="Gitignores to use")
    issue_labels: Optional[StrictStr] = Field(default=None, description="Label-Set to use")
    license: Optional[StrictStr] = Field(default=None, description="License to use")
    name: StrictStr = Field(description="Name of the repository to create")
    object_format_name: Optional[StrictStr] = Field(default=None, description="ObjectFormatName of the underlying git repository")
    private: Optional[StrictBool] = Field(default=None, description="Whether the repository is private")
    readme: Optional[StrictStr] = Field(default=None, description="Readme of the repository to create")
    template: Optional[StrictBool] = Field(default=None, description="Whether the repository is template")
    trust_model: Optional[StrictStr] = Field(default=None, description="TrustModel of the repository")
    __properties: ClassVar[List[str]] = ["auto_init", "default_branch", "description", "gitignores", "issue_labels", "license", "name", "object_format_name", "private", "readme", "template", "trust_model"]

    @field_validator('object_format_name')
    def object_format_name_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['sha1', 'sha256']):
            raise ValueError("must be one of enum values ('sha1', 'sha256')")
        return value

    @field_validator('trust_model')
    def trust_model_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['default', 'collaborator', 'committer', 'collaboratorcommitter']):
            raise ValueError("must be one of enum values ('default', 'collaborator', 'committer', 'collaboratorcommitter')")
        return value

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
        """Create an instance of CreateRepoOption from a JSON string"""
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
        """Create an instance of CreateRepoOption from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "auto_init": obj.get("auto_init"),
            "default_branch": obj.get("default_branch"),
            "description": obj.get("description"),
            "gitignores": obj.get("gitignores"),
            "issue_labels": obj.get("issue_labels"),
            "license": obj.get("license"),
            "name": obj.get("name"),
            "object_format_name": obj.get("object_format_name"),
            "private": obj.get("private"),
            "readme": obj.get("readme"),
            "template": obj.get("template"),
            "trust_model": obj.get("trust_model")
        })
        return _obj


