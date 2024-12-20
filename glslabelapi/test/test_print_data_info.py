# coding: utf-8

"""
    MyGLS API

    API for MyGLS services

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.print_data_info import PrintDataInfo

class TestPrintDataInfo(unittest.TestCase):
    """PrintDataInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PrintDataInfo:
        """Test PrintDataInfo
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PrintDataInfo`
        """
        model = PrintDataInfo()
        if include_optional:
            return PrintDataInfo(
                client_reference = '',
                parcel_id = 56
            )
        else:
            return PrintDataInfo(
        )
        """

    def testPrintDataInfo(self):
        """Test PrintDataInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
