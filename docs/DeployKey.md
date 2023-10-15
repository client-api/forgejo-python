# DeployKey

DeployKey a deploy key

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**fingerprint** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**key** | **str** |  | [optional] 
**key_id** | **int** |  | [optional] 
**read_only** | **bool** |  | [optional] 
**repository** | [**Repository**](Repository.md) |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.deploy_key import DeployKey

# TODO update the JSON string below
json = "{}"
# create an instance of DeployKey from a JSON string
deploy_key_instance = DeployKey.from_json(json)
# print the JSON string representation of the object
print DeployKey.to_json()

# convert the object into a dict
deploy_key_dict = deploy_key_instance.to_dict()
# create an instance of DeployKey from a dict
deploy_key_form_dict = deploy_key.from_dict(deploy_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


