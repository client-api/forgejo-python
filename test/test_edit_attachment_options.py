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

from clientapi_forgejo.models.edit_attachment_options import EditAttachmentOptions  # noqa: E501

class TestEditAttachmentOptions(unittest.TestCase):
    """EditAttachmentOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EditAttachmentOptions:
        """Test EditAttachmentOptions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EditAttachmentOptions`
        """
        model = EditAttachmentOptions()  # noqa: E501
        if include_optional:
            return EditAttachmentOptions(
                name = ''
            )
        else:
            return EditAttachmentOptions(
        )
        """

    def testEditAttachmentOptions(self):
        """Test EditAttachmentOptions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()