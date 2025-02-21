# UserSettings

UserSettings represents user settings

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
from clientapi_forgejo.models.user_settings import UserSettings

# TODO update the JSON string below
json = "{}"
# create an instance of UserSettings from a JSON string
user_settings_instance = UserSettings.from_json(json)
# print the JSON string representation of the object
print(UserSettings.to_json())

# convert the object into a dict
user_settings_dict = user_settings_instance.to_dict()
# create an instance of UserSettings from a dict
user_settings_from_dict = UserSettings.from_dict(user_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


