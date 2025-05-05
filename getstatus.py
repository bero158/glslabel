import glslabel.glslabelapi.openapi_client as openapi_client
from dynaconf import Dynaconf
import logging as LOGGER
import os
import argparse
from glslabel.getprintedlabels import GLSApi

class GLSApiStatus(GLSApi):
    """High level API for manipulating with GLS labels"""
    def getStatuses(self, ParcelNumber : str) -> list[openapi_client.ParcelStatus]:
        """Returns status of the parcel"""
        getStatusRequest = openapi_client.GetParcelStatusesRequest(
            Username=self.userName,
            Password=self.pwdH,
            ParcelNumber=ParcelNumber,
            return_pod=False
            )
        try:
            # Get printed labels
            api_response = self.apiInstance.get_parcel_statuses_post(getStatusRequest)
            LOGGER.info("The response of DefaultApi->getParcelStatus:")
            LOGGER.debug(api_response)
            return api_response.parcel_status_list
        except openapi_client.ApiException as e:
            LOGGER.error("Exception when calling DefaultApi->getParcelStatus: %s" % e)
    
    
def main():
    realPath = os.path.join(os.path.realpath(os.path.dirname(__file__)))
    settings = Dynaconf(
        envvar_prefix="GLSLABEL",
        settings_files=[  os.path.join(realPath,'settings.toml'), os.path.join(realPath,'.secrets.toml')]
        )

    parser = argparse.ArgumentParser(exit_on_error=True,
                    prog='getprintedlabels',
                    description='This software downloads and store label through GLS API',
                    epilog="""
                    Credentials (USERNAME, PASSWORD) must be specified in .secrets.toml
                    Configuration is in settings.toml and settings.local.toml.
                    """)

    parser.add_argument('-nr','--parcelnr', help="Parcel Number (printed on label). Must be younger than 20 days", type=int)
    parser.add_argument('-sc','--statuscode', help="Get status of a specific status code", type=int)
    parser.add_argument('-v', '--verbose', help="Show Debug messages", action='store_true') 
    
    args = parser.parse_args()
    
    level='DEBUG' if args.verbose else settings.LOGLEVEL
    format="%(asctime)s %(levelname)s:%(name)s:%(message)s" if level == 'DEBUG' else "%(levelname)s - %(message)s"
    LOGGER.basicConfig(level='DEBUG' if args.verbose else settings.LOGLEVEL, format=format)
    api = GLSApiStatus(settings.USERNAME, settings.PASSWORD, host = settings.HOST, webshopEngine=settings.WEBSHOP_ENGINE)
    status = api.getStatuses(str(args.parcelnr))
    if args.statuscode:
        status = list(filter(lambda s: s.status_code == str(args.statuscode), status))
    print(status)

if __name__ == '__main__':
    main()