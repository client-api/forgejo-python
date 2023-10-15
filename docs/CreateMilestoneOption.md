# CreateMilestoneOption

CreateMilestoneOption options for creating a milestone

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**due_on** | **datetime** |  | [optional] 
**state** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.create_milestone_option import CreateMilestoneOption

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMilestoneOption from a JSON string
create_milestone_option_instance = CreateMilestoneOption.from_json(json)
# print the JSON string representation of the object
print CreateMilestoneOption.to_json()

# convert the object into a dict
create_milestone_option_dict = create_milestone_option_instance.to_dict()
# create an instance of CreateMilestoneOption from a dict
create_milestone_option_form_dict = create_milestone_option.from_dict(create_milestone_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


