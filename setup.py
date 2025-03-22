# coding: utf-8

"""
    Forgejo API

    This documentation describes the Forgejo API.

    The version of the OpenAPI document: 10.0.0-93-60eedb9+gitea-1.22.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "clientapi-forgejo"
VERSION = "1.1.1"
PYTHON_REQUIRES = ">= 3.8"
REQUIRES = [
    "urllib3 >= 1.25.3, < 3.0.0",
    "python-dateutil >= 2.8.2",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="Forgejo API",
    author="OpenAPI Generator community",
    author_email="team@openapitools.org",
    url="https://github.com/client-api/forgejo-python",
    keywords=["OpenAPI", "OpenAPI-Generator", "Forgejo API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="This file is distributed under the MIT license for the purpose of interoperability",
    long_description_content_type='text/markdown',
    long_description="""\
    This documentation describes the Forgejo API.
    """,  # noqa: E501
    package_data={"clientapi_forgejo": ["py.typed"]},
)