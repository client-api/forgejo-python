# CreateLabelOption

CreateLabelOption options for creating a label

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** |  | 
**description** | **str** |  | [optional] 
**exclusive** | **bool** |  | [optional] 
**name** | **str** |  | 

## Example

```python
from clientapi_forgejo.models.create_label_option import CreateLabelOption

# TODO update the JSON string below
json = "{}"
# create an instance of CreateLabelOption from a JSON string
create_label_option_instance = CreateLabelOption.from_json(json)
# print the JSON string representation of the object
print CreateLabelOption.to_json()

# convert the object into a dict
create_label_option_dict = create_label_option_instance.to_dict()
# create an instance of CreateLabelOption from a dict
create_label_option_form_dict = create_label_option.from_dict(create_label_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


