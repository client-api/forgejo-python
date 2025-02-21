# CreateTagProtectionOption

CreateTagProtectionOption options for creating a tag protection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name_pattern** | **str** |  | [optional] 
**whitelist_teams** | **List[str]** |  | [optional] 
**whitelist_usernames** | **List[str]** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.create_tag_protection_option import CreateTagProtectionOption

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTagProtectionOption from a JSON string
create_tag_protection_option_instance = CreateTagProtectionOption.from_json(json)
# print the JSON string representation of the object
print(CreateTagProtectionOption.to_json())

# convert the object into a dict
create_tag_protection_option_dict = create_tag_protection_option_instance.to_dict()
# create an instance of CreateTagProtectionOption from a dict
create_tag_protection_option_from_dict = CreateTagProtectionOption.from_dict(create_tag_protection_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


