# EditMilestoneOption

EditMilestoneOption options for editing a milestone

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**due_on** | **datetime** |  | [optional] 
**state** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.edit_milestone_option import EditMilestoneOption

# TODO update the JSON string below
json = "{}"
# create an instance of EditMilestoneOption from a JSON string
edit_milestone_option_instance = EditMilestoneOption.from_json(json)
# print the JSON string representation of the object
print(EditMilestoneOption.to_json())

# convert the object into a dict
edit_milestone_option_dict = edit_milestone_option_instance.to_dict()
# create an instance of EditMilestoneOption from a dict
edit_milestone_option_from_dict = EditMilestoneOption.from_dict(edit_milestone_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


