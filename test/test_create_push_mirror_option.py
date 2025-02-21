# coding: utf-8

"""
    Forgejo API

    This documentation describes the Forgejo API.

    The version of the OpenAPI document: 10.0.0-93-60eedb9+gitea-1.22.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from clientapi_forgejo.models.create_push_mirror_option import CreatePushMirrorOption

class TestCreatePushMirrorOption(unittest.TestCase):
    """CreatePushMirrorOption unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreatePushMirrorOption:
        """Test CreatePushMirrorOption
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreatePushMirrorOption`
        """
        model = CreatePushMirrorOption()
        if include_optional:
            return CreatePushMirrorOption(
                interval = '',
                remote_address = '',
                remote_password = '',
                remote_username = '',
                sync_on_commit = True,
                use_ssh = True
            )
        else:
            return CreatePushMirrorOption(
        )
        """

    def testCreatePushMirrorOption(self):
        """Test CreatePushMirrorOption"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
