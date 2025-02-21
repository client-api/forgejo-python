# EditHookOption

EditHookOption options when modify one hook

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**authorization_header** | **str** |  | [optional] 
**branch_filter** | **str** |  | [optional] 
**config** | **Dict[str, str]** |  | [optional] 
**events** | **List[str]** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.edit_hook_option import EditHookOption

# TODO update the JSON string below
json = "{}"
# create an instance of EditHookOption from a JSON string
edit_hook_option_instance = EditHookOption.from_json(json)
# print the JSON string representation of the object
print(EditHookOption.to_json())

# convert the object into a dict
edit_hook_option_dict = edit_hook_option_instance.to_dict()
# create an instance of EditHookOption from a dict
edit_hook_option_from_dict = EditHookOption.from_dict(edit_hook_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


