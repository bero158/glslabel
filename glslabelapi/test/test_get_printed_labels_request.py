# coding: utf-8

"""
    MyGLS API

    API for MyGLS services

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.get_printed_labels_request import GetPrintedLabelsRequest

class TestGetPrintedLabelsRequest(unittest.TestCase):
    """GetPrintedLabelsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetPrintedLabelsRequest:
        """Test GetPrintedLabelsRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetPrintedLabelsRequest`
        """
        model = GetPrintedLabelsRequest()
        if include_optional:
            return GetPrintedLabelsRequest(
                username = '',
                password = [
                    56
                    ],
                parcel_id_list = [
                    56
                    ],
                print_position = 56,
                show_print_dialog = True,
                type_of_printer = ''
            )
        else:
            return GetPrintedLabelsRequest(
        )
        """

    def testGetPrintedLabelsRequest(self):
        """Test GetPrintedLabelsRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
