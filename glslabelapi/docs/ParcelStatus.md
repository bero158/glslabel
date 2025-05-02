# ParcelStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**depot_city** | **str** |  | [optional] 
**depot_number** | **str** |  | [optional] 
**status_code** | **str** |  | [optional] 
**status_date** | [**datetime**](DateTime.md) |  | [optional] 
**status_description** | **str** |  | [optional] 
**status_info** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.parcel_status import ParcelStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ParcelStatus from a JSON string
parcel_status_instance = ParcelStatus.from_json(json)
# print the JSON string representation of the object
print(ParcelStatus.to_json())

# convert the object into a dict
parcel_status_dict = parcel_status_instance.to_dict()
# create an instance of ParcelStatus from a dict
parcel_status_from_dict = ParcelStatus.from_dict(parcel_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


