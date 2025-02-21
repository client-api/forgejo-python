# coding: utf-8

"""
    Forgejo API

    This documentation describes the Forgejo API.

    The version of the OpenAPI document: 10.0.0-93-60eedb9+gitea-1.22.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from clientapi_forgejo.models.quota_group import QuotaGroup

class TestQuotaGroup(unittest.TestCase):
    """QuotaGroup unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QuotaGroup:
        """Test QuotaGroup
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QuotaGroup`
        """
        model = QuotaGroup()
        if include_optional:
            return QuotaGroup(
                name = '',
                rules = [
                    clientapi_forgejo.models.quota_rule_info.QuotaRuleInfo(
                        limit = 56, 
                        name = '', 
                        subjects = [
                            ''
                            ], )
                    ]
            )
        else:
            return QuotaGroup(
        )
        """

    def testQuotaGroup(self):
        """Test QuotaGroup"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
