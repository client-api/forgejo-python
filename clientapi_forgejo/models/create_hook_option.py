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

class CreateHookOption(BaseModel):
    """
    CreateHookOption options when create a hook
    """ # noqa: E501
    active: Optional[StrictBool] = False
    authorization_header: Optional[StrictStr] = None
    branch_filter: Optional[StrictStr] = None
    config: Dict[str, StrictStr] = Field(description="CreateHookOptionConfig has all config options in it required are \"content_type\" and \"url\" Required")
    events: Optional[List[StrictStr]] = None
    type: StrictStr
    __properties: ClassVar[List[str]] = ["active", "authorization_header", "branch_filter", "config", "events", "type"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['forgejo', 'dingtalk', 'discord', 'gitea', 'gogs', 'msteams', 'slack', 'telegram', 'feishu', 'wechatwork', 'packagist']):
            raise ValueError("must be one of enum values ('forgejo', 'dingtalk', 'discord', 'gitea', 'gogs', 'msteams', 'slack', 'telegram', 'feishu', 'wechatwork', 'packagist')")
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
        """Create an instance of CreateHookOption from a JSON string"""
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
        """Create an instance of CreateHookOption from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "active": obj.get("active") if obj.get("active") is not None else False,
            "authorization_header": obj.get("authorization_header"),
            "branch_filter": obj.get("branch_filter"),
            "config": obj.get("config"),
            "events": obj.get("events"),
            "type": obj.get("type")
        })
        return _obj


