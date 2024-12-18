# ParcelInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_reference** | **str** |  | [optional] 
**parcel_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.parcel_info import ParcelInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ParcelInfo from a JSON string
parcel_info_instance = ParcelInfo.from_json(json)
# print the JSON string representation of the object
print(ParcelInfo.to_json())

# convert the object into a dict
parcel_info_dict = parcel_info_instance.to_dict()
# create an instance of ParcelInfo from a dict
parcel_info_from_dict = ParcelInfo.from_dict(parcel_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


