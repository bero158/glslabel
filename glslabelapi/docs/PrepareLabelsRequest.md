# PrepareLabelsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | [optional] 
**password** | **List[int]** |  | [optional] 
**parcel_list** | [**List[Parcel]**](Parcel.md) |  | [optional] 

## Example

```python
from openapi_client.models.prepare_labels_request import PrepareLabelsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PrepareLabelsRequest from a JSON string
prepare_labels_request_instance = PrepareLabelsRequest.from_json(json)
# print the JSON string representation of the object
print(PrepareLabelsRequest.to_json())

# convert the object into a dict
prepare_labels_request_dict = prepare_labels_request_instance.to_dict()
# create an instance of PrepareLabelsRequest from a dict
prepare_labels_request_from_dict = PrepareLabelsRequest.from_dict(prepare_labels_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


