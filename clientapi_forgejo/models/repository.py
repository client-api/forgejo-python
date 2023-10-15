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
from clientapi_forgejo.models.external_tracker import ExternalTracker
from clientapi_forgejo.models.external_wiki import ExternalWiki
from clientapi_forgejo.models.internal_tracker import InternalTracker
from clientapi_forgejo.models.permission import Permission
from clientapi_forgejo.models.repo_transfer import RepoTransfer
from clientapi_forgejo.models.user import User

class Repository(BaseModel):
    """
    Repository represents a repository  # noqa: E501
    """
    allow_merge_commits: Optional[StrictBool] = None
    allow_rebase: Optional[StrictBool] = None
    allow_rebase_explicit: Optional[StrictBool] = None
    allow_rebase_update: Optional[StrictBool] = None
    allow_squash_merge: Optional[StrictBool] = None
    archived: Optional[StrictBool] = None
    archived_at: Optional[datetime] = None
    avatar_url: Optional[StrictStr] = None
    clone_url: Optional[StrictStr] = None
    created_at: Optional[datetime] = None
    default_allow_maintainer_edit: Optional[StrictBool] = None
    default_branch: Optional[StrictStr] = None
    default_delete_branch_after_merge: Optional[StrictBool] = None
    default_merge_style: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    empty: Optional[StrictBool] = None
    external_tracker: Optional[ExternalTracker] = None
    external_wiki: Optional[ExternalWiki] = None
    fork: Optional[StrictBool] = None
    forks_count: Optional[StrictInt] = None
    full_name: Optional[StrictStr] = None
    has_actions: Optional[StrictBool] = None
    has_issues: Optional[StrictBool] = None
    has_packages: Optional[StrictBool] = None
    has_projects: Optional[StrictBool] = None
    has_pull_requests: Optional[StrictBool] = None
    has_releases: Optional[StrictBool] = None
    has_wiki: Optional[StrictBool] = None
    html_url: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    ignore_whitespace_conflicts: Optional[StrictBool] = None
    internal: Optional[StrictBool] = None
    internal_tracker: Optional[InternalTracker] = None
    language: Optional[StrictStr] = None
    languages_url: Optional[StrictStr] = None
    link: Optional[StrictStr] = None
    mirror: Optional[StrictBool] = None
    mirror_interval: Optional[StrictStr] = None
    mirror_updated: Optional[datetime] = None
    name: Optional[StrictStr] = None
    open_issues_count: Optional[StrictInt] = None
    open_pr_counter: Optional[StrictInt] = None
    original_url: Optional[StrictStr] = None
    owner: Optional[User] = None
    parent: Optional[Repository] = None
    permissions: Optional[Permission] = None
    private: Optional[StrictBool] = None
    release_counter: Optional[StrictInt] = None
    repo_transfer: Optional[RepoTransfer] = None
    size: Optional[StrictInt] = None
    ssh_url: Optional[StrictStr] = None
    stars_count: Optional[StrictInt] = None
    template: Optional[StrictBool] = None
    updated_at: Optional[datetime] = None
    url: Optional[StrictStr] = None
    watchers_count: Optional[StrictInt] = None
    website: Optional[StrictStr] = None
    __properties = ["allow_merge_commits", "allow_rebase", "allow_rebase_explicit", "allow_rebase_update", "allow_squash_merge", "archived", "archived_at", "avatar_url", "clone_url", "created_at", "default_allow_maintainer_edit", "default_branch", "default_delete_branch_after_merge", "default_merge_style", "description", "empty", "external_tracker", "external_wiki", "fork", "forks_count", "full_name", "has_actions", "has_issues", "has_packages", "has_projects", "has_pull_requests", "has_releases", "has_wiki", "html_url", "id", "ignore_whitespace_conflicts", "internal", "internal_tracker", "language", "languages_url", "link", "mirror", "mirror_interval", "mirror_updated", "name", "open_issues_count", "open_pr_counter", "original_url", "owner", "parent", "permissions", "private", "release_counter", "repo_transfer", "size", "ssh_url", "stars_count", "template", "updated_at", "url", "watchers_count", "website"]

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
    def from_json(cls, json_str: str) -> Repository:
        """Create an instance of Repository from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of external_tracker
        if self.external_tracker:
            _dict['external_tracker'] = self.external_tracker.to_dict()
        # override the default output from pydantic by calling `to_dict()` of external_wiki
        if self.external_wiki:
            _dict['external_wiki'] = self.external_wiki.to_dict()
        # override the default output from pydantic by calling `to_dict()` of internal_tracker
        if self.internal_tracker:
            _dict['internal_tracker'] = self.internal_tracker.to_dict()
        # override the default output from pydantic by calling `to_dict()` of owner
        if self.owner:
            _dict['owner'] = self.owner.to_dict()
        # override the default output from pydantic by calling `to_dict()` of parent
        if self.parent:
            _dict['parent'] = self.parent.to_dict()
        # override the default output from pydantic by calling `to_dict()` of permissions
        if self.permissions:
            _dict['permissions'] = self.permissions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of repo_transfer
        if self.repo_transfer:
            _dict['repo_transfer'] = self.repo_transfer.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Repository:
        """Create an instance of Repository from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Repository.parse_obj(obj)

        _obj = Repository.parse_obj({
            "allow_merge_commits": obj.get("allow_merge_commits"),
            "allow_rebase": obj.get("allow_rebase"),
            "allow_rebase_explicit": obj.get("allow_rebase_explicit"),
            "allow_rebase_update": obj.get("allow_rebase_update"),
            "allow_squash_merge": obj.get("allow_squash_merge"),
            "archived": obj.get("archived"),
            "archived_at": obj.get("archived_at"),
            "avatar_url": obj.get("avatar_url"),
            "clone_url": obj.get("clone_url"),
            "created_at": obj.get("created_at"),
            "default_allow_maintainer_edit": obj.get("default_allow_maintainer_edit"),
            "default_branch": obj.get("default_branch"),
            "default_delete_branch_after_merge": obj.get("default_delete_branch_after_merge"),
            "default_merge_style": obj.get("default_merge_style"),
            "description": obj.get("description"),
            "empty": obj.get("empty"),
            "external_tracker": ExternalTracker.from_dict(obj.get("external_tracker")) if obj.get("external_tracker") is not None else None,
            "external_wiki": ExternalWiki.from_dict(obj.get("external_wiki")) if obj.get("external_wiki") is not None else None,
            "fork": obj.get("fork"),
            "forks_count": obj.get("forks_count"),
            "full_name": obj.get("full_name"),
            "has_actions": obj.get("has_actions"),
            "has_issues": obj.get("has_issues"),
            "has_packages": obj.get("has_packages"),
            "has_projects": obj.get("has_projects"),
            "has_pull_requests": obj.get("has_pull_requests"),
            "has_releases": obj.get("has_releases"),
            "has_wiki": obj.get("has_wiki"),
            "html_url": obj.get("html_url"),
            "id": obj.get("id"),
            "ignore_whitespace_conflicts": obj.get("ignore_whitespace_conflicts"),
            "internal": obj.get("internal"),
            "internal_tracker": InternalTracker.from_dict(obj.get("internal_tracker")) if obj.get("internal_tracker") is not None else None,
            "language": obj.get("language"),
            "languages_url": obj.get("languages_url"),
            "link": obj.get("link"),
            "mirror": obj.get("mirror"),
            "mirror_interval": obj.get("mirror_interval"),
            "mirror_updated": obj.get("mirror_updated"),
            "name": obj.get("name"),
            "open_issues_count": obj.get("open_issues_count"),
            "open_pr_counter": obj.get("open_pr_counter"),
            "original_url": obj.get("original_url"),
            "owner": User.from_dict(obj.get("owner")) if obj.get("owner") is not None else None,
            "parent": Repository.from_dict(obj.get("parent")) if obj.get("parent") is not None else None,
            "permissions": Permission.from_dict(obj.get("permissions")) if obj.get("permissions") is not None else None,
            "private": obj.get("private"),
            "release_counter": obj.get("release_counter"),
            "repo_transfer": RepoTransfer.from_dict(obj.get("repo_transfer")) if obj.get("repo_transfer") is not None else None,
            "size": obj.get("size"),
            "ssh_url": obj.get("ssh_url"),
            "stars_count": obj.get("stars_count"),
            "template": obj.get("template"),
            "updated_at": obj.get("updated_at"),
            "url": obj.get("url"),
            "watchers_count": obj.get("watchers_count"),
            "website": obj.get("website")
        })
        return _obj

Repository.update_forward_refs()
