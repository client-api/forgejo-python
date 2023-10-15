# EditGitHookOption

EditGitHookOption options when modifying one Git hook

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.edit_git_hook_option import EditGitHookOption

# TODO update the JSON string below
json = "{}"
# create an instance of EditGitHookOption from a JSON string
edit_git_hook_option_instance = EditGitHookOption.from_json(json)
# print the JSON string representation of the object
print EditGitHookOption.to_json()

# convert the object into a dict
edit_git_hook_option_dict = edit_git_hook_option_instance.to_dict()
# create an instance of EditGitHookOption from a dict
edit_git_hook_option_form_dict = edit_git_hook_option.from_dict(edit_git_hook_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


