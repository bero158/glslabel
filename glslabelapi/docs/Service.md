# Service


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**adr_parameter** | **str** |  | [optional] 
**aos_parameter** | **str** |  | [optional] 
**cs1_parameter** | **str** |  | [optional] 
**dds_parameter** | **str** |  | [optional] 
**dpv_parameter** | **str** |  | [optional] 
**fds_parameter** | **str** |  | [optional] 
**fss_parameter** | **str** |  | [optional] 
**ins_parameter** | **str** |  | [optional] 
**mmp_parameter** | **str** |  | [optional] 
**psd_parameter** | **str** |  | [optional] 
**sds_parameter** | **str** |  | [optional] 
**sm1_parameter** | **str** |  | [optional] 
**sm2_parameter** | **str** |  | [optional] 
**szl_parameter** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service import Service

# TODO update the JSON string below
json = "{}"
# create an instance of Service from a JSON string
service_instance = Service.from_json(json)
# print the JSON string representation of the object
print(Service.to_json())

# convert the object into a dict
service_dict = service_instance.to_dict()
# create an instance of Service from a dict
service_from_dict = Service.from_dict(service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


