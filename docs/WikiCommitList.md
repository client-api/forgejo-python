# WikiCommitList

WikiCommitList commit/revision list

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commits** | [**List[WikiCommit]**](WikiCommit.md) |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.wiki_commit_list import WikiCommitList

# TODO update the JSON string below
json = "{}"
# create an instance of WikiCommitList from a JSON string
wiki_commit_list_instance = WikiCommitList.from_json(json)
# print the JSON string representation of the object
print(WikiCommitList.to_json())

# convert the object into a dict
wiki_commit_list_dict = wiki_commit_list_instance.to_dict()
# create an instance of WikiCommitList from a dict
wiki_commit_list_from_dict = WikiCommitList.from_dict(wiki_commit_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


