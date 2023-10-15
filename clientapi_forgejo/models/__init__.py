# coding: utf-8

# flake8: noqa
"""
    Forgejo API.

    This documentation describes the Forgejo API.

    The version of the OpenAPI document: 1.20.5+0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from clientapi_forgejo.models.api_error import APIError
from clientapi_forgejo.models.access_token import AccessToken
from clientapi_forgejo.models.activity import Activity
from clientapi_forgejo.models.activity_pub import ActivityPub
from clientapi_forgejo.models.add_collaborator_option import AddCollaboratorOption
from clientapi_forgejo.models.add_time_option import AddTimeOption
from clientapi_forgejo.models.annotated_tag import AnnotatedTag
from clientapi_forgejo.models.annotated_tag_object import AnnotatedTagObject
from clientapi_forgejo.models.attachment import Attachment
from clientapi_forgejo.models.blocked_user import BlockedUser
from clientapi_forgejo.models.branch import Branch
from clientapi_forgejo.models.branch_protection import BranchProtection
from clientapi_forgejo.models.change_file_operation import ChangeFileOperation
from clientapi_forgejo.models.change_files_options import ChangeFilesOptions
from clientapi_forgejo.models.changed_file import ChangedFile
from clientapi_forgejo.models.combined_status import CombinedStatus
from clientapi_forgejo.models.comment import Comment
from clientapi_forgejo.models.commit import Commit
from clientapi_forgejo.models.commit_affected_files import CommitAffectedFiles
from clientapi_forgejo.models.commit_date_options import CommitDateOptions
from clientapi_forgejo.models.commit_meta import CommitMeta
from clientapi_forgejo.models.commit_stats import CommitStats
from clientapi_forgejo.models.commit_status import CommitStatus
from clientapi_forgejo.models.commit_user import CommitUser
from clientapi_forgejo.models.contents_response import ContentsResponse
from clientapi_forgejo.models.create_access_token_option import CreateAccessTokenOption
from clientapi_forgejo.models.create_branch_protection_option import CreateBranchProtectionOption
from clientapi_forgejo.models.create_branch_repo_option import CreateBranchRepoOption
from clientapi_forgejo.models.create_email_option import CreateEmailOption
from clientapi_forgejo.models.create_file_options import CreateFileOptions
from clientapi_forgejo.models.create_fork_option import CreateForkOption
from clientapi_forgejo.models.create_gpg_key_option import CreateGPGKeyOption
from clientapi_forgejo.models.create_hook_option import CreateHookOption
from clientapi_forgejo.models.create_issue_comment_option import CreateIssueCommentOption
from clientapi_forgejo.models.create_issue_option import CreateIssueOption
from clientapi_forgejo.models.create_key_option import CreateKeyOption
from clientapi_forgejo.models.create_label_option import CreateLabelOption
from clientapi_forgejo.models.create_milestone_option import CreateMilestoneOption
from clientapi_forgejo.models.create_o_auth2_application_options import CreateOAuth2ApplicationOptions
from clientapi_forgejo.models.create_org_option import CreateOrgOption
from clientapi_forgejo.models.create_pull_request_option import CreatePullRequestOption
from clientapi_forgejo.models.create_pull_review_comment import CreatePullReviewComment
from clientapi_forgejo.models.create_pull_review_options import CreatePullReviewOptions
from clientapi_forgejo.models.create_push_mirror_option import CreatePushMirrorOption
from clientapi_forgejo.models.create_release_option import CreateReleaseOption
from clientapi_forgejo.models.create_repo_option import CreateRepoOption
from clientapi_forgejo.models.create_status_option import CreateStatusOption
from clientapi_forgejo.models.create_tag_option import CreateTagOption
from clientapi_forgejo.models.create_team_option import CreateTeamOption
from clientapi_forgejo.models.create_user_option import CreateUserOption
from clientapi_forgejo.models.create_wiki_page_options import CreateWikiPageOptions
from clientapi_forgejo.models.cron import Cron
from clientapi_forgejo.models.delete_email_option import DeleteEmailOption
from clientapi_forgejo.models.delete_file_options import DeleteFileOptions
from clientapi_forgejo.models.deploy_key import DeployKey
from clientapi_forgejo.models.dismiss_pull_review_options import DismissPullReviewOptions
from clientapi_forgejo.models.edit_attachment_options import EditAttachmentOptions
from clientapi_forgejo.models.edit_branch_protection_option import EditBranchProtectionOption
from clientapi_forgejo.models.edit_deadline_option import EditDeadlineOption
from clientapi_forgejo.models.edit_git_hook_option import EditGitHookOption
from clientapi_forgejo.models.edit_hook_option import EditHookOption
from clientapi_forgejo.models.edit_issue_comment_option import EditIssueCommentOption
from clientapi_forgejo.models.edit_issue_option import EditIssueOption
from clientapi_forgejo.models.edit_label_option import EditLabelOption
from clientapi_forgejo.models.edit_milestone_option import EditMilestoneOption
from clientapi_forgejo.models.edit_org_option import EditOrgOption
from clientapi_forgejo.models.edit_pull_request_option import EditPullRequestOption
from clientapi_forgejo.models.edit_reaction_option import EditReactionOption
from clientapi_forgejo.models.edit_release_option import EditReleaseOption
from clientapi_forgejo.models.edit_repo_option import EditRepoOption
from clientapi_forgejo.models.edit_team_option import EditTeamOption
from clientapi_forgejo.models.edit_user_option import EditUserOption
from clientapi_forgejo.models.email import Email
from clientapi_forgejo.models.external_tracker import ExternalTracker
from clientapi_forgejo.models.external_wiki import ExternalWiki
from clientapi_forgejo.models.file_commit_response import FileCommitResponse
from clientapi_forgejo.models.file_delete_response import FileDeleteResponse
from clientapi_forgejo.models.file_links_response import FileLinksResponse
from clientapi_forgejo.models.file_response import FileResponse
from clientapi_forgejo.models.files_response import FilesResponse
from clientapi_forgejo.models.gpg_key import GPGKey
from clientapi_forgejo.models.gpg_key_email import GPGKeyEmail
from clientapi_forgejo.models.general_api_settings import GeneralAPISettings
from clientapi_forgejo.models.general_attachment_settings import GeneralAttachmentSettings
from clientapi_forgejo.models.general_repo_settings import GeneralRepoSettings
from clientapi_forgejo.models.general_ui_settings import GeneralUISettings
from clientapi_forgejo.models.generate_repo_option import GenerateRepoOption
from clientapi_forgejo.models.git_blob_response import GitBlobResponse
from clientapi_forgejo.models.git_entry import GitEntry
from clientapi_forgejo.models.git_hook import GitHook
from clientapi_forgejo.models.git_object import GitObject
from clientapi_forgejo.models.git_tree_response import GitTreeResponse
from clientapi_forgejo.models.gitignore_template_info import GitignoreTemplateInfo
from clientapi_forgejo.models.hook import Hook
from clientapi_forgejo.models.identity import Identity
from clientapi_forgejo.models.internal_tracker import InternalTracker
from clientapi_forgejo.models.issue import Issue
from clientapi_forgejo.models.issue_config import IssueConfig
from clientapi_forgejo.models.issue_config_contact_link import IssueConfigContactLink
from clientapi_forgejo.models.issue_config_validation import IssueConfigValidation
from clientapi_forgejo.models.issue_deadline import IssueDeadline
from clientapi_forgejo.models.issue_form_field import IssueFormField
from clientapi_forgejo.models.issue_labels_option import IssueLabelsOption
from clientapi_forgejo.models.issue_meta import IssueMeta
from clientapi_forgejo.models.issue_template import IssueTemplate
from clientapi_forgejo.models.label import Label
from clientapi_forgejo.models.label_template import LabelTemplate
from clientapi_forgejo.models.license_template_info import LicenseTemplateInfo
from clientapi_forgejo.models.licenses_template_list_entry import LicensesTemplateListEntry
from clientapi_forgejo.models.markdown_option import MarkdownOption
from clientapi_forgejo.models.markup_option import MarkupOption
from clientapi_forgejo.models.merge_pull_request_option import MergePullRequestOption
from clientapi_forgejo.models.migrate_repo_options import MigrateRepoOptions
from clientapi_forgejo.models.milestone import Milestone
from clientapi_forgejo.models.new_issue_pins_allowed import NewIssuePinsAllowed
from clientapi_forgejo.models.node_info import NodeInfo
from clientapi_forgejo.models.node_info_services import NodeInfoServices
from clientapi_forgejo.models.node_info_software import NodeInfoSoftware
from clientapi_forgejo.models.node_info_usage import NodeInfoUsage
from clientapi_forgejo.models.node_info_usage_users import NodeInfoUsageUsers
from clientapi_forgejo.models.note import Note
from clientapi_forgejo.models.notification_count import NotificationCount
from clientapi_forgejo.models.notification_subject import NotificationSubject
from clientapi_forgejo.models.notification_thread import NotificationThread
from clientapi_forgejo.models.o_auth2_application import OAuth2Application
from clientapi_forgejo.models.organization import Organization
from clientapi_forgejo.models.organization_permissions import OrganizationPermissions
from clientapi_forgejo.models.pr_branch_info import PRBranchInfo
from clientapi_forgejo.models.package import Package
from clientapi_forgejo.models.package_file import PackageFile
from clientapi_forgejo.models.payload_commit import PayloadCommit
from clientapi_forgejo.models.payload_commit_verification import PayloadCommitVerification
from clientapi_forgejo.models.payload_user import PayloadUser
from clientapi_forgejo.models.permission import Permission
from clientapi_forgejo.models.public_key import PublicKey
from clientapi_forgejo.models.pull_request import PullRequest
from clientapi_forgejo.models.pull_request_meta import PullRequestMeta
from clientapi_forgejo.models.pull_review import PullReview
from clientapi_forgejo.models.pull_review_comment import PullReviewComment
from clientapi_forgejo.models.pull_review_request_options import PullReviewRequestOptions
from clientapi_forgejo.models.push_mirror import PushMirror
from clientapi_forgejo.models.reaction import Reaction
from clientapi_forgejo.models.reference import Reference
from clientapi_forgejo.models.release import Release
from clientapi_forgejo.models.rename_user_option import RenameUserOption
from clientapi_forgejo.models.repo_collaborator_permission import RepoCollaboratorPermission
from clientapi_forgejo.models.repo_commit import RepoCommit
from clientapi_forgejo.models.repo_topic_options import RepoTopicOptions
from clientapi_forgejo.models.repo_transfer import RepoTransfer
from clientapi_forgejo.models.repository import Repository
from clientapi_forgejo.models.repository_meta import RepositoryMeta
from clientapi_forgejo.models.search_results import SearchResults
from clientapi_forgejo.models.server_version import ServerVersion
from clientapi_forgejo.models.stop_watch import StopWatch
from clientapi_forgejo.models.submit_pull_review_options import SubmitPullReviewOptions
from clientapi_forgejo.models.tag import Tag
from clientapi_forgejo.models.team import Team
from clientapi_forgejo.models.team_search200_response import TeamSearch200Response
from clientapi_forgejo.models.timeline_comment import TimelineComment
from clientapi_forgejo.models.topic_name import TopicName
from clientapi_forgejo.models.topic_response import TopicResponse
from clientapi_forgejo.models.tracked_time import TrackedTime
from clientapi_forgejo.models.transfer_repo_option import TransferRepoOption
from clientapi_forgejo.models.update_file_options import UpdateFileOptions
from clientapi_forgejo.models.user import User
from clientapi_forgejo.models.user_heatmap_data import UserHeatmapData
from clientapi_forgejo.models.user_search200_response import UserSearch200Response
from clientapi_forgejo.models.user_settings import UserSettings
from clientapi_forgejo.models.user_settings_options import UserSettingsOptions
from clientapi_forgejo.models.watch_info import WatchInfo
from clientapi_forgejo.models.wiki_commit import WikiCommit
from clientapi_forgejo.models.wiki_commit_list import WikiCommitList
from clientapi_forgejo.models.wiki_page import WikiPage
from clientapi_forgejo.models.wiki_page_meta_data import WikiPageMetaData
