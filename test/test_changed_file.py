# coding: utf-8

"""
    Forgejo API

    This documentation describes the Forgejo API.

    The version of the OpenAPI document: 10.0.0-93-60eedb9+gitea-1.22.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from clientapi_forgejo.models.changed_file import ChangedFile

class TestChangedFile(unittest.TestCase):
    """ChangedFile unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ChangedFile:
        """Test ChangedFile
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ChangedFile`
        """
        model = ChangedFile()
        if include_optional:
            return ChangedFile(
                additions = 56,
                changes = 56,
                contents_url = '',
                deletions = 56,
                filename = '',
                html_url = '',
                previous_filename = '',
                raw_url = '',
                status = ''
            )
        else:
            return ChangedFile(
        )
        """

    def testChangedFile(self):
        """Test ChangedFile"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
