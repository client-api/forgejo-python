# coding: utf-8

"""
    Forgejo API

    This documentation describes the Forgejo API.

    The version of the OpenAPI document: 10.0.0-93-60eedb9+gitea-1.22.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from clientapi_forgejo.models.commit import Commit

class TestCommit(unittest.TestCase):
    """Commit unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Commit:
        """Test Commit
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Commit`
        """
        model = Commit()
        if include_optional:
            return Commit(
                author = clientapi_forgejo.models.user.User(
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
                commit = clientapi_forgejo.models.repo_commit_contains_information_of_a_commit_in_the_context_of_a_repository/.RepoCommit contains information of a commit in the context of a repository.(
                    author = clientapi_forgejo.models.commit_user_contains_information_of_a_user_in_the_context_of_a_commit/.CommitUser contains information of a user in the context of a commit.(
                        date = '', 
                        email = '', 
                        name = '', ), 
                    committer = clientapi_forgejo.models.commit_user_contains_information_of_a_user_in_the_context_of_a_commit/.CommitUser contains information of a user in the context of a commit.(
                        date = '', 
                        email = '', 
                        name = '', ), 
                    message = '', 
                    tree = clientapi_forgejo.models.commit_meta_contains_meta_information_of_a_commit_in_terms_of_api/.CommitMeta contains meta information of a commit in terms of API.(
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        sha = '', 
                        url = '', ), 
                    url = '', 
                    verification = clientapi_forgejo.models.payload_commit_verification.PayloadCommitVerification(
                        payload = '', 
                        reason = '', 
                        signature = '', 
                        signer = clientapi_forgejo.models.payload_user.PayloadUser(
                            email = '', 
                            name = '', 
                            username = '', ), 
                        verified = True, ), ),
                committer = clientapi_forgejo.models.user.User(
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
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                files = [
                    clientapi_forgejo.models.commit_affected_files.CommitAffectedFiles(
                        filename = '', 
                        status = '', )
                    ],
                html_url = '',
                parents = [
                    clientapi_forgejo.models.commit_meta_contains_meta_information_of_a_commit_in_terms_of_api/.CommitMeta contains meta information of a commit in terms of API.(
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        sha = '', 
                        url = '', )
                    ],
                sha = '',
                stats = clientapi_forgejo.models.commit_stats.CommitStats(
                    additions = 56, 
                    deletions = 56, 
                    total = 56, ),
                url = ''
            )
        else:
            return Commit(
        )
        """

    def testCommit(self):
        """Test Commit"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
