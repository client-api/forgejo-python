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

from clientapi_forgejo.models.identity import Identity  # noqa: E501

class TestIdentity(unittest.TestCase):
    """Identity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Identity:
        """Test Identity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Identity`
        """
        model = Identity()  # noqa: E501
        if include_optional:
            return Identity(
                email = '',
                name = ''
            )
        else:
            return Identity(
        )
        """

    def testIdentity(self):
        """Test Identity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
