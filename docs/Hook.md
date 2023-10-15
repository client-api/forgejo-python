# Hook

Hook a hook is a web hook when one repository changed

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**authorization_header** | **str** |  | [optional] 
**branch_filter** | **str** |  | [optional] 
**config** | **Dict[str, str]** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**events** | **List[str]** |  | [optional] 
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.hook import Hook

# TODO update the JSON string below
json = "{}"
# create an instance of Hook from a JSON string
hook_instance = Hook.from_json(json)
# print the JSON string representation of the object
print Hook.to_json()

# convert the object into a dict
hook_dict = hook_instance.to_dict()
# create an instance of Hook from a dict
hook_form_dict = hook.from_dict(hook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


