# QuotaUsedSize

QuotaUsedSize represents the size-based quota usage of a user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assets** | [**QuotaUsedSizeAssets**](QuotaUsedSizeAssets.md) |  | [optional] 
**git** | [**QuotaUsedSizeGit**](QuotaUsedSizeGit.md) |  | [optional] 
**repos** | [**QuotaUsedSizeRepos**](QuotaUsedSizeRepos.md) |  | [optional] 

## Example

```python
from clientapi_forgejo.models.quota_used_size import QuotaUsedSize

# TODO update the JSON string below
json = "{}"
# create an instance of QuotaUsedSize from a JSON string
quota_used_size_instance = QuotaUsedSize.from_json(json)
# print the JSON string representation of the object
print(QuotaUsedSize.to_json())

# convert the object into a dict
quota_used_size_dict = quota_used_size_instance.to_dict()
# create an instance of QuotaUsedSize from a dict
quota_used_size_from_dict = QuotaUsedSize.from_dict(quota_used_size_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


