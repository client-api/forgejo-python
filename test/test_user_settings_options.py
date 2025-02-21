# coding: utf-8

"""
    Forgejo API

    This documentation describes the Forgejo API.

    The version of the OpenAPI document: 10.0.0-93-60eedb9+gitea-1.22.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from clientapi_forgejo.models.user_settings_options import UserSettingsOptions

class TestUserSettingsOptions(unittest.TestCase):
    """UserSettingsOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserSettingsOptions:
        """Test UserSettingsOptions
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserSettingsOptions`
        """
        model = UserSettingsOptions()
        if include_optional:
            return UserSettingsOptions(
                description = '',
                diff_view_style = '',
                enable_repo_unit_hints = True,
                full_name = '',
                hide_activity = True,
                hide_email = True,
                language = '',
                location = '',
                pronouns = '',
                theme = '',
                website = ''
            )
        else:
            return UserSettingsOptions(
        )
        """

    def testUserSettingsOptions(self):
        """Test UserSettingsOptions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
