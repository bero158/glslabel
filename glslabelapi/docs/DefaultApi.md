# openapi_client.DefaultApi

All URIs are relative to *https://api.mygls.cz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_parcel_list_post**](DefaultApi.md#get_parcel_list_post) | **POST** /GetParcelList | Get parcel(s) information by date ranges.
[**get_printed_labels_post**](DefaultApi.md#get_printed_labels_post) | **POST** /GetPrintedLabels | Get printed labels
[**prepare_labels_post**](DefaultApi.md#prepare_labels_post) | **POST** /PrepareLabels | Prepare labels for parcels
[**print_labels_post**](DefaultApi.md#print_labels_post) | **POST** /PrintLabels | Calls both PrepareLabels and GetPrintedLabels in one step


# **get_parcel_list_post**
> GetParcelListResponse get_parcel_list_post(get_parcel_list_request)

Get parcel(s) information by date ranges.

### Example


```python
import openapi_client
from openapi_client.models.get_parcel_list_request import GetParcelListRequest
from openapi_client.models.get_parcel_list_response import GetParcelListResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mygls.cz
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.mygls.cz"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    get_parcel_list_request = openapi_client.GetParcelListRequest() # GetParcelListRequest | 

    try:
        # Get parcel(s) information by date ranges.
        api_response = api_instance.get_parcel_list_post(get_parcel_list_request)
        print("The response of DefaultApi->get_parcel_list_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_parcel_list_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_parcel_list_request** | [**GetParcelListRequest**](GetParcelListRequest.md)|  | 

### Return type

[**GetParcelListResponse**](GetParcelListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Parcel list retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_printed_labels_post**
> GetPrintedLabelsResponse get_printed_labels_post(get_printed_labels_request)

Get printed labels

### Example


```python
import openapi_client
from openapi_client.models.get_printed_labels_request import GetPrintedLabelsRequest
from openapi_client.models.get_printed_labels_response import GetPrintedLabelsResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mygls.cz
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.mygls.cz"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    get_printed_labels_request = openapi_client.GetPrintedLabelsRequest() # GetPrintedLabelsRequest | 

    try:
        # Get printed labels
        api_response = api_instance.get_printed_labels_post(get_printed_labels_request)
        print("The response of DefaultApi->get_printed_labels_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_printed_labels_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_printed_labels_request** | [**GetPrintedLabelsRequest**](GetPrintedLabelsRequest.md)|  | 

### Return type

[**GetPrintedLabelsResponse**](GetPrintedLabelsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Printed labels retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **prepare_labels_post**
> PrepareLabelsResponse prepare_labels_post(prepare_labels_request)

Prepare labels for parcels

### Example


```python
import openapi_client
from openapi_client.models.prepare_labels_request import PrepareLabelsRequest
from openapi_client.models.prepare_labels_response import PrepareLabelsResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mygls.cz
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.mygls.cz"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    prepare_labels_request = openapi_client.PrepareLabelsRequest() # PrepareLabelsRequest | 

    try:
        # Prepare labels for parcels
        api_response = api_instance.prepare_labels_post(prepare_labels_request)
        print("The response of DefaultApi->prepare_labels_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->prepare_labels_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prepare_labels_request** | [**PrepareLabelsRequest**](PrepareLabelsRequest.md)|  | 

### Return type

[**PrepareLabelsResponse**](PrepareLabelsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Labels prepared successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **print_labels_post**
> GetPrintedLabelsResponse print_labels_post(print_labels_request)

Calls both PrepareLabels and GetPrintedLabels in one step

### Example


```python
import openapi_client
from openapi_client.models.get_printed_labels_response import GetPrintedLabelsResponse
from openapi_client.models.print_labels_request import PrintLabelsRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mygls.cz
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.mygls.cz"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    print_labels_request = openapi_client.PrintLabelsRequest() # PrintLabelsRequest | 

    try:
        # Calls both PrepareLabels and GetPrintedLabels in one step
        api_response = api_instance.print_labels_post(print_labels_request)
        print("The response of DefaultApi->print_labels_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->print_labels_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **print_labels_request** | [**PrintLabelsRequest**](PrintLabelsRequest.md)|  | 

### Return type

[**GetPrintedLabelsResponse**](GetPrintedLabelsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Print labels retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

