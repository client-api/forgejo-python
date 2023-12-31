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
from pydantic import BaseModel, conlist
from clientapi_forgejo.models.contents_response import ContentsResponse
from clientapi_forgejo.models.file_commit_response import FileCommitResponse
from clientapi_forgejo.models.payload_commit_verification import PayloadCommitVerification

class FilesResponse(BaseModel):
    """
    FilesResponse contains information about multiple files from a repo  # noqa: E501
    """
    commit: Optional[FileCommitResponse] = None
    files: Optional[conlist(ContentsResponse)] = None
    verification: Optional[PayloadCommitVerification] = None
    __properties = ["commit", "files", "verification"]

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
    def from_json(cls, json_str: str) -> FilesResponse:
        """Create an instance of FilesResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of commit
        if self.commit:
            _dict['commit'] = self.commit.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in files (list)
        _items = []
        if self.files:
            for _item in self.files:
                if _item:
                    _items.append(_item.to_dict())
            _dict['files'] = _items
        # override the default output from pydantic by calling `to_dict()` of verification
        if self.verification:
            _dict['verification'] = self.verification.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FilesResponse:
        """Create an instance of FilesResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FilesResponse.parse_obj(obj)

        _obj = FilesResponse.parse_obj({
            "commit": FileCommitResponse.from_dict(obj.get("commit")) if obj.get("commit") is not None else None,
            "files": [ContentsResponse.from_dict(_item) for _item in obj.get("files")] if obj.get("files") is not None else None,
            "verification": PayloadCommitVerification.from_dict(obj.get("verification")) if obj.get("verification") is not None else None
        })
        return _obj


