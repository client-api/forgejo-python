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

from clientapi_forgejo.models.update_file_options import UpdateFileOptions  # noqa: E501

class TestUpdateFileOptions(unittest.TestCase):
    """UpdateFileOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateFileOptions:
        """Test UpdateFileOptions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateFileOptions`
        """
        model = UpdateFileOptions()  # noqa: E501
        if include_optional:
            return UpdateFileOptions(
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
                from_path = '',
                message = '',
                new_branch = '',
                sha = '',
                signoff = True
            )
        else:
            return UpdateFileOptions(
                content = '',
                sha = '',
        )
        """

    def testUpdateFileOptions(self):
        """Test UpdateFileOptions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()