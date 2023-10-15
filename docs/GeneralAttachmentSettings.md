# GeneralAttachmentSettings

GeneralAttachmentSettings contains global Attachment settings exposed by API

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_types** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**max_files** | **int** |  | [optional] 
**max_size** | **int** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.general_attachment_settings import GeneralAttachmentSettings

# TODO update the JSON string below
json = "{}"
# create an instance of GeneralAttachmentSettings from a JSON string
general_attachment_settings_instance = GeneralAttachmentSettings.from_json(json)
# print the JSON string representation of the object
print GeneralAttachmentSettings.to_json()

# convert the object into a dict
general_attachment_settings_dict = general_attachment_settings_instance.to_dict()
# create an instance of GeneralAttachmentSettings from a dict
general_attachment_settings_form_dict = general_attachment_settings.from_dict(general_attachment_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


