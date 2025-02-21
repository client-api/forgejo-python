# PushMirror

PushMirror represents information of a push mirror

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** |  | [optional] 
**interval** | **str** |  | [optional] 
**last_error** | **str** |  | [optional] 
**last_update** | **datetime** |  | [optional] 
**public_key** | **str** |  | [optional] 
**remote_address** | **str** |  | [optional] 
**remote_name** | **str** |  | [optional] 
**repo_name** | **str** |  | [optional] 
**sync_on_commit** | **bool** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.push_mirror import PushMirror

# TODO update the JSON string below
json = "{}"
# create an instance of PushMirror from a JSON string
push_mirror_instance = PushMirror.from_json(json)
# print the JSON string representation of the object
print(PushMirror.to_json())

# convert the object into a dict
push_mirror_dict = push_mirror_instance.to_dict()
# create an instance of PushMirror from a dict
push_mirror_from_dict = PushMirror.from_dict(push_mirror_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


