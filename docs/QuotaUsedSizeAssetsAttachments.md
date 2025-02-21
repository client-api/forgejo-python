# QuotaUsedSizeAssetsAttachments

QuotaUsedSizeAssetsAttachments represents the size-based attachment quota usage of a user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issues** | **int** | Storage size used for the user&#39;s issue &amp; comment attachments | [optional] 
**releases** | **int** | Storage size used for the user&#39;s release attachments | [optional] 

## Example

```python
from clientapi_forgejo.models.quota_used_size_assets_attachments import QuotaUsedSizeAssetsAttachments

# TODO update the JSON string below
json = "{}"
# create an instance of QuotaUsedSizeAssetsAttachments from a JSON string
quota_used_size_assets_attachments_instance = QuotaUsedSizeAssetsAttachments.from_json(json)
# print the JSON string representation of the object
print(QuotaUsedSizeAssetsAttachments.to_json())

# convert the object into a dict
quota_used_size_assets_attachments_dict = quota_used_size_assets_attachments_instance.to_dict()
# create an instance of QuotaUsedSizeAssetsAttachments from a dict
quota_used_size_assets_attachments_from_dict = QuotaUsedSizeAssetsAttachments.from_dict(quota_used_size_assets_attachments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


