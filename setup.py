# coding: utf-8

"""
    Puupee API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0.0
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "puupee-api"
VERSION = "${VERSION}"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.25.3", "six >= 1.10", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Puupee API",
    author="OpenAPI Generator community",
    author_email="team@openapitools.org",
    url="https://github.com/jiejie-dev/puupee-api-python",
    keywords=["OpenAPI", "OpenAPI-Generator", "Puupee API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description="""\
    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501
    """
)
