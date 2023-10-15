# coding: utf-8

"""
    Forgejo API.

    This documentation describes the Forgejo API.

    The version of the OpenAPI document: 1.20.5+0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from clientapi_forgejo.models.wiki_page import WikiPage  # noqa: E501

class TestWikiPage(unittest.TestCase):
    """WikiPage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WikiPage:
        """Test WikiPage
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WikiPage`
        """
        model = WikiPage()  # noqa: E501
        if include_optional:
            return WikiPage(
                commit_count = 56,
                content_base64 = '',
                footer = '',
                html_url = '',
                last_commit = clientapi_forgejo.models.wiki_commit.WikiCommit(
                    author = clientapi_forgejo.models.commit_user_contains_information_of_a_user_in_the_context_of_a_commit/.CommitUser contains information of a user in the context of a commit.(
                        date = '', 
                        email = '', 
                        name = '', ), 
                    commiter = clientapi_forgejo.models.commit_user_contains_information_of_a_user_in_the_context_of_a_commit/.CommitUser contains information of a user in the context of a commit.(
                        date = '', 
                        email = '', 
                        name = '', ), 
                    message = '', 
                    sha = '', ),
                sidebar = '',
                sub_url = '',
                title = ''
            )
        else:
            return WikiPage(
        )
        """

    def testWikiPage(self):
        """Test WikiPage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()