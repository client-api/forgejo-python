# CreateTagOption

CreateTagOption options when creating a tag

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**tag_name** | **str** |  | 
**target** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.create_tag_option import CreateTagOption

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTagOption from a JSON string
create_tag_option_instance = CreateTagOption.from_json(json)
# print the JSON string representation of the object
print CreateTagOption.to_json()

# convert the object into a dict
create_tag_option_dict = create_tag_option_instance.to_dict()
# create an instance of CreateTagOption from a dict
create_tag_option_form_dict = create_tag_option.from_dict(create_tag_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


