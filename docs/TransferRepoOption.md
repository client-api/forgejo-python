# TransferRepoOption

TransferRepoOption options when transfer a repository's ownership

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_owner** | **str** |  | 
**team_ids** | **List[int]** | ID of the team or teams to add to the repository. Teams can only be added to organization-owned repositories. | [optional] 

## Example

```python
from clientapi_forgejo.models.transfer_repo_option import TransferRepoOption

# TODO update the JSON string below
json = "{}"
# create an instance of TransferRepoOption from a JSON string
transfer_repo_option_instance = TransferRepoOption.from_json(json)
# print the JSON string representation of the object
print TransferRepoOption.to_json()

# convert the object into a dict
transfer_repo_option_dict = transfer_repo_option_instance.to_dict()
# create an instance of TransferRepoOption from a dict
transfer_repo_option_form_dict = transfer_repo_option.from_dict(transfer_repo_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


