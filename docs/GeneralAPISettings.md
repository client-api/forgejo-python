# GeneralAPISettings

GeneralAPISettings contains global api settings exposed by it

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_git_trees_per_page** | **int** |  | [optional] 
**default_max_blob_size** | **int** |  | [optional] 
**default_paging_num** | **int** |  | [optional] 
**max_response_items** | **int** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.general_api_settings import GeneralAPISettings

# TODO update the JSON string below
json = "{}"
# create an instance of GeneralAPISettings from a JSON string
general_api_settings_instance = GeneralAPISettings.from_json(json)
# print the JSON string representation of the object
print(GeneralAPISettings.to_json())

# convert the object into a dict
general_api_settings_dict = general_api_settings_instance.to_dict()
# create an instance of GeneralAPISettings from a dict
general_api_settings_from_dict = GeneralAPISettings.from_dict(general_api_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


