# FilesResponse

FilesResponse contains information about multiple files from a repo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commit** | [**FileCommitResponse**](FileCommitResponse.md) |  | [optional] 
**files** | [**List[ContentsResponse]**](ContentsResponse.md) |  | [optional] 
**verification** | [**PayloadCommitVerification**](PayloadCommitVerification.md) |  | [optional] 

## Example

```python
from clientapi_forgejo.models.files_response import FilesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FilesResponse from a JSON string
files_response_instance = FilesResponse.from_json(json)
# print the JSON string representation of the object
print FilesResponse.to_json()

# convert the object into a dict
files_response_dict = files_response_instance.to_dict()
# create an instance of FilesResponse from a dict
files_response_form_dict = files_response.from_dict(files_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


