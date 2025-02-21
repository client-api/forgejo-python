# ActionTask

ActionTask represents a ActionTask

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**display_title** | **str** |  | [optional] 
**event** | **str** |  | [optional] 
**head_branch** | **str** |  | [optional] 
**head_sha** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**run_number** | **int** |  | [optional] 
**run_started_at** | **datetime** |  | [optional] 
**status** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**url** | **str** |  | [optional] 
**workflow_id** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.action_task import ActionTask

# TODO update the JSON string below
json = "{}"
# create an instance of ActionTask from a JSON string
action_task_instance = ActionTask.from_json(json)
# print the JSON string representation of the object
print(ActionTask.to_json())

# convert the object into a dict
action_task_dict = action_task_instance.to_dict()
# create an instance of ActionTask from a dict
action_task_from_dict = ActionTask.from_dict(action_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


