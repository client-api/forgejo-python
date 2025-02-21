# WikiCommit

WikiCommit page commit/revision

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**CommitUser**](CommitUser.md) |  | [optional] 
**commiter** | [**CommitUser**](CommitUser.md) |  | [optional] 
**message** | **str** |  | [optional] 
**sha** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.wiki_commit import WikiCommit

# TODO update the JSON string below
json = "{}"
# create an instance of WikiCommit from a JSON string
wiki_commit_instance = WikiCommit.from_json(json)
# print the JSON string representation of the object
print(WikiCommit.to_json())

# convert the object into a dict
wiki_commit_dict = wiki_commit_instance.to_dict()
# create an instance of WikiCommit from a dict
wiki_commit_from_dict = WikiCommit.from_dict(wiki_commit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


