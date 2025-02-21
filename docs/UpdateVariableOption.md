# UpdateVariableOption

UpdateVariableOption the option when updating variable

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | New name for the variable. If the field is empty, the variable name won&#39;t be updated. | [optional] 
**value** | **str** | Value of the variable to update | 

## Example

```python
from clientapi_forgejo.models.update_variable_option import UpdateVariableOption

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateVariableOption from a JSON string
update_variable_option_instance = UpdateVariableOption.from_json(json)
# print the JSON string representation of the object
print(UpdateVariableOption.to_json())

# convert the object into a dict
update_variable_option_dict = update_variable_option_instance.to_dict()
# create an instance of UpdateVariableOption from a dict
update_variable_option_from_dict = UpdateVariableOption.from_dict(update_variable_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


