# ServiceADRParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adr_item_type** | **int** |  | [optional] 
**amount_unit** | **int** |  | [optional] 
**inner_count** | **int** |  | [optional] 
**pack_size** | **int** |  | [optional] 
**un_number** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.service_adr_parameter import ServiceADRParameter

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceADRParameter from a JSON string
service_adr_parameter_instance = ServiceADRParameter.from_json(json)
# print the JSON string representation of the object
print(ServiceADRParameter.to_json())

# convert the object into a dict
service_adr_parameter_dict = service_adr_parameter_instance.to_dict()
# create an instance of ServiceADRParameter from a dict
service_adr_parameter_from_dict = ServiceADRParameter.from_dict(service_adr_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


