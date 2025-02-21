# EditTagProtectionOption

EditTagProtectionOption options for editing a tag protection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name_pattern** | **str** |  | [optional] 
**whitelist_teams** | **List[str]** |  | [optional] 
**whitelist_usernames** | **List[str]** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.edit_tag_protection_option import EditTagProtectionOption

# TODO update the JSON string below
json = "{}"
# create an instance of EditTagProtectionOption from a JSON string
edit_tag_protection_option_instance = EditTagProtectionOption.from_json(json)
# print the JSON string representation of the object
print(EditTagProtectionOption.to_json())

# convert the object into a dict
edit_tag_protection_option_dict = edit_tag_protection_option_instance.to_dict()
# create an instance of EditTagProtectionOption from a dict
edit_tag_protection_option_from_dict = EditTagProtectionOption.from_dict(edit_tag_protection_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


