# CreateVariableOption

CreateVariableOption the option when creating variable

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Value of the variable to create | 

## Example

```python
from clientapi_forgejo.models.create_variable_option import CreateVariableOption

# TODO update the JSON string below
json = "{}"
# create an instance of CreateVariableOption from a JSON string
create_variable_option_instance = CreateVariableOption.from_json(json)
# print the JSON string representation of the object
print(CreateVariableOption.to_json())

# convert the object into a dict
create_variable_option_dict = create_variable_option_instance.to_dict()
# create an instance of CreateVariableOption from a dict
create_variable_option_from_dict = CreateVariableOption.from_dict(create_variable_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


