# EditReactionOption

EditReactionOption contain the reaction type

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.edit_reaction_option import EditReactionOption

# TODO update the JSON string below
json = "{}"
# create an instance of EditReactionOption from a JSON string
edit_reaction_option_instance = EditReactionOption.from_json(json)
# print the JSON string representation of the object
print EditReactionOption.to_json()

# convert the object into a dict
edit_reaction_option_dict = edit_reaction_option_instance.to_dict()
# create an instance of EditReactionOption from a dict
edit_reaction_option_form_dict = edit_reaction_option.from_dict(edit_reaction_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


