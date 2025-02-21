# Commit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**User**](User.md) |  | [optional] 
**commit** | [**RepoCommit**](RepoCommit.md) |  | [optional] 
**committer** | [**User**](User.md) |  | [optional] 
**created** | **datetime** |  | [optional] 
**files** | [**List[CommitAffectedFiles]**](CommitAffectedFiles.md) |  | [optional] 
**html_url** | **str** |  | [optional] 
**parents** | [**List[CommitMeta]**](CommitMeta.md) |  | [optional] 
**sha** | **str** |  | [optional] 
**stats** | [**CommitStats**](CommitStats.md) |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.commit import Commit

# TODO update the JSON string below
json = "{}"
# create an instance of Commit from a JSON string
commit_instance = Commit.from_json(json)
# print the JSON string representation of the object
print(Commit.to_json())

# convert the object into a dict
commit_dict = commit_instance.to_dict()
# create an instance of Commit from a dict
commit_from_dict = Commit.from_dict(commit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


