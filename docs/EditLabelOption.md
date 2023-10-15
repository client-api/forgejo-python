# EditLabelOption

EditLabelOption options for editing a label

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**exclusive** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.edit_label_option import EditLabelOption

# TODO update the JSON string below
json = "{}"
# create an instance of EditLabelOption from a JSON string
edit_label_option_instance = EditLabelOption.from_json(json)
# print the JSON string representation of the object
print EditLabelOption.to_json()

# convert the object into a dict
edit_label_option_dict = edit_label_option_instance.to_dict()
# create an instance of EditLabelOption from a dict
edit_label_option_form_dict = edit_label_option.from_dict(edit_label_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


