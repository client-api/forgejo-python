# QuotaUsedSizeRepos

QuotaUsedSizeRepos represents the size-based repository quota usage of a user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**private** | **int** | Storage size of the user&#39;s private repositories | [optional] 
**public** | **int** | Storage size of the user&#39;s public repositories | [optional] 

## Example

```python
from clientapi_forgejo.models.quota_used_size_repos import QuotaUsedSizeRepos

# TODO update the JSON string below
json = "{}"
# create an instance of QuotaUsedSizeRepos from a JSON string
quota_used_size_repos_instance = QuotaUsedSizeRepos.from_json(json)
# print the JSON string representation of the object
print(QuotaUsedSizeRepos.to_json())

# convert the object into a dict
quota_used_size_repos_dict = quota_used_size_repos_instance.to_dict()
# create an instance of QuotaUsedSizeRepos from a dict
quota_used_size_repos_from_dict = QuotaUsedSizeRepos.from_dict(quota_used_size_repos_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


