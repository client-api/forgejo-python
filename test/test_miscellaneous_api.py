# coding: utf-8

"""
    Forgejo API.

    This documentation describes the Forgejo API.

    The version of the OpenAPI document: 1.20.5+0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from clientapi_forgejo.api.miscellaneous_api import MiscellaneousApi  # noqa: E501


class TestMiscellaneousApi(unittest.TestCase):
    """MiscellaneousApi unit test stubs"""

    def setUp(self) -> None:
        self.api = MiscellaneousApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_get_gitignore_template_info(self) -> None:
        """Test case for get_gitignore_template_info

        Returns information about a gitignore template  # noqa: E501
        """
        pass

    def test_get_label_template_info(self) -> None:
        """Test case for get_label_template_info

        Returns all labels in a template  # noqa: E501
        """
        pass

    def test_get_license_template_info(self) -> None:
        """Test case for get_license_template_info

        Returns information about a license template  # noqa: E501
        """
        pass

    def test_get_node_info(self) -> None:
        """Test case for get_node_info

        Returns the nodeinfo of the Gitea application  # noqa: E501
        """
        pass

    def test_get_signing_key(self) -> None:
        """Test case for get_signing_key

        Get default signing-key.gpg  # noqa: E501
        """
        pass

    def test_get_version(self) -> None:
        """Test case for get_version

        Returns the version of the Gitea application  # noqa: E501
        """
        pass

    def test_list_gitignores_templates(self) -> None:
        """Test case for list_gitignores_templates

        Returns a list of all gitignore templates  # noqa: E501
        """
        pass

    def test_list_label_templates(self) -> None:
        """Test case for list_label_templates

        Returns a list of all label templates  # noqa: E501
        """
        pass

    def test_list_license_templates(self) -> None:
        """Test case for list_license_templates

        Returns a list of all license templates  # noqa: E501
        """
        pass

    def test_render_markdown(self) -> None:
        """Test case for render_markdown

        Render a markdown document as HTML  # noqa: E501
        """
        pass

    def test_render_markdown_raw(self) -> None:
        """Test case for render_markdown_raw

        Render raw markdown as HTML  # noqa: E501
        """
        pass

    def test_render_markup(self) -> None:
        """Test case for render_markup

        Render a markup document as HTML  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
