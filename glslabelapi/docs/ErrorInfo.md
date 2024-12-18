# ErrorInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | [**ErrorInfoErrorCode**](ErrorInfoErrorCode.md) |  | [optional] 
**error_description** | **str** |  | [optional] 
**client_reference_list** | **List[str]** |  | [optional] 
**parcel_id_list** | **List[int]** |  | [optional] 

## Example

```python
from openapi_client.models.error_info import ErrorInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorInfo from a JSON string
error_info_instance = ErrorInfo.from_json(json)
# print the JSON string representation of the object
print(ErrorInfo.to_json())

# convert the object into a dict
error_info_dict = error_info_instance.to_dict()
# create an instance of ErrorInfo from a dict
error_info_from_dict = ErrorInfo.from_dict(error_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


