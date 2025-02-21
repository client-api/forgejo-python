# coding: utf-8

"""
    Forgejo API

    This documentation describes the Forgejo API.

    The version of the OpenAPI document: 10.0.0-93-60eedb9+gitea-1.22.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from clientapi_forgejo.models.organization_permissions import OrganizationPermissions

class TestOrganizationPermissions(unittest.TestCase):
    """OrganizationPermissions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrganizationPermissions:
        """Test OrganizationPermissions
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrganizationPermissions`
        """
        model = OrganizationPermissions()
        if include_optional:
            return OrganizationPermissions(
                can_create_repository = True,
                can_read = True,
                can_write = True,
                is_admin = True,
                is_owner = True
            )
        else:
            return OrganizationPermissions(
        )
        """

    def testOrganizationPermissions(self):
        """Test OrganizationPermissions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
