# GenerateRepoOption

GenerateRepoOption options when creating repository using a template

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatar** | **bool** | include avatar of the template repo | [optional] 
**default_branch** | **str** | Default branch of the new repository | [optional] 
**description** | **str** | Description of the repository to create | [optional] 
**git_content** | **bool** | include git content of default branch in template repo | [optional] 
**git_hooks** | **bool** | include git hooks in template repo | [optional] 
**labels** | **bool** | include labels in template repo | [optional] 
**name** | **str** | Name of the repository to create | 
**owner** | **str** | The organization or person who will own the new repository | 
**private** | **bool** | Whether the repository is private | [optional] 
**topics** | **bool** | include topics in template repo | [optional] 
**webhooks** | **bool** | include webhooks in template repo | [optional] 

## Example

```python
from clientapi_forgejo.models.generate_repo_option import GenerateRepoOption

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateRepoOption from a JSON string
generate_repo_option_instance = GenerateRepoOption.from_json(json)
# print the JSON string representation of the object
print GenerateRepoOption.to_json()

# convert the object into a dict
generate_repo_option_dict = generate_repo_option_instance.to_dict()
# create an instance of GenerateRepoOption from a dict
generate_repo_option_form_dict = generate_repo_option.from_dict(generate_repo_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


