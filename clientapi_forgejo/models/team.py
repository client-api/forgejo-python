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

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from clientapi_forgejo.models.organization import Organization
from typing import Optional, Set
from typing_extensions import Self

class Team(BaseModel):
    """
    Team represents a team in an organization
    """ # noqa: E501
    can_create_org_repo: Optional[StrictBool] = None
    description: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    includes_all_repositories: Optional[StrictBool] = None
    name: Optional[StrictStr] = None
    organization: Optional[Organization] = None
    permission: Optional[StrictStr] = None
    units: Optional[List[StrictStr]] = None
    units_map: Optional[Dict[str, StrictStr]] = None
    __properties: ClassVar[List[str]] = ["can_create_org_repo", "description", "id", "includes_all_repositories", "name", "organization", "permission", "units", "units_map"]

    @field_validator('permission')
    def permission_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['none', 'read', 'write', 'admin', 'owner']):
            raise ValueError("must be one of enum values ('none', 'read', 'write', 'admin', 'owner')")
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
        """Create an instance of Team from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of organization
        if self.organization:
            _dict['organization'] = self.organization.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Team from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "can_create_org_repo": obj.get("can_create_org_repo"),
            "description": obj.get("description"),
            "id": obj.get("id"),
            "includes_all_repositories": obj.get("includes_all_repositories"),
            "name": obj.get("name"),
            "organization": Organization.from_dict(obj["organization"]) if obj.get("organization") is not None else None,
            "permission": obj.get("permission"),
            "units": obj.get("units"),
            "units_map": obj.get("units_map")
        })
        return _obj


