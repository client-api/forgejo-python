# coding: utf-8

"""
    Forgejo API.

    This documentation describes the Forgejo API.

    The version of the OpenAPI document: 1.20.5+0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from clientapi_forgejo.api.activitypub_api import ActivitypubApi  # noqa: E501


class TestActivitypubApi(unittest.TestCase):
    """ActivitypubApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ActivitypubApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_activitypub_person(self) -> None:
        """Test case for activitypub_person

        Returns the Person actor for a user  # noqa: E501
        """
        pass

    def test_activitypub_person_inbox(self) -> None:
        """Test case for activitypub_person_inbox

        Send to the inbox  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
