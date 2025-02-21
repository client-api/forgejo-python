# coding: utf-8

"""
    Forgejo API

    This documentation describes the Forgejo API.

    The version of the OpenAPI document: 10.0.0-93-60eedb9+gitea-1.22.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from clientapi_forgejo.models.add_time_option import AddTimeOption

class TestAddTimeOption(unittest.TestCase):
    """AddTimeOption unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AddTimeOption:
        """Test AddTimeOption
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AddTimeOption`
        """
        model = AddTimeOption()
        if include_optional:
            return AddTimeOption(
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                time = 56,
                user_name = ''
            )
        else:
            return AddTimeOption(
                time = 56,
        )
        """

    def testAddTimeOption(self):
        """Test AddTimeOption"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
