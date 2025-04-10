# coding: utf-8

"""
    Forgejo API

    This documentation describes the Forgejo API.

    The version of the OpenAPI document: 10.0.0-93-60eedb9+gitea-1.22.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from clientapi_forgejo.models.deploy_key import DeployKey

class TestDeployKey(unittest.TestCase):
    """DeployKey unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeployKey:
        """Test DeployKey
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeployKey`
        """
        model = DeployKey()
        if include_optional:
            return DeployKey(
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                fingerprint = '',
                id = 56,
                key = '',
                key_id = 56,
                read_only = True,
                repository = clientapi_forgejo.models.repository.Repository(
                    allow_fast_forward_only_merge = True, 
                    allow_merge_commits = True, 
                    allow_rebase = True, 
                    allow_rebase_explicit = True, 
                    allow_rebase_update = True, 
                    allow_squash_merge = True, 
                    archived = True, 
                    archived_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    avatar_url = '', 
                    clone_url = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    default_allow_maintainer_edit = True, 
                    default_branch = '', 
                    default_delete_branch_after_merge = True, 
                    default_merge_style = '', 
                    default_update_style = '', 
                    description = '', 
                    empty = True, 
                    external_tracker = clientapi_forgejo.models.external_tracker.ExternalTracker(
                        external_tracker_format = '', 
                        external_tracker_regexp_pattern = '', 
                        external_tracker_style = '', 
                        external_tracker_url = '', ), 
                    external_wiki = clientapi_forgejo.models.external_wiki.ExternalWiki(
                        external_wiki_url = '', ), 
                    fork = True, 
                    forks_count = 56, 
                    full_name = '', 
                    globally_editable_wiki = True, 
                    has_actions = True, 
                    has_issues = True, 
                    has_packages = True, 
                    has_projects = True, 
                    has_pull_requests = True, 
                    has_releases = True, 
                    has_wiki = True, 
                    html_url = '', 
                    id = 56, 
                    ignore_whitespace_conflicts = True, 
                    internal = True, 
                    internal_tracker = clientapi_forgejo.models.internal_tracker.InternalTracker(
                        allow_only_contributors_to_track_time = True, 
                        enable_issue_dependencies = True, 
                        enable_time_tracker = True, ), 
                    language = '', 
                    languages_url = '', 
                    link = '', 
                    mirror = True, 
                    mirror_interval = '', 
                    mirror_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    name = '', 
                    object_format_name = 'sha1', 
                    open_issues_count = 56, 
                    open_pr_counter = 56, 
                    original_url = '', 
                    owner = clientapi_forgejo.models.user.User(
                        active = True, 
                        avatar_url = '', 
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        description = '', 
                        email = '', 
                        followers_count = 56, 
                        following_count = 56, 
                        full_name = '', 
                        html_url = '', 
                        id = 56, 
                        is_admin = True, 
                        language = '', 
                        last_login = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        location = '', 
                        login = '', 
                        login_name = 'empty', 
                        prohibit_login = True, 
                        pronouns = '', 
                        restricted = True, 
                        source_id = 56, 
                        starred_repos_count = 56, 
                        visibility = '', 
                        website = '', ), 
                    parent = clientapi_forgejo.models.repository.Repository(
                        allow_fast_forward_only_merge = True, 
                        allow_merge_commits = True, 
                        allow_rebase = True, 
                        allow_rebase_explicit = True, 
                        allow_rebase_update = True, 
                        allow_squash_merge = True, 
                        archived = True, 
                        archived_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        avatar_url = '', 
                        clone_url = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        default_allow_maintainer_edit = True, 
                        default_branch = '', 
                        default_delete_branch_after_merge = True, 
                        default_merge_style = '', 
                        default_update_style = '', 
                        description = '', 
                        empty = True, 
                        fork = True, 
                        forks_count = 56, 
                        full_name = '', 
                        globally_editable_wiki = True, 
                        has_actions = True, 
                        has_issues = True, 
                        has_packages = True, 
                        has_projects = True, 
                        has_pull_requests = True, 
                        has_releases = True, 
                        has_wiki = True, 
                        html_url = '', 
                        id = 56, 
                        ignore_whitespace_conflicts = True, 
                        internal = True, 
                        language = '', 
                        languages_url = '', 
                        link = '', 
                        mirror = True, 
                        mirror_interval = '', 
                        mirror_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        name = '', 
                        object_format_name = 'sha1', 
                        open_issues_count = 56, 
                        open_pr_counter = 56, 
                        original_url = '', 
                        permissions = clientapi_forgejo.models.permission.Permission(
                            admin = True, 
                            pull = True, 
                            push = True, ), 
                        private = True, 
                        release_counter = 56, 
                        repo_transfer = clientapi_forgejo.models.repo_transfer.RepoTransfer(
                            doer = clientapi_forgejo.models.user.User(
                                active = True, 
                                avatar_url = '', 
                                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                description = '', 
                                email = '', 
                                followers_count = 56, 
                                following_count = 56, 
                                full_name = '', 
                                html_url = '', 
                                id = 56, 
                                is_admin = True, 
                                language = '', 
                                last_login = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                location = '', 
                                login = '', 
                                login_name = 'empty', 
                                prohibit_login = True, 
                                pronouns = '', 
                                restricted = True, 
                                source_id = 56, 
                                starred_repos_count = 56, 
                                visibility = '', 
                                website = '', ), 
                            recipient = , 
                            teams = [
                                clientapi_forgejo.models.team.Team(
                                    can_create_org_repo = True, 
                                    description = '', 
                                    id = 56, 
                                    includes_all_repositories = True, 
                                    name = '', 
                                    organization = clientapi_forgejo.models.organization.Organization(
                                        avatar_url = '', 
                                        description = '', 
                                        email = '', 
                                        full_name = '', 
                                        id = 56, 
                                        location = '', 
                                        name = '', 
                                        repo_admin_change_team_access = True, 
                                        username = '', 
                                        visibility = '', 
                                        website = '', ), 
                                    permission = 'none', 
                                    units = ["repo.code","repo.issues","repo.ext_issues","repo.wiki","repo.pulls","repo.releases","repo.projects","repo.ext_wiki"], 
                                    units_map = {"repo.code":"read","repo.ext_issues":"none","repo.ext_wiki":"none","repo.issues":"write","repo.projects":"none","repo.pulls":"owner","repo.releases":"none","repo.wiki":"admin"}, )
                                ], ), 
                        size = 56, 
                        ssh_url = '', 
                        stars_count = 56, 
                        template = True, 
                        topics = [
                            ''
                            ], 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        url = '', 
                        watchers_count = 56, 
                        website = '', 
                        wiki_branch = '', ), 
                    permissions = clientapi_forgejo.models.permission.Permission(
                        admin = True, 
                        pull = True, 
                        push = True, ), 
                    private = True, 
                    release_counter = 56, 
                    repo_transfer = clientapi_forgejo.models.repo_transfer.RepoTransfer(), 
                    size = 56, 
                    ssh_url = '', 
                    stars_count = 56, 
                    template = True, 
                    topics = [
                        ''
                        ], 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    url = '', 
                    watchers_count = 56, 
                    website = '', 
                    wiki_branch = '', ),
                title = '',
                url = ''
            )
        else:
            return DeployKey(
        )
        """

    def testDeployKey(self):
        """Test DeployKey"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
