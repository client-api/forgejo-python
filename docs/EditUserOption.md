# EditUserOption

EditUserOption edit user options

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**admin** | **bool** |  | [optional] 
**allow_create_organization** | **bool** |  | [optional] 
**allow_git_hook** | **bool** |  | [optional] 
**allow_import_local** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**full_name** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**login_name** | **str** |  | [optional] 
**max_repo_creation** | **int** |  | [optional] 
**must_change_password** | **bool** |  | [optional] 
**password** | **str** |  | [optional] 
**prohibit_login** | **bool** |  | [optional] 
**pronouns** | **str** |  | [optional] 
**restricted** | **bool** |  | [optional] 
**source_id** | **int** |  | [optional] 
**visibility** | **str** |  | [optional] 
**website** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.edit_user_option import EditUserOption

# TODO update the JSON string below
json = "{}"
# create an instance of EditUserOption from a JSON string
edit_user_option_instance = EditUserOption.from_json(json)
# print the JSON string representation of the object
print(EditUserOption.to_json())

# convert the object into a dict
edit_user_option_dict = edit_user_option_instance.to_dict()
# create an instance of EditUserOption from a dict
edit_user_option_from_dict = EditUserOption.from_dict(edit_user_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


