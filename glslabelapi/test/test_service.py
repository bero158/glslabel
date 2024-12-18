# coding: utf-8

"""
    MyGLS API

    API for MyGLS services

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.service import Service

class TestService(unittest.TestCase):
    """Service unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Service:
        """Test Service
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Service`
        """
        model = Service()
        if include_optional:
            return Service(
                adr_parameter = '',
                aos_parameter = '',
                cs1_parameter = '',
                dds_parameter = '',
                dpv_parameter = '',
                fds_parameter = '',
                fss_parameter = '',
                ins_parameter = '',
                mmp_parameter = '',
                psd_parameter = '',
                sds_parameter = '',
                sm1_parameter = '',
                sm2_parameter = '',
                szl_parameter = '',
                value = ''
            )
        else:
            return Service(
        )
        """

    def testService(self):
        """Test Service"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()