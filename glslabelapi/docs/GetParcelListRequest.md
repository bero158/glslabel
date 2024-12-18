# GetParcelListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | [optional] 
**password** | **List[int]** |  | [optional] 
**pickup_date_from** | **str** |  | [optional] 
**pickup_date_to** | **str** |  | [optional] 
**print_date_from** | **str** |  | [optional] 
**print_date_to** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.get_parcel_list_request import GetParcelListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetParcelListRequest from a JSON string
get_parcel_list_request_instance = GetParcelListRequest.from_json(json)
# print the JSON string representation of the object
print(GetParcelListRequest.to_json())

# convert the object into a dict
get_parcel_list_request_dict = get_parcel_list_request_instance.to_dict()
# create an instance of GetParcelListRequest from a dict
get_parcel_list_request_from_dict = GetParcelListRequest.from_dict(get_parcel_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


