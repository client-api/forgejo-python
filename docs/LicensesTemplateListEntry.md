# LicensesTemplateListEntry

LicensesListEntry is used for the API

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.licenses_template_list_entry import LicensesTemplateListEntry

# TODO update the JSON string below
json = "{}"
# create an instance of LicensesTemplateListEntry from a JSON string
licenses_template_list_entry_instance = LicensesTemplateListEntry.from_json(json)
# print the JSON string representation of the object
print(LicensesTemplateListEntry.to_json())

# convert the object into a dict
licenses_template_list_entry_dict = licenses_template_list_entry_instance.to_dict()
# create an instance of LicensesTemplateListEntry from a dict
licenses_template_list_entry_from_dict = LicensesTemplateListEntry.from_dict(licenses_template_list_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


