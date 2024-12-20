import glslabelapi.openapi_client as openapi_client
from glslabelapi.openapi_client.rest import ApiException
from dynaconf import Dynaconf
import logging as LOGGER
import os
import hashlib
import time
from datetime import datetime
from dateutil.relativedelta import relativedelta
import argparse
import tempfile


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
            return api_response.labels,api_response.get_printed_labels_error_list
        except ApiException as e:
            LOGGER.error("Exception when calling DefaultApi->get_printed_labels_post: %s\n" % e)

    @staticmethod
    def savePdf(fName : str, data : list[int]):
        if data:
            with open(fName, 'wb') as file:
                file.write(bytearray(data))
        else:
            LOGGER.error("Label data is empty")

    @staticmethod
    def printPdf(data : list[int]):
        if data:
            fd,file = tempfile.mkstemp(suffix=".pdf") 
            os.write(fd,bytearray(data))
            os.close(fd)
            os.startfile(file, 'print')
            os.remove(file)
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
        # pickupDateFrom = None #self.formatPHPDate(pickupDates[0])
        # pickupDateTo = None #self.formatPHPDate(pickupDates[1])

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


    def findParcelDataInfo(self, parcelNr : int = None, parcelId : int = None, parcelList : list[openapi_client.Parcel] = None) -> openapi_client.PrintDataInfo:
        """Finds a parcel and rerurns Parcel"""
        if not parcelList:
            parcelList = self.getParcelList()
        printDataInfoList = self.getParcelList()
        try:
            printDataInfo = next(printDataInfo for printDataInfo in printDataInfoList if printDataInfo.parcel_number == parcelNr or printDataInfo.parcel_id == parcelId)
            return printDataInfo
        except StopIteration:
            LOGGER.error(f"Parcel not found")
            return None
    
    def parcelNr2parcelID(self, parcelNr : int = None, parcelId : int = None) -> int:
        """Converts Parcel Nr (number on the label) to Parcel ID (number in GLS database)
            Calls getParcelList() so use is limited to labels made less than 20 days ago.
        """
        printDataInfo = self.findParcelDataInfo(parcelNr=parcelNr, parcelId=parcelId)
        return printDataInfo.parcel_id
    
    def getParcel(self, parcelNr : int = None, parcelId : int = None) -> openapi_client.Parcel:
        printDataInfo = self.findParcelDataInfo(parcelNr=parcelNr, parcelId=parcelId)
        return printDataInfo.parcel
    
    def copyParcel(self, parcelIdList : list[int] = None) -> list[int]:
        """Copies parcel for printing because GLS doesn't support print a copy of the parcel which has been printed yet"""
        srcParcelList = []
        for parcelId in parcelIdList:
            srcParcelList.append(self.getParcel(parcelId=parcelId))
        request = openapi_client.PrepareLabelsRequest(
            Username=self.userName,
            Password=self.pwdH,
            ParcelList=srcParcelList
            )
        try:
            # Prepare labels for parcels
            api_response = self.apiInstance.prepare_labels_post(request)
            LOGGER.debug(f"The response of DefaultApi->prepare_labels_post: {api_response}")
            return map( lambda parcel_info : parcel_info.parcel_id, api_response.parcel_info_list)
        except Exception as e:
            LOGGER.error(f"Exception when calling DefaultApi->prepare_labels_post: {e}")

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
    parser.add_argument('-id','--parcelid', help="Parcel ID (number in GLS database)", type=int)
    parser.add_argument('-o','--output', help="Output filename")
    parser.add_argument('-p','--print', help="Print label(s)", action='store_true')
    parser.add_argument('-v', '--verbose', help="Show Debug messages", action='store_true') 
    
    args = parser.parse_args()
    
    level='DEBUG' if args.verbose else settings.LOGLEVEL
    format="%(asctime)s %(levelname)s:%(name)s:%(message)s" if level == 'DEBUG' else "%(levelname)s - %(message)s"
    LOGGER.basicConfig(level='DEBUG' if args.verbose else settings.LOGLEVEL, format=format)
    configuration = openapi_client.Configuration(host = settings.HOST)
    api = GLSApi(configuration, settings.USERNAME, settings.PASSWORD)
    labels = None
    parcelId = None
    if not args.output and not args.print:
        LOGGER.error(f"Output file or device must be specified (-o) or Print must be set (-p)") 
        return
    if args.parcelid:
        parcelId = args.parcelid
    elif args.parcelnr:
        parcelId = api.parcelNr2parcelID(args.parcelnr)
        if not parcelId:
            LOGGER.error(f"Parcel Nr {args.parcelnr} wasn't found in the database") 
            return
    else:
        LOGGER.error("Parcel Nr or Parcel ID must be specified")
        return
    labels,errors = api.getPrintedLabels( [parcelId], settings.TYPEOFPRINTER)
    if not labels and errors:
        if errors[0].error_code.actual_instance == 18:
            # Parcel label has already been generated
            # create a copy
            parcelIDs = api.copyParcel([parcelId])
            if parcelIDs:
                labels,errors = api.getPrintedLabels( parcelIDs, settings.TYPEOFPRINTER)

    if args.output:
        api.savePdf(args.output, labels)
    if args.print:
        api.printPdf(labels)



if __name__ == '__main__':
    main()