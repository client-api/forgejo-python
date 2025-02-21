# coding: utf-8

"""
    Forgejo API

    This documentation describes the Forgejo API.

    The version of the OpenAPI document: 10.0.0-93-60eedb9+gitea-1.22.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from clientapi_forgejo.models.create_file_options import CreateFileOptions

class TestCreateFileOptions(unittest.TestCase):
    """CreateFileOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateFileOptions:
        """Test CreateFileOptions
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateFileOptions`
        """
        model = CreateFileOptions()
        if include_optional:
            return CreateFileOptions(
                author = clientapi_forgejo.models.identity.Identity(
                    email = '', 
                    name = '', ),
                branch = '',
                committer = clientapi_forgejo.models.identity.Identity(
                    email = '', 
                    name = '', ),
                content = '',
                dates = clientapi_forgejo.models.commit_date_options.CommitDateOptions(
                    author = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    committer = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                message = '',
                new_branch = '',
                signoff = True
            )
        else:
            return CreateFileOptions(
                content = '',
        )
        """

    def testCreateFileOptions(self):
        """Test CreateFileOptions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
