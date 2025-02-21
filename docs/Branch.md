# Branch

Branch represents a repository branch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commit** | [**PayloadCommit**](PayloadCommit.md) |  | [optional] 
**effective_branch_protection_name** | **str** |  | [optional] 
**enable_status_check** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**protected** | **bool** |  | [optional] 
**required_approvals** | **int** |  | [optional] 
**status_check_contexts** | **List[str]** |  | [optional] 
**user_can_merge** | **bool** |  | [optional] 
**user_can_push** | **bool** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.branch import Branch

# TODO update the JSON string below
json = "{}"
# create an instance of Branch from a JSON string
branch_instance = Branch.from_json(json)
# print the JSON string representation of the object
print(Branch.to_json())

# convert the object into a dict
branch_dict = branch_instance.to_dict()
# create an instance of Branch from a dict
branch_from_dict = Branch.from_dict(branch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


