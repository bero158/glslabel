# GetParcelStatusesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_reference** | **str** |  | [optional] 
**delivery_country_code** | **str** |  | [optional] 
**delivery_zip_code** | **str** |  | [optional] 
**get_parcel_status_errors** | [**List[ErrorInfo]**](ErrorInfo.md) |  | [optional] 
**parcel_number** | **int** |  | [optional] 
**parcel_status_list** | [**List[ParcelStatus]**](ParcelStatus.md) |  | [optional] 
**pod** | **List[int]** |  | [optional] 
**weight** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.get_parcel_statuses_response import GetParcelStatusesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetParcelStatusesResponse from a JSON string
get_parcel_statuses_response_instance = GetParcelStatusesResponse.from_json(json)
# print the JSON string representation of the object
print(GetParcelStatusesResponse.to_json())

# convert the object into a dict
get_parcel_statuses_response_dict = get_parcel_statuses_response_instance.to_dict()
# create an instance of GetParcelStatusesResponse from a dict
get_parcel_statuses_response_from_dict = GetParcelStatusesResponse.from_dict(get_parcel_statuses_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


