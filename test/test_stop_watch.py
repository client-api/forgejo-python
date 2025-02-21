# coding: utf-8

"""
    Forgejo API

    This documentation describes the Forgejo API.

    The version of the OpenAPI document: 10.0.0-93-60eedb9+gitea-1.22.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from clientapi_forgejo.models.stop_watch import StopWatch

class TestStopWatch(unittest.TestCase):
    """StopWatch unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StopWatch:
        """Test StopWatch
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StopWatch`
        """
        model = StopWatch()
        if include_optional:
            return StopWatch(
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                duration = '',
                issue_index = 56,
                issue_title = '',
                repo_name = '',
                repo_owner_name = '',
                seconds = 56
            )
        else:
            return StopWatch(
        )
        """

    def testStopWatch(self):
        """Test StopWatch"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
