# PRBranchInfo

PRBranchInfo information about a branch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**ref** | **str** |  | [optional] 
**repo** | [**Repository**](Repository.md) |  | [optional] 
**repo_id** | **int** |  | [optional] 
**sha** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.pr_branch_info import PRBranchInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PRBranchInfo from a JSON string
pr_branch_info_instance = PRBranchInfo.from_json(json)
# print the JSON string representation of the object
print(PRBranchInfo.to_json())

# convert the object into a dict
pr_branch_info_dict = pr_branch_info_instance.to_dict()
# create an instance of PRBranchInfo from a dict
pr_branch_info_from_dict = PRBranchInfo.from_dict(pr_branch_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


