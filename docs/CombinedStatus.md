# CombinedStatus

CombinedStatus holds the combined state of several statuses for a single commit

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commit_url** | **str** |  | [optional] 
**repository** | [**Repository**](Repository.md) |  | [optional] 
**sha** | **str** |  | [optional] 
**state** | **str** | CommitStatusState holds the state of a CommitStatus It can be \&quot;pending\&quot;, \&quot;success\&quot;, \&quot;error\&quot; and \&quot;failure\&quot; | [optional] 
**statuses** | [**List[CommitStatus]**](CommitStatus.md) |  | [optional] 
**total_count** | **int** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.combined_status import CombinedStatus

# TODO update the JSON string below
json = "{}"
# create an instance of CombinedStatus from a JSON string
combined_status_instance = CombinedStatus.from_json(json)
# print the JSON string representation of the object
print(CombinedStatus.to_json())

# convert the object into a dict
combined_status_dict = combined_status_instance.to_dict()
# create an instance of CombinedStatus from a dict
combined_status_from_dict = CombinedStatus.from_dict(combined_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


