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
from pydantic import BaseModel, StrictStr
from clientapi_forgejo.models.commit_meta import CommitMeta
from clientapi_forgejo.models.commit_user import CommitUser
from clientapi_forgejo.models.payload_commit_verification import PayloadCommitVerification

class RepoCommit(BaseModel):
    """
    RepoCommit
    """
    author: Optional[CommitUser] = None
    committer: Optional[CommitUser] = None
    message: Optional[StrictStr] = None
    tree: Optional[CommitMeta] = None
    url: Optional[StrictStr] = None
    verification: Optional[PayloadCommitVerification] = None
    __properties = ["author", "committer", "message", "tree", "url", "verification"]

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
    def from_json(cls, json_str: str) -> RepoCommit:
        """Create an instance of RepoCommit from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of author
        if self.author:
            _dict['author'] = self.author.to_dict()
        # override the default output from pydantic by calling `to_dict()` of committer
        if self.committer:
            _dict['committer'] = self.committer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tree
        if self.tree:
            _dict['tree'] = self.tree.to_dict()
        # override the default output from pydantic by calling `to_dict()` of verification
        if self.verification:
            _dict['verification'] = self.verification.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RepoCommit:
        """Create an instance of RepoCommit from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RepoCommit.parse_obj(obj)

        _obj = RepoCommit.parse_obj({
            "author": CommitUser.from_dict(obj.get("author")) if obj.get("author") is not None else None,
            "committer": CommitUser.from_dict(obj.get("committer")) if obj.get("committer") is not None else None,
            "message": obj.get("message"),
            "tree": CommitMeta.from_dict(obj.get("tree")) if obj.get("tree") is not None else None,
            "url": obj.get("url"),
            "verification": PayloadCommitVerification.from_dict(obj.get("verification")) if obj.get("verification") is not None else None
        })
        return _obj


