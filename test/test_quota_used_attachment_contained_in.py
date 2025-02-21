# coding: utf-8

"""
    Forgejo API

    This documentation describes the Forgejo API.

    The version of the OpenAPI document: 10.0.0-93-60eedb9+gitea-1.22.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from clientapi_forgejo.models.quota_used_attachment_contained_in import QuotaUsedAttachmentContainedIn

class TestQuotaUsedAttachmentContainedIn(unittest.TestCase):
    """QuotaUsedAttachmentContainedIn unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QuotaUsedAttachmentContainedIn:
        """Test QuotaUsedAttachmentContainedIn
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QuotaUsedAttachmentContainedIn`
        """
        model = QuotaUsedAttachmentContainedIn()
        if include_optional:
            return QuotaUsedAttachmentContainedIn(
                api_url = '',
                html_url = ''
            )
        else:
            return QuotaUsedAttachmentContainedIn(
        )
        """

    def testQuotaUsedAttachmentContainedIn(self):
        """Test QuotaUsedAttachmentContainedIn"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
