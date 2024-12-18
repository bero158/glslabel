# GetParcelListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**get_parcel_list_errors** | [**List[ErrorInfo]**](ErrorInfo.md) |  | [optional] 
**print_data_info_list** | [**List[PrintDataInfo]**](PrintDataInfo.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_parcel_list_response import GetParcelListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetParcelListResponse from a JSON string
get_parcel_list_response_instance = GetParcelListResponse.from_json(json)
# print the JSON string representation of the object
print(GetParcelListResponse.to_json())

# convert the object into a dict
get_parcel_list_response_dict = get_parcel_list_response_instance.to_dict()
# create an instance of GetParcelListResponse from a dict
get_parcel_list_response_from_dict = GetParcelListResponse.from_dict(get_parcel_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


