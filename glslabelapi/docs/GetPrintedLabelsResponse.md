# GetPrintedLabelsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | **List[int]** |  | [optional] 
**get_printed_labels_error_list** | [**List[ErrorInfo]**](ErrorInfo.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_printed_labels_response import GetPrintedLabelsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetPrintedLabelsResponse from a JSON string
get_printed_labels_response_instance = GetPrintedLabelsResponse.from_json(json)
# print the JSON string representation of the object
print(GetPrintedLabelsResponse.to_json())

# convert the object into a dict
get_printed_labels_response_dict = get_printed_labels_response_instance.to_dict()
# create an instance of GetPrintedLabelsResponse from a dict
get_printed_labels_response_from_dict = GetPrintedLabelsResponse.from_dict(get_printed_labels_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


