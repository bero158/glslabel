# coding: utf-8

"""
    MyGLS API

    API for MyGLS services

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.get_printed_labels_response import GetPrintedLabelsResponse

class TestGetPrintedLabelsResponse(unittest.TestCase):
    """GetPrintedLabelsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetPrintedLabelsResponse:
        """Test GetPrintedLabelsResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetPrintedLabelsResponse`
        """
        model = GetPrintedLabelsResponse()
        if include_optional:
            return GetPrintedLabelsResponse(
                labels = [
                    ''
                    ]
            )
        else:
            return GetPrintedLabelsResponse(
        )
        """

    def testGetPrintedLabelsResponse(self):
        """Test GetPrintedLabelsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
