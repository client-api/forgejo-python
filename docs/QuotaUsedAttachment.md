# QuotaUsedAttachment

QuotaUsedAttachment represents an attachment counting towards a user's quota

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_url** | **str** | API URL for the attachment | [optional] 
**contained_in** | [**QuotaUsedAttachmentContainedIn**](QuotaUsedAttachmentContainedIn.md) |  | [optional] 
**name** | **str** | Filename of the attachment | [optional] 
**size** | **int** | Size of the attachment (in bytes) | [optional] 

## Example

```python
from clientapi_forgejo.models.quota_used_attachment import QuotaUsedAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of QuotaUsedAttachment from a JSON string
quota_used_attachment_instance = QuotaUsedAttachment.from_json(json)
# print the JSON string representation of the object
print(QuotaUsedAttachment.to_json())

# convert the object into a dict
quota_used_attachment_dict = quota_used_attachment_instance.to_dict()
# create an instance of QuotaUsedAttachment from a dict
quota_used_attachment_from_dict = QuotaUsedAttachment.from_dict(quota_used_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


