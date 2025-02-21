# UpdateBranchRepoOption

UpdateBranchRepoOption options when updating a branch in a repository

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | New branch name | 

## Example

```python
from clientapi_forgejo.models.update_branch_repo_option import UpdateBranchRepoOption

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateBranchRepoOption from a JSON string
update_branch_repo_option_instance = UpdateBranchRepoOption.from_json(json)
# print the JSON string representation of the object
print(UpdateBranchRepoOption.to_json())

# convert the object into a dict
update_branch_repo_option_dict = update_branch_repo_option_instance.to_dict()
# create an instance of UpdateBranchRepoOption from a dict
update_branch_repo_option_from_dict = UpdateBranchRepoOption.from_dict(update_branch_repo_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


