# coding: utf-8

"""
    Forgejo API

    This documentation describes the Forgejo API.

    The version of the OpenAPI document: 10.0.0-93-60eedb9+gitea-1.22.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from clientapi_forgejo.models.external_wiki import ExternalWiki

class TestExternalWiki(unittest.TestCase):
    """ExternalWiki unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ExternalWiki:
        """Test ExternalWiki
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ExternalWiki`
        """
        model = ExternalWiki()
        if include_optional:
            return ExternalWiki(
                external_wiki_url = ''
            )
        else:
            return ExternalWiki(
        )
        """

    def testExternalWiki(self):
        """Test ExternalWiki"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
