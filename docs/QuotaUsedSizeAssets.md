# QuotaUsedSizeAssets

QuotaUsedSizeAssets represents the size-based asset usage of a user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifacts** | **int** | Storage size used for the user&#39;s artifacts | [optional] 
**attachments** | [**QuotaUsedSizeAssetsAttachments**](QuotaUsedSizeAssetsAttachments.md) |  | [optional] 
**packages** | [**QuotaUsedSizeAssetsPackages**](QuotaUsedSizeAssetsPackages.md) |  | [optional] 

## Example

```python
from clientapi_forgejo.models.quota_used_size_assets import QuotaUsedSizeAssets

# TODO update the JSON string below
json = "{}"
# create an instance of QuotaUsedSizeAssets from a JSON string
quota_used_size_assets_instance = QuotaUsedSizeAssets.from_json(json)
# print the JSON string representation of the object
print(QuotaUsedSizeAssets.to_json())

# convert the object into a dict
quota_used_size_assets_dict = quota_used_size_assets_instance.to_dict()
# create an instance of QuotaUsedSizeAssets from a dict
quota_used_size_assets_from_dict = QuotaUsedSizeAssets.from_dict(quota_used_size_assets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


