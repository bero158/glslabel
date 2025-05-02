# GetParcelStatusesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parcel_number** | **str** |  | [optional] 
**return_pod** | **bool** |  | [optional] 
**language_iso_code** | **str** |  | [optional] 
**pickup_date_to** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.get_parcel_statuses_request import GetParcelStatusesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetParcelStatusesRequest from a JSON string
get_parcel_statuses_request_instance = GetParcelStatusesRequest.from_json(json)
# print the JSON string representation of the object
print(GetParcelStatusesRequest.to_json())

# convert the object into a dict
get_parcel_statuses_request_dict = get_parcel_statuses_request_instance.to_dict()
# create an instance of GetParcelStatusesRequest from a dict
get_parcel_statuses_request_from_dict = GetParcelStatusesRequest.from_dict(get_parcel_statuses_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


