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

from clientapi_forgejo.models.general_api_settings import GeneralAPISettings  # noqa: E501

class TestGeneralAPISettings(unittest.TestCase):
    """GeneralAPISettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GeneralAPISettings:
        """Test GeneralAPISettings
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GeneralAPISettings`
        """
        model = GeneralAPISettings()  # noqa: E501
        if include_optional:
            return GeneralAPISettings(
                default_git_trees_per_page = 56,
                default_max_blob_size = 56,
                default_paging_num = 56,
                max_response_items = 56
            )
        else:
            return GeneralAPISettings(
        )
        """

    def testGeneralAPISettings(self):
        """Test GeneralAPISettings"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()