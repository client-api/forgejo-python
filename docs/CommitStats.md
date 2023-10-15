# CommitStats

CommitStats is statistics for a RepoCommit

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additions** | **int** |  | [optional] 
**deletions** | **int** |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.commit_stats import CommitStats

# TODO update the JSON string below
json = "{}"
# create an instance of CommitStats from a JSON string
commit_stats_instance = CommitStats.from_json(json)
# print the JSON string representation of the object
print CommitStats.to_json()

# convert the object into a dict
commit_stats_dict = commit_stats_instance.to_dict()
# create an instance of CommitStats from a dict
commit_stats_form_dict = commit_stats.from_dict(commit_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


