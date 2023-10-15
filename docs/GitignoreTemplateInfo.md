# GitignoreTemplateInfo

GitignoreTemplateInfo name and text of a gitignore template

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**source** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.gitignore_template_info import GitignoreTemplateInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GitignoreTemplateInfo from a JSON string
gitignore_template_info_instance = GitignoreTemplateInfo.from_json(json)
# print the JSON string representation of the object
print GitignoreTemplateInfo.to_json()

# convert the object into a dict
gitignore_template_info_dict = gitignore_template_info_instance.to_dict()
# create an instance of GitignoreTemplateInfo from a dict
gitignore_template_info_form_dict = gitignore_template_info.from_dict(gitignore_template_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


