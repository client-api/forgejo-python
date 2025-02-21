# UserSettingsOptions

UserSettingsOptions represents options to change user settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**diff_view_style** | **str** |  | [optional] 
**enable_repo_unit_hints** | **bool** |  | [optional] 
**full_name** | **str** |  | [optional] 
**hide_activity** | **bool** |  | [optional] 
**hide_email** | **bool** | Privacy | [optional] 
**language** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**pronouns** | **str** |  | [optional] 
**theme** | **str** |  | [optional] 
**website** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.user_settings_options import UserSettingsOptions

# TODO update the JSON string below
json = "{}"
# create an instance of UserSettingsOptions from a JSON string
user_settings_options_instance = UserSettingsOptions.from_json(json)
# print the JSON string representation of the object
print(UserSettingsOptions.to_json())

# convert the object into a dict
user_settings_options_dict = user_settings_options_instance.to_dict()
# create an instance of UserSettingsOptions from a dict
user_settings_options_from_dict = UserSettingsOptions.from_dict(user_settings_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


