# QuotaUsedAttachmentContainedIn

Context for the attachment: URLs to the containing object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_url** | **str** | API URL for the object that contains this attachment | [optional] 
**html_url** | **str** | HTML URL for the object that contains this attachment | [optional] 

## Example

```python
from clientapi_forgejo.models.quota_used_attachment_contained_in import QuotaUsedAttachmentContainedIn

# TODO update the JSON string below
json = "{}"
# create an instance of QuotaUsedAttachmentContainedIn from a JSON string
quota_used_attachment_contained_in_instance = QuotaUsedAttachmentContainedIn.from_json(json)
# print the JSON string representation of the object
print(QuotaUsedAttachmentContainedIn.to_json())

# convert the object into a dict
quota_used_attachment_contained_in_dict = quota_used_attachment_contained_in_instance.to_dict()
# create an instance of QuotaUsedAttachmentContainedIn from a dict
quota_used_attachment_contained_in_from_dict = QuotaUsedAttachmentContainedIn.from_dict(quota_used_attachment_contained_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


