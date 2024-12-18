# coding: utf-8

"""
    MyGLS API

    API for MyGLS services

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.get_parcel_list_request import GetParcelListRequest

class TestGetParcelListRequest(unittest.TestCase):
    """GetParcelListRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetParcelListRequest:
        """Test GetParcelListRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetParcelListRequest`
        """
        model = GetParcelListRequest()
        if include_optional:
            return GetParcelListRequest(
                pickup_date_from = '',
                pickup_date_to = '',
                print_date_from = '',
                print_date_to = ''
            )
        else:
            return GetParcelListRequest(
        )
        """

    def testGetParcelListRequest(self):
        """Test GetParcelListRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()