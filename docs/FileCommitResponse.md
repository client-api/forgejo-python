# FileCommitResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**CommitUser**](CommitUser.md) |  | [optional] 
**committer** | [**CommitUser**](CommitUser.md) |  | [optional] 
**created** | **datetime** |  | [optional] 
**html_url** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**parents** | [**List[CommitMeta]**](CommitMeta.md) |  | [optional] 
**sha** | **str** |  | [optional] 
**tree** | [**CommitMeta**](CommitMeta.md) |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.file_commit_response import FileCommitResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FileCommitResponse from a JSON string
file_commit_response_instance = FileCommitResponse.from_json(json)
# print the JSON string representation of the object
print(FileCommitResponse.to_json())

# convert the object into a dict
file_commit_response_dict = file_commit_response_instance.to_dict()
# create an instance of FileCommitResponse from a dict
file_commit_response_from_dict = FileCommitResponse.from_dict(file_commit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


