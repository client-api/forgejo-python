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

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from clientapi_forgejo.models.notification_subject import NotificationSubject
from clientapi_forgejo.models.repository import Repository

class NotificationThread(BaseModel):
    """
    NotificationThread expose Notification on API  # noqa: E501
    """
    id: Optional[StrictInt] = None
    pinned: Optional[StrictBool] = None
    repository: Optional[Repository] = None
    subject: Optional[NotificationSubject] = None
    unread: Optional[StrictBool] = None
    updated_at: Optional[datetime] = None
    url: Optional[StrictStr] = None
    __properties = ["id", "pinned", "repository", "subject", "unread", "updated_at", "url"]

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
    def from_json(cls, json_str: str) -> NotificationThread:
        """Create an instance of NotificationThread from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of repository
        if self.repository:
            _dict['repository'] = self.repository.to_dict()
        # override the default output from pydantic by calling `to_dict()` of subject
        if self.subject:
            _dict['subject'] = self.subject.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NotificationThread:
        """Create an instance of NotificationThread from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return NotificationThread.parse_obj(obj)

        _obj = NotificationThread.parse_obj({
            "id": obj.get("id"),
            "pinned": obj.get("pinned"),
            "repository": Repository.from_dict(obj.get("repository")) if obj.get("repository") is not None else None,
            "subject": NotificationSubject.from_dict(obj.get("subject")) if obj.get("subject") is not None else None,
            "unread": obj.get("unread"),
            "updated_at": obj.get("updated_at"),
            "url": obj.get("url")
        })
        return _obj


