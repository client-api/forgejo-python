# coding: utf-8

"""
    Forgejo API

    This documentation describes the Forgejo API.

    The version of the OpenAPI document: 10.0.0-93-60eedb9+gitea-1.22.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from clientapi_forgejo.models.timeline_comment import TimelineComment

class TestTimelineComment(unittest.TestCase):
    """TimelineComment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TimelineComment:
        """Test TimelineComment
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TimelineComment`
        """
        model = TimelineComment()
        if include_optional:
            return TimelineComment(
                assignee = clientapi_forgejo.models.user.User(
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
                assignee_team = clientapi_forgejo.models.team.Team(
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
                    units_map = {"repo.code":"read","repo.ext_issues":"none","repo.ext_wiki":"none","repo.issues":"write","repo.projects":"none","repo.pulls":"owner","repo.releases":"none","repo.wiki":"admin"}, ),
                body = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                dependent_issue = clientapi_forgejo.models.issue.Issue(
                    assets = [
                        clientapi_forgejo.models.attachment.Attachment(
                            browser_download_url = '', 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            download_count = 56, 
                            id = 56, 
                            name = '', 
                            size = 56, 
                            type = 'attachment', 
                            uuid = '', )
                        ], 
                    assignee = clientapi_forgejo.models.user.User(
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
                    assignees = [
                        clientapi_forgejo.models.user.User(
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
                            website = '', )
                        ], 
                    body = '', 
                    closed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    comments = 56, 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    due_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    html_url = '', 
                    id = 56, 
                    is_locked = True, 
                    labels = [
                        clientapi_forgejo.models.label.Label(
                            color = '00aabb', 
                            description = '', 
                            exclusive = False, 
                            id = 56, 
                            is_archived = False, 
                            name = '', 
                            url = '', )
                        ], 
                    milestone = clientapi_forgejo.models.milestone.Milestone(
                        closed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        closed_issues = 56, 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        description = '', 
                        due_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        id = 56, 
                        open_issues = 56, 
                        state = '', 
                        title = '', 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                    number = 56, 
                    original_author = '', 
                    original_author_id = 56, 
                    pin_order = 56, 
                    pull_request = clientapi_forgejo.models.pull_request_meta.PullRequestMeta(
                        draft = True, 
                        html_url = '', 
                        merged = True, 
                        merged_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                    ref = '', 
                    repository = clientapi_forgejo.models.repository_meta.RepositoryMeta(
                        full_name = '', 
                        id = 56, 
                        name = '', 
                        owner = '', ), 
                    state = '', 
                    title = '', 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    url = '', 
                    user = , ),
                html_url = '',
                id = 56,
                issue_url = '',
                label = clientapi_forgejo.models.label.Label(
                    color = '00aabb', 
                    description = '', 
                    exclusive = False, 
                    id = 56, 
                    is_archived = False, 
                    name = '', 
                    url = '', ),
                milestone = clientapi_forgejo.models.milestone.Milestone(
                    closed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    closed_issues = 56, 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    description = '', 
                    due_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    id = 56, 
                    open_issues = 56, 
                    state = '', 
                    title = '', 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                new_ref = '',
                new_title = '',
                old_milestone = clientapi_forgejo.models.milestone.Milestone(
                    closed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    closed_issues = 56, 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    description = '', 
                    due_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    id = 56, 
                    open_issues = 56, 
                    state = '', 
                    title = '', 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                old_project_id = 56,
                old_ref = '',
                old_title = '',
                project_id = 56,
                pull_request_url = '',
                ref_action = '',
                ref_comment = clientapi_forgejo.models.comment.Comment(
                    assets = [
                        clientapi_forgejo.models.attachment.Attachment(
                            browser_download_url = '', 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            download_count = 56, 
                            id = 56, 
                            name = '', 
                            size = 56, 
                            type = 'attachment', 
                            uuid = '', )
                        ], 
                    body = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    html_url = '', 
                    id = 56, 
                    issue_url = '', 
                    original_author = '', 
                    original_author_id = 56, 
                    pull_request_url = '', 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    user = clientapi_forgejo.models.user.User(
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
                        website = '', ), ),
                ref_commit_sha = '',
                ref_issue = clientapi_forgejo.models.issue.Issue(
                    assets = [
                        clientapi_forgejo.models.attachment.Attachment(
                            browser_download_url = '', 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            download_count = 56, 
                            id = 56, 
                            name = '', 
                            size = 56, 
                            type = 'attachment', 
                            uuid = '', )
                        ], 
                    assignee = clientapi_forgejo.models.user.User(
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
                    assignees = [
                        clientapi_forgejo.models.user.User(
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
                            website = '', )
                        ], 
                    body = '', 
                    closed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    comments = 56, 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    due_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    html_url = '', 
                    id = 56, 
                    is_locked = True, 
                    labels = [
                        clientapi_forgejo.models.label.Label(
                            color = '00aabb', 
                            description = '', 
                            exclusive = False, 
                            id = 56, 
                            is_archived = False, 
                            name = '', 
                            url = '', )
                        ], 
                    milestone = clientapi_forgejo.models.milestone.Milestone(
                        closed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        closed_issues = 56, 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        description = '', 
                        due_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        id = 56, 
                        open_issues = 56, 
                        state = '', 
                        title = '', 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                    number = 56, 
                    original_author = '', 
                    original_author_id = 56, 
                    pin_order = 56, 
                    pull_request = clientapi_forgejo.models.pull_request_meta.PullRequestMeta(
                        draft = True, 
                        html_url = '', 
                        merged = True, 
                        merged_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                    ref = '', 
                    repository = clientapi_forgejo.models.repository_meta.RepositoryMeta(
                        full_name = '', 
                        id = 56, 
                        name = '', 
                        owner = '', ), 
                    state = '', 
                    title = '', 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    url = '', 
                    user = , ),
                removed_assignee = True,
                resolve_doer = clientapi_forgejo.models.user.User(
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
                review_id = 56,
                tracked_time = clientapi_forgejo.models.tracked_time.TrackedTime(
                    created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    id = 56, 
                    issue = clientapi_forgejo.models.issue.Issue(
                        assets = [
                            clientapi_forgejo.models.attachment.Attachment(
                                browser_download_url = '', 
                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                download_count = 56, 
                                id = 56, 
                                name = '', 
                                size = 56, 
                                type = 'attachment', 
                                uuid = '', )
                            ], 
                        assignee = clientapi_forgejo.models.user.User(
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
                        assignees = [
                            clientapi_forgejo.models.user.User(
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
                                website = '', )
                            ], 
                        body = '', 
                        closed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        comments = 56, 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        due_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        html_url = '', 
                        id = 56, 
                        is_locked = True, 
                        labels = [
                            clientapi_forgejo.models.label.Label(
                                color = '00aabb', 
                                description = '', 
                                exclusive = False, 
                                id = 56, 
                                is_archived = False, 
                                name = '', 
                                url = '', )
                            ], 
                        milestone = clientapi_forgejo.models.milestone.Milestone(
                            closed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            closed_issues = 56, 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            description = '', 
                            due_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            id = 56, 
                            open_issues = 56, 
                            state = '', 
                            title = '', 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                        number = 56, 
                        original_author = '', 
                        original_author_id = 56, 
                        pin_order = 56, 
                        pull_request = clientapi_forgejo.models.pull_request_meta.PullRequestMeta(
                            draft = True, 
                            html_url = '', 
                            merged = True, 
                            merged_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                        ref = '', 
                        repository = clientapi_forgejo.models.repository_meta.RepositoryMeta(
                            full_name = '', 
                            id = 56, 
                            name = '', 
                            owner = '', ), 
                        state = '', 
                        title = '', 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        url = '', 
                        user = , ), 
                    issue_id = 56, 
                    time = 56, 
                    user_id = 56, 
                    user_name = '', ),
                type = '',
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                user = clientapi_forgejo.models.user.User(
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
                    website = '', )
            )
        else:
            return TimelineComment(
        )
        """

    def testTimelineComment(self):
        """Test TimelineComment"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
