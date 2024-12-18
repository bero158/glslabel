# Parcel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_number** | **int** |  | [optional] 
**client_reference** | **str** |  | [optional] 
**count** | **int** |  | [optional] 
**cod_amount** | **float** |  | [optional] 
**cod_reference** | **str** |  | [optional] 
**cod_currency** | **str** |  | [optional] 
**content** | **str** |  | [optional] 
**pickup_date** | **str** |  | [optional] 
**pickup_address** | [**Address**](Address.md) |  | [optional] 
**delivery_address** | [**Address**](Address.md) |  | [optional] 
**service_list** | [**List[Service]**](Service.md) |  | [optional] 
**sender_identity_card_number** | **str** |  | [optional] 
**pickup_type** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.parcel import Parcel

# TODO update the JSON string below
json = "{}"
# create an instance of Parcel from a JSON string
parcel_instance = Parcel.from_json(json)
# print the JSON string representation of the object
print(Parcel.to_json())

# convert the object into a dict
parcel_dict = parcel_instance.to_dict()
# create an instance of Parcel from a dict
parcel_from_dict = Parcel.from_dict(parcel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


