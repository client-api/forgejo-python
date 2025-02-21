# ActionTaskResponse

ActionTaskResponse returns a ActionTask

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | [optional] 
**workflow_runs** | [**List[ActionTask]**](ActionTask.md) |  | [optional] 

## Example

```python
from clientapi_forgejo.models.action_task_response import ActionTaskResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ActionTaskResponse from a JSON string
action_task_response_instance = ActionTaskResponse.from_json(json)
# print the JSON string representation of the object
print(ActionTaskResponse.to_json())

# convert the object into a dict
action_task_response_dict = action_task_response_instance.to_dict()
# create an instance of ActionTaskResponse from a dict
action_task_response_from_dict = ActionTaskResponse.from_dict(action_task_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


