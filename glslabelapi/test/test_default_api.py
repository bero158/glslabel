# coding: utf-8

"""
    MyGLS API

    API for MyGLS services

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.default_api import DefaultApi


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DefaultApi()

    def tearDown(self) -> None:
        pass

    def test_get_printed_labels_post(self) -> None:
        """Test case for get_printed_labels_post

        Get printed labels
        """
        pass

    def test_prepare_labels_post(self) -> None:
        """Test case for prepare_labels_post

        Prepare labels for parcels
        """
        pass


if __name__ == '__main__':
    unittest.main()
