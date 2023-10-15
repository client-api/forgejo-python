# GitTreeResponse

GitTreeResponse returns a git tree

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**sha** | **str** |  | [optional] 
**total_count** | **int** |  | [optional] 
**tree** | [**List[GitEntry]**](GitEntry.md) |  | [optional] 
**truncated** | **bool** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.git_tree_response import GitTreeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GitTreeResponse from a JSON string
git_tree_response_instance = GitTreeResponse.from_json(json)
# print the JSON string representation of the object
print GitTreeResponse.to_json()

# convert the object into a dict
git_tree_response_dict = git_tree_response_instance.to_dict()
# create an instance of GitTreeResponse from a dict
git_tree_response_form_dict = git_tree_response.from_dict(git_tree_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


