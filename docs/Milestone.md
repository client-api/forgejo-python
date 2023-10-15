# Milestone

Milestone milestone is a collection of issues on one repository

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**closed_at** | **datetime** |  | [optional] 
**closed_issues** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**due_on** | **datetime** |  | [optional] 
**id** | **int** |  | [optional] 
**open_issues** | **int** |  | [optional] 
**state** | **str** | StateType issue state type | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.milestone import Milestone

# TODO update the JSON string below
json = "{}"
# create an instance of Milestone from a JSON string
milestone_instance = Milestone.from_json(json)
# print the JSON string representation of the object
print Milestone.to_json()

# convert the object into a dict
milestone_dict = milestone_instance.to_dict()
# create an instance of Milestone from a dict
milestone_form_dict = milestone.from_dict(milestone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


