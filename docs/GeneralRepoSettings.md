# GeneralRepoSettings

GeneralRepoSettings contains global repository settings exposed by API

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_git_disabled** | **bool** |  | [optional] 
**lfs_disabled** | **bool** |  | [optional] 
**migrations_disabled** | **bool** |  | [optional] 
**mirrors_disabled** | **bool** |  | [optional] 
**stars_disabled** | **bool** |  | [optional] 
**time_tracking_disabled** | **bool** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.general_repo_settings import GeneralRepoSettings

# TODO update the JSON string below
json = "{}"
# create an instance of GeneralRepoSettings from a JSON string
general_repo_settings_instance = GeneralRepoSettings.from_json(json)
# print the JSON string representation of the object
print GeneralRepoSettings.to_json()

# convert the object into a dict
general_repo_settings_dict = general_repo_settings_instance.to_dict()
# create an instance of GeneralRepoSettings from a dict
general_repo_settings_form_dict = general_repo_settings.from_dict(general_repo_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


