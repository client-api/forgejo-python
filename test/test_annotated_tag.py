# coding: utf-8

"""
    Forgejo API

    This documentation describes the Forgejo API.

    The version of the OpenAPI document: 10.0.0-93-60eedb9+gitea-1.22.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from clientapi_forgejo.models.annotated_tag import AnnotatedTag

class TestAnnotatedTag(unittest.TestCase):
    """AnnotatedTag unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AnnotatedTag:
        """Test AnnotatedTag
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AnnotatedTag`
        """
        model = AnnotatedTag()
        if include_optional:
            return AnnotatedTag(
                archive_download_count = clientapi_forgejo.models.tag_archive_download_count.TagArchiveDownloadCount(
                    tar_gz = 56, 
                    zip = 56, ),
                message = '',
                object = clientapi_forgejo.models.annotated_tag_object.AnnotatedTagObject(
                    sha = '', 
                    type = '', 
                    url = '', ),
                sha = '',
                tag = '',
                tagger = clientapi_forgejo.models.commit_user_contains_information_of_a_user_in_the_context_of_a_commit/.CommitUser contains information of a user in the context of a commit.(
                    date = '', 
                    email = '', 
                    name = '', ),
                url = '',
                verification = clientapi_forgejo.models.payload_commit_verification.PayloadCommitVerification(
                    payload = '', 
                    reason = '', 
                    signature = '', 
                    signer = clientapi_forgejo.models.payload_user.PayloadUser(
                        email = '', 
                        name = '', 
                        username = '', ), 
                    verified = True, )
            )
        else:
            return AnnotatedTag(
        )
        """

    def testAnnotatedTag(self):
        """Test AnnotatedTag"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
