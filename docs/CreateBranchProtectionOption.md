# CreateBranchProtectionOption

CreateBranchProtectionOption options for creating a branch protection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apply_to_admins** | **bool** |  | [optional] 
**approvals_whitelist_teams** | **List[str]** |  | [optional] 
**approvals_whitelist_username** | **List[str]** |  | [optional] 
**block_on_official_review_requests** | **bool** |  | [optional] 
**block_on_outdated_branch** | **bool** |  | [optional] 
**block_on_rejected_reviews** | **bool** |  | [optional] 
**branch_name** | **str** | Deprecated: true | [optional] 
**dismiss_stale_approvals** | **bool** |  | [optional] 
**enable_approvals_whitelist** | **bool** |  | [optional] 
**enable_merge_whitelist** | **bool** |  | [optional] 
**enable_push** | **bool** |  | [optional] 
**enable_push_whitelist** | **bool** |  | [optional] 
**enable_status_check** | **bool** |  | [optional] 
**ignore_stale_approvals** | **bool** |  | [optional] 
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

## Example

```python
from clientapi_forgejo.models.create_branch_protection_option import CreateBranchProtectionOption

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBranchProtectionOption from a JSON string
create_branch_protection_option_instance = CreateBranchProtectionOption.from_json(json)
# print the JSON string representation of the object
print(CreateBranchProtectionOption.to_json())

# convert the object into a dict
create_branch_protection_option_dict = create_branch_protection_option_instance.to_dict()
# create an instance of CreateBranchProtectionOption from a dict
create_branch_protection_option_from_dict = CreateBranchProtectionOption.from_dict(create_branch_protection_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


