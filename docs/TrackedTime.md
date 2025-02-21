# TrackedTime

TrackedTime worked time for an issue / pr

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** |  | [optional] 
**id** | **int** |  | [optional] 
**issue** | [**Issue**](Issue.md) |  | [optional] 
**issue_id** | **int** | deprecated (only for backwards compatibility) | [optional] 
**time** | **int** | Time in seconds | [optional] 
**user_id** | **int** | deprecated (only for backwards compatibility) | [optional] 
**user_name** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.tracked_time import TrackedTime

# TODO update the JSON string below
json = "{}"
# create an instance of TrackedTime from a JSON string
tracked_time_instance = TrackedTime.from_json(json)
# print the JSON string representation of the object
print(TrackedTime.to_json())

# convert the object into a dict
tracked_time_dict = tracked_time_instance.to_dict()
# create an instance of TrackedTime from a dict
tracked_time_from_dict = TrackedTime.from_dict(tracked_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


