# GetPrintedLabelsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | [optional] 
**password** | **List[int]** |  | [optional] 
**parcel_id_list** | **List[int]** |  | [optional] 
**print_position** | **int** |  | [optional] 
**show_print_dialog** | **bool** |  | [optional] 
**type_of_printer** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.get_printed_labels_request import GetPrintedLabelsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetPrintedLabelsRequest from a JSON string
get_printed_labels_request_instance = GetPrintedLabelsRequest.from_json(json)
# print the JSON string representation of the object
print(GetPrintedLabelsRequest.to_json())

# convert the object into a dict
get_printed_labels_request_dict = get_printed_labels_request_instance.to_dict()
# create an instance of GetPrintedLabelsRequest from a dict
get_printed_labels_request_from_dict = GetPrintedLabelsRequest.from_dict(get_printed_labels_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


