# PrintLabelsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | [optional] 
**password** | **List[int]** |  | [optional] 
**parcel_list** | [**List[Parcel]**](Parcel.md) |  | [optional] 
**print_position** | **int** |  | [optional] 
**show_print_dialog** | **bool** |  | [optional] 
**type_of_printer** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.print_labels_request import PrintLabelsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PrintLabelsRequest from a JSON string
print_labels_request_instance = PrintLabelsRequest.from_json(json)
# print the JSON string representation of the object
print(PrintLabelsRequest.to_json())

# convert the object into a dict
print_labels_request_dict = print_labels_request_instance.to_dict()
# create an instance of PrintLabelsRequest from a dict
print_labels_request_from_dict = PrintLabelsRequest.from_dict(print_labels_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


