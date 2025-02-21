# CreateRepoOption

CreateRepoOption options when creating repository

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_init** | **bool** | Whether the repository should be auto-initialized? | [optional] 
**default_branch** | **str** | DefaultBranch of the repository (used when initializes and in template) | [optional] 
**description** | **str** | Description of the repository to create | [optional] 
**gitignores** | **str** | Gitignores to use | [optional] 
**issue_labels** | **str** | Label-Set to use | [optional] 
**license** | **str** | License to use | [optional] 
**name** | **str** | Name of the repository to create | 
**object_format_name** | **str** | ObjectFormatName of the underlying git repository | [optional] 
**private** | **bool** | Whether the repository is private | [optional] 
**readme** | **str** | Readme of the repository to create | [optional] 
**template** | **bool** | Whether the repository is template | [optional] 
**trust_model** | **str** | TrustModel of the repository | [optional] 

## Example

```python
from clientapi_forgejo.models.create_repo_option import CreateRepoOption

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRepoOption from a JSON string
create_repo_option_instance = CreateRepoOption.from_json(json)
# print the JSON string representation of the object
print(CreateRepoOption.to_json())

# convert the object into a dict
create_repo_option_dict = create_repo_option_instance.to_dict()
# create an instance of CreateRepoOption from a dict
create_repo_option_from_dict = CreateRepoOption.from_dict(create_repo_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


