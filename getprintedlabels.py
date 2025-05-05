import glslabel.glslabelapi.openapi_client as openapi_client
#import openapi_client as openapi_client
from dynaconf import Dynaconf
import logging as LOGGER
import os
import hashlib
import time
from datetime import datetime
from dateutil.relativedelta import relativedelta
import argparse
import tempfile
import locale

class GLSApi:
    """High level API for manipulating with GLS labels"""
    userName : str
    pwdH : str
    apiClient : openapi_client.ApiClient
    apiInstance : openapi_client.DefaultApi
    webshopEngine : str
    def __init__(self, username : str, pwd : str, host : str, webshopEngine : str):
        self.userName = username
        self.pwdH = self.hashPassword(pwd)
        configuration = openapi_client.Configuration(host = host)
        self.apiClient = openapi_client.ApiClient(configuration)
        self.apiInstance = openapi_client.DefaultApi(self.apiClient)
        self.webshopEngine = webshopEngine
    @staticmethod
    def hashPassword(pwd : str) -> list[int]:
        """GLS specific password hash"""
        hashed = hashlib.sha512(pwd.encode()).digest()
        return list(hashed)

    @staticmethod
    def formatPHPDate(dt : time.struct_time) -> str:
        """GLS specific date format"""
        phpDate = "/Date(" + str(int(time.mktime(dt) * 1000)) + ")/"
        return phpDate
    
    def printLabel(self, parcel : openapi_client.Parcel) -> tuple[list[int],str]:
        return self.printLabels([parcel])
    
    def printLabels(self,parcelList : list[openapi_client.Parcel]) -> tuple[list[int],str]:
        printLabelsRequest = openapi_client.PrintLabelsRequest(
            Username=self.userName,
            Password=self.pwdH,
            ParcelList=parcelList,
            WebshopEngine=self.webshopEngine)
        try:
            # Get printed labels
            api_response = self.apiInstance.print_labels_post(printLabelsRequest)
            LOGGER.info("The response of DefaultApi->printLabelsRequest:")
            LOGGER.debug(api_response)
            return api_response.labels,api_response.get_printed_labels_error_list
        except openapi_client.ApiException as e:
            LOGGER.error("Exception when calling DefaultApi->printLabelsRequest: %s" % e)

    def prepareLabel(self, parcel : openapi_client.Parcel) -> tuple[list[openapi_client.ParcelInfo],list[openapi_client.ErrorInfo]]:
        return self.prepareLabels([parcel])
    
    def prepareLabels(self, parcelList : list[openapi_client.Parcel]) -> tuple[list[openapi_client.ParcelInfo],list[openapi_client.ErrorInfo]]:
        """
        Creates a new parcel
        returns labels PDFs as array of integers
        """
        # Enter a context with an instance of the API client
        prepareLabelsRequest = openapi_client.PrepareLabelsRequest(
                Username=self.userName,
                Password=self.pwdH,
                ParcelList=parcelList,
                WebshopEngine=self.webshopEngine
        )
        try:
            # Get printed labels
            api_response : openapi_client.PrepareLabelsResponse = self.apiInstance.prepare_labels_post(prepareLabelsRequest)
            LOGGER.info("The response of DefaultApi->prepareLabelsRequest:")
            LOGGER.debug(api_response)
            return api_response.parcel_info_list,api_response.prepare_labels_error
            #return api_response.parcel_info_list,api_response.parcel_labels_error
        except openapi_client.ApiException as e:
            LOGGER.error("Exception when calling DefaultApi->prepareLabelsRequest: %s" % e)

    def getPrintedLabels(self, parcelList : list[str], typeOfPrinter : str) -> list[int]:
        """returns labels PDFs as array of integers"""
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
            LOGGER.info("The response of DefaultApi->get_printed_labels_post:")
            LOGGER.debug(api_response)
            return api_response.labels,api_response.get_printed_labels_error_list
        except openapi_client.ApiException as e:
            LOGGER.error("Exception when calling DefaultApi->get_printed_labels_post: %s" % e)

    @staticmethod
    def savePdf(fName : str, data : list[int]):
        """Save to file"""
        if data:
            with open(fName, 'wb') as file:
                file.write(bytearray(data))
        else:
            LOGGER.error("Label data is empty")

    def savePdfToTemp(data : list[int]) -> str:
        """Save to temp and returns filename """
        if data:
            fd,file = tempfile.mkstemp(suffix=".pdf") 
            if fd:
                os.write(fd,bytearray(data))
                os.close(fd)
                return file
        else:
            LOGGER.error("Label data is empty")

    @staticmethod
    def printPdf(data : list[int]):
        """Prints PDF(s)through a standard system printing service (on Windows opens Adobe Reader)"""
        if data:
            file = GLSApi.savePdfToTemp(data)
            os.startfile(file, 'print')
            os.remove(file)
        else:
            LOGGER.error("Label data is empty")
    
    @staticmethod
    def printGS(data: list[int], device: str):
        """Prints PDF(s) via GhostScript"""
        from ghostscript import Ghostscript, GhostscriptError
        encoding = locale.getpreferredencoding()
        if data:
            file = GLSApi.savePdfToTemp(data)
            args = [
                "-q",
                "-dQUIET",
                "-dPrinted",
                "-dBATCH",
                "-dNOSAFER",
                "-dNOPAUSE",
                "-dNOPROMPT",
                f"-sOutputFile=%printer%{device}",
                "-dNumCopies=1",
                "-dFitPage",
                "-dNOCANCEL",
                "-dAutoRotatePages=/All",
                "-sDEVICE=mswinpr2",
                file
            ]
            
            argsE = [a.encode(encoding) for a in args]
            try:
                Ghostscript(*argsE)
            except GhostscriptError as e:
                LOGGER.error(f"Ghostscript error: {e}")
            os.remove(file)
        else:
            LOGGER.error("Label data is empty")   
                     
    @staticmethod
    def getListOfAvailablePrinters():
        """Returns list of available printers"""
        from win32print import EnumPrinters, PRINTER_ENUM_LOCAL
        printers = EnumPrinters(PRINTER_ENUM_LOCAL)
        return printers

    def getParcelList(self, printDates : tuple[time.struct_time,time.struct_time] = None) -> list[openapi_client.PrintDataInfo]:
        """Returns list of parcels created in the selected interval"""
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
            LOGGER.info("The response of DefaultApi->get_parcel_list_post:")
            LOGGER.debug(api_response)
            LOGGER.info(f"Found {len(api_response.print_data_info_list)} packages:\n")
            
            return api_response.print_data_info_list
        except openapi_client.ApiException as e:
            LOGGER.error("Exception when calling DefaultApi->get_printed_labels_post: %s" % e)


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
        return printDataInfo.parcel_id if printDataInfo else None
    
    def getParcel(self, parcelNr : int = None, parcelId : int = None) -> openapi_client.Parcel:
        printDataInfo = self.findParcelDataInfo(parcelNr=parcelNr, parcelId=parcelId)
        return printDataInfo.parcel if printDataInfo else None
    
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
    parser.add_argument('-p','--print', help="Print label(s) through default PDF system handler", action='store_true')
    parser.add_argument('-lp','--listprinters', help="List of available printers. Currently for Windows only", action='store_true')
    parser.add_argument('-pg','--printgs', help="Print label(s) via GhostScript (GhostScript must be installed)", action='store_true')
    parser.add_argument('-pd','--printdev', help="Printing device for GhostScript", type=str)
    
    parser.add_argument('-v', '--verbose', help="Show Debug messages", action='store_true') 
    
    args = parser.parse_args()
    
    level='DEBUG' if args.verbose else settings.LOGLEVEL
    format="%(asctime)s %(levelname)s:%(name)s:%(message)s" if level == 'DEBUG' else "%(levelname)s - %(message)s"
    LOGGER.basicConfig(level='DEBUG' if args.verbose else settings.LOGLEVEL, format=format)
    api = GLSApi(settings.USERNAME, settings.PASSWORD, host = settings.HOST, webshopEngine=settings.WEBSHOP_ENGINE)
    labels = None
    parcelId = None
    if args.listprinters:
        printers = api.getListOfAvailablePrinters()
        for printer in printers:
            LOGGER.info(f"Printer: {printer[2]}")
        return
    if not args.output and not args.print and not args.printgs:
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
    if args.printgs:
        api.printGS(labels, args.printdev)
        

if __name__ == '__main__':
    main()