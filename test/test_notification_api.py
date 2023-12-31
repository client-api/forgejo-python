# coding: utf-8

"""
    Forgejo API.

    This documentation describes the Forgejo API.

    The version of the OpenAPI document: 1.20.5+0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from clientapi_forgejo.api.notification_api import NotificationApi  # noqa: E501


class TestNotificationApi(unittest.TestCase):
    """NotificationApi unit test stubs"""

    def setUp(self) -> None:
        self.api = NotificationApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_notify_get_list(self) -> None:
        """Test case for notify_get_list

        List users's notification threads  # noqa: E501
        """
        pass

    def test_notify_get_repo_list(self) -> None:
        """Test case for notify_get_repo_list

        List users's notification threads on a specific repo  # noqa: E501
        """
        pass

    def test_notify_get_thread(self) -> None:
        """Test case for notify_get_thread

        Get notification thread by ID  # noqa: E501
        """
        pass

    def test_notify_new_available(self) -> None:
        """Test case for notify_new_available

        Check if unread notifications exist  # noqa: E501
        """
        pass

    def test_notify_read_list(self) -> None:
        """Test case for notify_read_list

        Mark notification threads as read, pinned or unread  # noqa: E501
        """
        pass

    def test_notify_read_repo_list(self) -> None:
        """Test case for notify_read_repo_list

        Mark notification threads as read, pinned or unread on a specific repo  # noqa: E501
        """
        pass

    def test_notify_read_thread(self) -> None:
        """Test case for notify_read_thread

        Mark notification thread as read by ID  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
