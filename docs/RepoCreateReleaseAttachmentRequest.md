# RepoCreateReleaseAttachmentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachment** | **bytearray** | attachment to upload (this parameter is incompatible with &#x60;external_url&#x60;) | [optional] 
**external_url** | **str** | url to external asset (this parameter is incompatible with &#x60;attachment&#x60;) | [optional] 

## Example

```python
from clientapi_forgejo.models.repo_create_release_attachment_request import RepoCreateReleaseAttachmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RepoCreateReleaseAttachmentRequest from a JSON string
repo_create_release_attachment_request_instance = RepoCreateReleaseAttachmentRequest.from_json(json)
# print the JSON string representation of the object
print(RepoCreateReleaseAttachmentRequest.to_json())

# convert the object into a dict
repo_create_release_attachment_request_dict = repo_create_release_attachment_request_instance.to_dict()
# create an instance of RepoCreateReleaseAttachmentRequest from a dict
repo_create_release_attachment_request_from_dict = RepoCreateReleaseAttachmentRequest.from_dict(repo_create_release_attachment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


