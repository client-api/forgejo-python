# CommitAffectedFiles

CommitAffectedFiles store information about files affected by the commit

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.commit_affected_files import CommitAffectedFiles

# TODO update the JSON string below
json = "{}"
# create an instance of CommitAffectedFiles from a JSON string
commit_affected_files_instance = CommitAffectedFiles.from_json(json)
# print the JSON string representation of the object
print CommitAffectedFiles.to_json()

# convert the object into a dict
commit_affected_files_dict = commit_affected_files_instance.to_dict()
# create an instance of CommitAffectedFiles from a dict
commit_affected_files_form_dict = commit_affected_files.from_dict(commit_affected_files_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


