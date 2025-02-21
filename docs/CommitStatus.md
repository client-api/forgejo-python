# CommitStatus

CommitStatus holds a single status of a single Commit

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**creator** | [**User**](User.md) |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**status** | **str** | CommitStatusState holds the state of a CommitStatus It can be \&quot;pending\&quot;, \&quot;success\&quot;, \&quot;error\&quot; and \&quot;failure\&quot; | [optional] 
**target_url** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.commit_status import CommitStatus

# TODO update the JSON string below
json = "{}"
# create an instance of CommitStatus from a JSON string
commit_status_instance = CommitStatus.from_json(json)
# print the JSON string representation of the object
print(CommitStatus.to_json())

# convert the object into a dict
commit_status_dict = commit_status_instance.to_dict()
# create an instance of CommitStatus from a dict
commit_status_from_dict = CommitStatus.from_dict(commit_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


