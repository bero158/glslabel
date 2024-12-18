import glslabelapi.openapi_client as openapi_client
from glslabelapi.openapi_client.rest import ApiException
from dynaconf import Dynaconf
import logging as LOGGER
from os import path as osp
import hashlib
import time
from datetime import datetime
from dateutil.relativedelta import relativedelta
import argparse


class GLSApi:
    userName : str
    pwdH : str
    apiClient : openapi_client.ApiClient
    apiInstance : openapi_client.DefaultApi

    def __init__(self, configuration, username : str, pwd : str):
        self.userName = username
        self.pwdH = self.hashPassword(pwd)
        self.apiClient = openapi_client.ApiClient(configuration)
        self.apiInstance = openapi_client.DefaultApi(self.apiClient)
        
    @staticmethod
    def hashPassword(pwd : str) -> list[int]:
        hashed = hashlib.sha512(pwd.encode()).digest()
        return list(hashed)

    @staticmethod
    def formatPHPDate(dt : time.struct_time) -> str:
        phpDate = "/Date(" + str(int(time.mktime(dt) * 1000)) + ")/"
        return phpDate

    def getPrintedLabels(self, parcelList : list[str], typeOfPrinter : str) -> list[int]:
        # Enter a context with an instance of the API client
        getPrintedLabelsRequest = openapi_client.GetPrintedLabelsRequest(
                Username=self.userName,
                Password=self.pwdH,
                ParcelIdList=parcelList,
                TypeOfPrinter=typeOfPrinter
        )
        try:
            # Get printed labels
            api_response = self.apiInstance.get_printed_labels_post(getPrintedLabelsRequest)
            LOGGER.info("The response of DefaultApi->get_printed_labels_post:\n")
            LOGGER.debug(api_response)
            if hasattr(api_response,"get_printed_labels_error_list") and api_response.get_printed_labels_error_list:
                LOGGER.error(api_response.get_printed_labels_error_list)
            return api_response.labels
        except ApiException as e:
            LOGGER.error("Exception when calling DefaultApi->get_printed_labels_post: %s\n" % e)

    @staticmethod
    def savePdf(fName : str, data : list[int]):
        if data:
            with open(fName, 'wb') as file:
                file.write(bytearray(data))
        else:
            LOGGER.error("Label data is empty")
                

    def getParcelList(self, printDates : tuple[time.struct_time,time.struct_time] = None) -> list[openapi_client.PrintDataInfo]:
        if not printDates:
            #set default values. Only 31 days can be selected.
            now=datetime.now() 
            minDate=now - relativedelta(days=20)
            maxDate=now + relativedelta(days=10)
            printDates=(tuple(minDate.timetuple()),tuple(maxDate.timetuple()))
        # If pickup is set then non-printed are filtered out.
        pickupDateFrom = None #self.formatPHPDate(pickupDates[0])
        pickupDateTo = None #self.formatPHPDate(pickupDates[1])

        #it's not print date, it's create date. Unprinted labgels are here too.
        printDateFrom = self.formatPHPDate(printDates[0]) 
        printDateTo = self.formatPHPDate(printDates[1])
        LOGGER.debug(f"Retrieving packages created between {printDateFrom} - {printDateTo}")
        getParcelListRequest = openapi_client.GetParcelListRequest(
                Username=self.userName,
                Password=self.pwdH,
                PickupDateFrom=None,
                PickupDateTo=None,
                PrintDateFrom=printDateFrom,
                PrintDateTo=printDateTo
        )
        try:
            # Get printed labels
            api_response = self.apiInstance.get_parcel_list_post(getParcelListRequest)
            LOGGER.info("The response of DefaultApi->get_parcel_list_post:\n")
            LOGGER.debug(api_response)
            LOGGER.info(f"Found {len(api_response.print_data_info_list)} packages:\n")
            
            return api_response.print_data_info_list
        except ApiException as e:
            LOGGER.error("Exception when calling DefaultApi->get_printed_labels_post: %s\n" % e)


    def parcelNr2parcelID(self, parcelNr : int) -> int:
        """Converts Parcel Nr (number on the label) to Parcel ID (number in GLS database)
            Calls getParcelList() so use is limited to labels made less than 20 days ago.
        """
        printDataInfoList = self.getParcelList()
        try:
            printDataInfo = next(printDataInfo for printDataInfo in printDataInfoList if printDataInfo.parcel_number == parcelNr)
        except StopIteration:
            LOGGER.error(f"Parcel Nr. not found")
            return None
            
        LOGGER.debug(f"Parcel ID: {printDataInfo.parcel_id}")
        return printDataInfo.parcel_id

    

def main():
    realPath = osp.join(osp.realpath(osp.dirname(__file__)))
    settings = Dynaconf(
        envvar_prefix="GLSLABEL",
        settings_files=[  osp.join(realPath,'settings.toml'), osp.join(realPath,'.secrets.toml')]
        )

    parser = argparse.ArgumentParser(exit_on_error=True,
                    prog='getprintedlabels',
                    description='This software downloads and store label through GLS API',
                    epilog="""
                    Credentials (USERNAME, PASSWORD) must be specified in .secrets.toml
                    Configuration is in settings.toml and settings.local.toml.
                    """)

    parser.add_argument('-nr','--parcelnr', help="Parcel Number (printed on label). Must be younger than 20 days", type=int)
    parser.add_argument('-id','--parcelid', help="Parcel ID (number in GLS database)", type=int)
    parser.add_argument('-o','--output', help="Output filename")
    parser.add_argument('-v', '--verbose', help="Show Debug messages", action='store_true') 
    
    args = parser.parse_args()
    
    level='DEBUG' if args.verbose else settings.LOGLEVEL
    format="%(asctime)s %(levelname)s:%(name)s:%(message)s" if level == 'DEBUG' else "%(levelname)s - %(message)s"
    LOGGER.basicConfig(level='DEBUG' if args.verbose else settings.LOGLEVEL, format=format)


    configuration = openapi_client.Configuration(host = settings.HOST)
    api = GLSApi(configuration, settings.USERNAME, settings.PASSWORD)
    labels = None
    if not args.output:
        LOGGER.error(f"Output must be specified (parameter -o)") 
        return
    
    if args.parcelid:
        labels = api.getPrintedLabels( [args.parcelid], settings.TYPEOFPRINTER)
    elif args.parcelnr:
        parcelId = api.parcelNr2parcelID(args.parcelnr)
        if not parcelId:
            LOGGER.error(f"Parcel Nr {args.parcelnr} wasn't found in the database") 
            return
        labels = api.getPrintedLabels( [parcelId], settings.TYPEOFPRINTER)
    else:
        LOGGER.error("Parcel Nr or Parcel ID must be specified")
        return

    api.savePdf(args.output, labels)


if __name__ == '__main__':
    main()