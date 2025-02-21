# QuotaUsedSizeAssetsPackages

QuotaUsedSizeAssetsPackages represents the size-based package quota usage of a user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all** | **int** | Storage suze used for the user&#39;s packages | [optional] 

## Example

```python
from clientapi_forgejo.models.quota_used_size_assets_packages import QuotaUsedSizeAssetsPackages

# TODO update the JSON string below
json = "{}"
# create an instance of QuotaUsedSizeAssetsPackages from a JSON string
quota_used_size_assets_packages_instance = QuotaUsedSizeAssetsPackages.from_json(json)
# print the JSON string representation of the object
print(QuotaUsedSizeAssetsPackages.to_json())

# convert the object into a dict
quota_used_size_assets_packages_dict = quota_used_size_assets_packages_instance.to_dict()
# create an instance of QuotaUsedSizeAssetsPackages from a dict
quota_used_size_assets_packages_from_dict = QuotaUsedSizeAssetsPackages.from_dict(quota_used_size_assets_packages_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


