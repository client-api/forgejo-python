# PublicKey

PublicKey publickey is a user key to push code to repository

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**fingerprint** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**key** | **str** |  | [optional] 
**key_type** | **str** |  | [optional] 
**read_only** | **bool** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**user** | [**User**](User.md) |  | [optional] 

## Example

```python
from clientapi_forgejo.models.public_key import PublicKey

# TODO update the JSON string below
json = "{}"
# create an instance of PublicKey from a JSON string
public_key_instance = PublicKey.from_json(json)
# print the JSON string representation of the object
print PublicKey.to_json()

# convert the object into a dict
public_key_dict = public_key_instance.to_dict()
# create an instance of PublicKey from a dict
public_key_form_dict = public_key.from_dict(public_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


