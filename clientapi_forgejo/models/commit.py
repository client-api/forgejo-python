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
from typing import List, Optional
from pydantic import BaseModel, StrictStr, conlist
from clientapi_forgejo.models.commit_affected_files import CommitAffectedFiles
from clientapi_forgejo.models.commit_meta import CommitMeta
from clientapi_forgejo.models.commit_stats import CommitStats
from clientapi_forgejo.models.repo_commit import RepoCommit
from clientapi_forgejo.models.user import User

class Commit(BaseModel):
    """
    Commit
    """
    author: Optional[User] = None
    commit: Optional[RepoCommit] = None
    committer: Optional[User] = None
    created: Optional[datetime] = None
    files: Optional[conlist(CommitAffectedFiles)] = None
    html_url: Optional[StrictStr] = None
    parents: Optional[conlist(CommitMeta)] = None
    sha: Optional[StrictStr] = None
    stats: Optional[CommitStats] = None
    url: Optional[StrictStr] = None
    __properties = ["author", "commit", "committer", "created", "files", "html_url", "parents", "sha", "stats", "url"]

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
    def from_json(cls, json_str: str) -> Commit:
        """Create an instance of Commit from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of commit
        if self.commit:
            _dict['commit'] = self.commit.to_dict()
        # override the default output from pydantic by calling `to_dict()` of committer
        if self.committer:
            _dict['committer'] = self.committer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in files (list)
        _items = []
        if self.files:
            for _item in self.files:
                if _item:
                    _items.append(_item.to_dict())
            _dict['files'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in parents (list)
        _items = []
        if self.parents:
            for _item in self.parents:
                if _item:
                    _items.append(_item.to_dict())
            _dict['parents'] = _items
        # override the default output from pydantic by calling `to_dict()` of stats
        if self.stats:
            _dict['stats'] = self.stats.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Commit:
        """Create an instance of Commit from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Commit.parse_obj(obj)

        _obj = Commit.parse_obj({
            "author": User.from_dict(obj.get("author")) if obj.get("author") is not None else None,
            "commit": RepoCommit.from_dict(obj.get("commit")) if obj.get("commit") is not None else None,
            "committer": User.from_dict(obj.get("committer")) if obj.get("committer") is not None else None,
            "created": obj.get("created"),
            "files": [CommitAffectedFiles.from_dict(_item) for _item in obj.get("files")] if obj.get("files") is not None else None,
            "html_url": obj.get("html_url"),
            "parents": [CommitMeta.from_dict(_item) for _item in obj.get("parents")] if obj.get("parents") is not None else None,
            "sha": obj.get("sha"),
            "stats": CommitStats.from_dict(obj.get("stats")) if obj.get("stats") is not None else None,
            "url": obj.get("url")
        })
        return _obj


