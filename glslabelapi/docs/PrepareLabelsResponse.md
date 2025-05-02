# PrepareLabelsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parcel_info_list** | [**List[ParcelInfo]**](ParcelInfo.md) |  | [optional] 
**prepare_labels_error** | [**List[ErrorInfo]**](ErrorInfo.md) |  | [optional] 

## Example

```python
from openapi_client.models.prepare_labels_response import PrepareLabelsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PrepareLabelsResponse from a JSON string
prepare_labels_response_instance = PrepareLabelsResponse.from_json(json)
# print the JSON string representation of the object
print(PrepareLabelsResponse.to_json())

# convert the object into a dict
prepare_labels_response_dict = prepare_labels_response_instance.to_dict()
# create an instance of PrepareLabelsResponse from a dict
prepare_labels_response_from_dict = PrepareLabelsResponse.from_dict(prepare_labels_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


