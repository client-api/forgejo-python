# StopWatch

StopWatch represent a running stopwatch

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** |  | [optional] 
**duration** | **str** |  | [optional] 
**issue_index** | **int** |  | [optional] 
**issue_title** | **str** |  | [optional] 
**repo_name** | **str** |  | [optional] 
**repo_owner_name** | **str** |  | [optional] 
**seconds** | **int** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.stop_watch import StopWatch

# TODO update the JSON string below
json = "{}"
# create an instance of StopWatch from a JSON string
stop_watch_instance = StopWatch.from_json(json)
# print the JSON string representation of the object
print StopWatch.to_json()

# convert the object into a dict
stop_watch_dict = stop_watch_instance.to_dict()
# create an instance of StopWatch from a dict
stop_watch_form_dict = stop_watch.from_dict(stop_watch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


