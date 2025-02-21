# coding: utf-8

"""
    Forgejo API

    This documentation describes the Forgejo API.

    The version of the OpenAPI document: 10.0.0-93-60eedb9+gitea-1.22.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from clientapi_forgejo.models.repo_create_release_attachment_request import RepoCreateReleaseAttachmentRequest

class TestRepoCreateReleaseAttachmentRequest(unittest.TestCase):
    """RepoCreateReleaseAttachmentRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RepoCreateReleaseAttachmentRequest:
        """Test RepoCreateReleaseAttachmentRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RepoCreateReleaseAttachmentRequest`
        """
        model = RepoCreateReleaseAttachmentRequest()
        if include_optional:
            return RepoCreateReleaseAttachmentRequest(
                attachment = bytes(b'blah'),
                external_url = ''
            )
        else:
            return RepoCreateReleaseAttachmentRequest(
        )
        """

    def testRepoCreateReleaseAttachmentRequest(self):
        """Test RepoCreateReleaseAttachmentRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
