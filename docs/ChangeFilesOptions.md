# ChangeFilesOptions

ChangeFilesOptions options for creating, updating or deleting multiple files Note: `author` and `committer` are optional (if only one is given, it will be used for the other, otherwise the authenticated user will be used)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**Identity**](Identity.md) |  | [optional] 
**branch** | **str** | branch (optional) to base this file from. if not given, the default branch is used | [optional] 
**committer** | [**Identity**](Identity.md) |  | [optional] 
**dates** | [**CommitDateOptions**](CommitDateOptions.md) |  | [optional] 
**files** | [**List[ChangeFileOperation]**](ChangeFileOperation.md) | list of file operations | 
**message** | **str** | message (optional) for the commit of this file. if not supplied, a default message will be used | [optional] 
**new_branch** | **str** | new_branch (optional) will make a new branch from &#x60;branch&#x60; before creating the file | [optional] 
**signoff** | **bool** | Add a Signed-off-by trailer by the committer at the end of the commit log message. | [optional] 

## Example

```python
from clientapi_forgejo.models.change_files_options import ChangeFilesOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeFilesOptions from a JSON string
change_files_options_instance = ChangeFilesOptions.from_json(json)
# print the JSON string representation of the object
print ChangeFilesOptions.to_json()

# convert the object into a dict
change_files_options_dict = change_files_options_instance.to_dict()
# create an instance of ChangeFilesOptions from a dict
change_files_options_form_dict = change_files_options.from_dict(change_files_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


