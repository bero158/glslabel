# PrintLabelsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | **List[int]** |  | [optional] 
**print_labels_error_list** | [**List[ErrorInfo]**](ErrorInfo.md) |  | [optional] 
**print_labels_info_list** | [**List[ParcelInfo]**](ParcelInfo.md) |  | [optional] 

## Example

```python
from openapi_client.models.print_labels_response import PrintLabelsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PrintLabelsResponse from a JSON string
print_labels_response_instance = PrintLabelsResponse.from_json(json)
# print the JSON string representation of the object
print(PrintLabelsResponse.to_json())

# convert the object into a dict
print_labels_response_dict = print_labels_response_instance.to_dict()
# create an instance of PrintLabelsResponse from a dict
print_labels_response_from_dict = PrintLabelsResponse.from_dict(print_labels_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


