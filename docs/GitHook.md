# GitHook

GitHook represents a Git repository hook

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.git_hook import GitHook

# TODO update the JSON string below
json = "{}"
# create an instance of GitHook from a JSON string
git_hook_instance = GitHook.from_json(json)
# print the JSON string representation of the object
print GitHook.to_json()

# convert the object into a dict
git_hook_dict = git_hook_instance.to_dict()
# create an instance of GitHook from a dict
git_hook_form_dict = git_hook.from_dict(git_hook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


