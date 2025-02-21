# CreateBranchRepoOption

CreateBranchRepoOption options when creating a branch in a repository

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_branch_name** | **str** | Name of the branch to create | 
**old_branch_name** | **str** | Deprecated: true Name of the old branch to create from | [optional] 
**old_ref_name** | **str** | Name of the old branch/tag/commit to create from | [optional] 

## Example

```python
from clientapi_forgejo.models.create_branch_repo_option import CreateBranchRepoOption

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBranchRepoOption from a JSON string
create_branch_repo_option_instance = CreateBranchRepoOption.from_json(json)
# print the JSON string representation of the object
print(CreateBranchRepoOption.to_json())

# convert the object into a dict
create_branch_repo_option_dict = create_branch_repo_option_instance.to_dict()
# create an instance of CreateBranchRepoOption from a dict
create_branch_repo_option_from_dict = CreateBranchRepoOption.from_dict(create_branch_repo_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


