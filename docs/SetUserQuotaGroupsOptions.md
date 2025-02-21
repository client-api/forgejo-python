# SetUserQuotaGroupsOptions

SetUserQuotaGroupsOptions represents the quota groups of a user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | **List[str]** | Quota groups the user shall have | 

## Example

```python
from clientapi_forgejo.models.set_user_quota_groups_options import SetUserQuotaGroupsOptions

# TODO update the JSON string below
json = "{}"
# create an instance of SetUserQuotaGroupsOptions from a JSON string
set_user_quota_groups_options_instance = SetUserQuotaGroupsOptions.from_json(json)
# print the JSON string representation of the object
print(SetUserQuotaGroupsOptions.to_json())

# convert the object into a dict
set_user_quota_groups_options_dict = set_user_quota_groups_options_instance.to_dict()
# create an instance of SetUserQuotaGroupsOptions from a dict
set_user_quota_groups_options_from_dict = SetUserQuotaGroupsOptions.from_dict(set_user_quota_groups_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


