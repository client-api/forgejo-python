# BranchProtection

BranchProtection represents a branch protection for a repository

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approvals_whitelist_teams** | **List[str]** |  | [optional] 
**approvals_whitelist_username** | **List[str]** |  | [optional] 
**block_on_official_review_requests** | **bool** |  | [optional] 
**block_on_outdated_branch** | **bool** |  | [optional] 
**block_on_rejected_reviews** | **bool** |  | [optional] 
**branch_name** | **str** | Deprecated: true | [optional] 
**created_at** | **datetime** |  | [optional] 
**dismiss_stale_approvals** | **bool** |  | [optional] 
**enable_approvals_whitelist** | **bool** |  | [optional] 
**enable_merge_whitelist** | **bool** |  | [optional] 
**enable_push** | **bool** |  | [optional] 
**enable_push_whitelist** | **bool** |  | [optional] 
**enable_status_check** | **bool** |  | [optional] 
**merge_whitelist_teams** | **List[str]** |  | [optional] 
**merge_whitelist_usernames** | **List[str]** |  | [optional] 
**protected_file_patterns** | **str** |  | [optional] 
**push_whitelist_deploy_keys** | **bool** |  | [optional] 
**push_whitelist_teams** | **List[str]** |  | [optional] 
**push_whitelist_usernames** | **List[str]** |  | [optional] 
**require_signed_commits** | **bool** |  | [optional] 
**required_approvals** | **int** |  | [optional] 
**rule_name** | **str** |  | [optional] 
**status_check_contexts** | **List[str]** |  | [optional] 
**unprotected_file_patterns** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.branch_protection import BranchProtection

# TODO update the JSON string below
json = "{}"
# create an instance of BranchProtection from a JSON string
branch_protection_instance = BranchProtection.from_json(json)
# print the JSON string representation of the object
print BranchProtection.to_json()

# convert the object into a dict
branch_protection_dict = branch_protection_instance.to_dict()
# create an instance of BranchProtection from a dict
branch_protection_form_dict = branch_protection.from_dict(branch_protection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


