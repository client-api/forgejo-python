# GeneralUISettings

GeneralUISettings contains global ui settings exposed by API

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_reactions** | **List[str]** |  | [optional] 
**custom_emojis** | **List[str]** |  | [optional] 
**default_theme** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.general_ui_settings import GeneralUISettings

# TODO update the JSON string below
json = "{}"
# create an instance of GeneralUISettings from a JSON string
general_ui_settings_instance = GeneralUISettings.from_json(json)
# print the JSON string representation of the object
print(GeneralUISettings.to_json())

# convert the object into a dict
general_ui_settings_dict = general_ui_settings_instance.to_dict()
# create an instance of GeneralUISettings from a dict
general_ui_settings_from_dict = GeneralUISettings.from_dict(general_ui_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


