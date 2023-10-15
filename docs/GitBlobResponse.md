# GitBlobResponse

GitBlobResponse represents a git blob

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | [optional] 
**encoding** | **str** |  | [optional] 
**sha** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.git_blob_response import GitBlobResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GitBlobResponse from a JSON string
git_blob_response_instance = GitBlobResponse.from_json(json)
# print the JSON string representation of the object
print GitBlobResponse.to_json()

# convert the object into a dict
git_blob_response_dict = git_blob_response_instance.to_dict()
# create an instance of GitBlobResponse from a dict
git_blob_response_form_dict = git_blob_response.from_dict(git_blob_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


