# FileResponse

FileResponse contains information about a repo's file

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commit** | [**FileCommitResponse**](FileCommitResponse.md) |  | [optional] 
**content** | [**ContentsResponse**](ContentsResponse.md) |  | [optional] 
**verification** | [**PayloadCommitVerification**](PayloadCommitVerification.md) |  | [optional] 

## Example

```python
from clientapi_forgejo.models.file_response import FileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FileResponse from a JSON string
file_response_instance = FileResponse.from_json(json)
# print the JSON string representation of the object
print(FileResponse.to_json())

# convert the object into a dict
file_response_dict = file_response_instance.to_dict()
# create an instance of FileResponse from a dict
file_response_from_dict = FileResponse.from_dict(file_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


