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

from clientapi_forgejo.models.user_settings_options import UserSettingsOptions  # noqa: E501

class TestUserSettingsOptions(unittest.TestCase):
    """UserSettingsOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserSettingsOptions:
        """Test UserSettingsOptions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserSettingsOptions`
        """
        model = UserSettingsOptions()  # noqa: E501
        if include_optional:
            return UserSettingsOptions(
                description = '',
                diff_view_style = '',
                full_name = '',
                hide_activity = True,
                hide_email = True,
                language = '',
                location = '',
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
