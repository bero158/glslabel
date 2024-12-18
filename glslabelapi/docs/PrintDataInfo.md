# PrintDataInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**b2_c_char** | **str** |  | [optional] 
**client_reference** | **str** |  | [optional] 
**depot** | **str** |  | [optional] 
**depot_number** | **str** |  | [optional] 
**displaylanguage** | **str** |  | [optional] 
**driver** | **str** |  | [optional] 
**parcel** | [**Parcel**](Parcel.md) |  | [optional] 
**parcel_id** | **int** |  | [optional] 
**parcel_number** | **int** |  | [optional] 
**parcel_number_with_checkdigit** | **int** |  | [optional] 
**sort** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.print_data_info import PrintDataInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PrintDataInfo from a JSON string
print_data_info_instance = PrintDataInfo.from_json(json)
# print the JSON string representation of the object
print(PrintDataInfo.to_json())

# convert the object into a dict
print_data_info_dict = print_data_info_instance.to_dict()
# create an instance of PrintDataInfo from a dict
print_data_info_from_dict = PrintDataInfo.from_dict(print_data_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


