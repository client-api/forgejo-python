# QuotaUsedSizeGit

QuotaUsedSizeGit represents the size-based git (lfs) quota usage of a user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lfs** | **int** | Storage size of the user&#39;s Git LFS objects | [optional] 

## Example

```python
from clientapi_forgejo.models.quota_used_size_git import QuotaUsedSizeGit

# TODO update the JSON string below
json = "{}"
# create an instance of QuotaUsedSizeGit from a JSON string
quota_used_size_git_instance = QuotaUsedSizeGit.from_json(json)
# print the JSON string representation of the object
print(QuotaUsedSizeGit.to_json())

# convert the object into a dict
quota_used_size_git_dict = quota_used_size_git_instance.to_dict()
# create an instance of QuotaUsedSizeGit from a dict
quota_used_size_git_from_dict = QuotaUsedSizeGit.from_dict(quota_used_size_git_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


