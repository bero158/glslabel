# ServiceSDSParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_from** | **str** |  | [optional] 
**time_to** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_sds_parameter import ServiceSDSParameter

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceSDSParameter from a JSON string
service_sds_parameter_instance = ServiceSDSParameter.from_json(json)
# print the JSON string representation of the object
print(ServiceSDSParameter.to_json())

# convert the object into a dict
service_sds_parameter_dict = service_sds_parameter_instance.to_dict()
# create an instance of ServiceSDSParameter from a dict
service_sds_parameter_from_dict = ServiceSDSParameter.from_dict(service_sds_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


