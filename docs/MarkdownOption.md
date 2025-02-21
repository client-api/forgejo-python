# MarkdownOption

MarkdownOption markdown options

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **str** | Context to render  in: body | [optional] 
**mode** | **str** | Mode to render (comment, gfm, markdown)  in: body | [optional] 
**text** | **str** | Text markdown to render  in: body | [optional] 
**wiki** | **bool** | Is it a wiki page ?  in: body | [optional] 

## Example

```python
from clientapi_forgejo.models.markdown_option import MarkdownOption

# TODO update the JSON string below
json = "{}"
# create an instance of MarkdownOption from a JSON string
markdown_option_instance = MarkdownOption.from_json(json)
# print the JSON string representation of the object
print(MarkdownOption.to_json())

# convert the object into a dict
markdown_option_dict = markdown_option_instance.to_dict()
# create an instance of MarkdownOption from a dict
markdown_option_from_dict = MarkdownOption.from_dict(markdown_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


