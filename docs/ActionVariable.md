# ActionVariable

ActionVariable return value of the query API

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** | the value of the variable | [optional] 
**name** | **str** | the name of the variable | [optional] 
**owner_id** | **int** | the owner to which the variable belongs | [optional] 
**repo_id** | **int** | the repository to which the variable belongs | [optional] 

## Example

```python
from clientapi_forgejo.models.action_variable import ActionVariable

# TODO update the JSON string below
json = "{}"
# create an instance of ActionVariable from a JSON string
action_variable_instance = ActionVariable.from_json(json)
# print the JSON string representation of the object
print(ActionVariable.to_json())

# convert the object into a dict
action_variable_dict = action_variable_instance.to_dict()
# create an instance of ActionVariable from a dict
action_variable_from_dict = ActionVariable.from_dict(action_variable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


