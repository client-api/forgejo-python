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
from clientapi_forgejo.models.gpg_key_email import GPGKeyEmail
from typing import Optional, Set
from typing_extensions import Self

class GPGKey(BaseModel):
    """
    GPGKey a user GPG key to sign commit and tag in repository
    """ # noqa: E501
    can_certify: Optional[StrictBool] = None
    can_encrypt_comms: Optional[StrictBool] = None
    can_encrypt_storage: Optional[StrictBool] = None
    can_sign: Optional[StrictBool] = None
    created_at: Optional[datetime] = None
    emails: Optional[List[GPGKeyEmail]] = None
    expires_at: Optional[datetime] = None
    id: Optional[StrictInt] = None
    key_id: Optional[StrictStr] = None
    primary_key_id: Optional[StrictStr] = None
    public_key: Optional[StrictStr] = None
    subkeys: Optional[List[GPGKey]] = None
    verified: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["can_certify", "can_encrypt_comms", "can_encrypt_storage", "can_sign", "created_at", "emails", "expires_at", "id", "key_id", "primary_key_id", "public_key", "subkeys", "verified"]

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
        """Create an instance of GPGKey from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in emails (list)
        _items = []
        if self.emails:
            for _item_emails in self.emails:
                if _item_emails:
                    _items.append(_item_emails.to_dict())
            _dict['emails'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in subkeys (list)
        _items = []
        if self.subkeys:
            for _item_subkeys in self.subkeys:
                if _item_subkeys:
                    _items.append(_item_subkeys.to_dict())
            _dict['subkeys'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GPGKey from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "can_certify": obj.get("can_certify"),
            "can_encrypt_comms": obj.get("can_encrypt_comms"),
            "can_encrypt_storage": obj.get("can_encrypt_storage"),
            "can_sign": obj.get("can_sign"),
            "created_at": obj.get("created_at"),
            "emails": [GPGKeyEmail.from_dict(_item) for _item in obj["emails"]] if obj.get("emails") is not None else None,
            "expires_at": obj.get("expires_at"),
            "id": obj.get("id"),
            "key_id": obj.get("key_id"),
            "primary_key_id": obj.get("primary_key_id"),
            "public_key": obj.get("public_key"),
            "subkeys": [GPGKey.from_dict(_item) for _item in obj["subkeys"]] if obj.get("subkeys") is not None else None,
            "verified": obj.get("verified")
        })
        return _obj

# TODO: Rewrite to not use raise_errors
GPGKey.model_rebuild(raise_errors=False)

