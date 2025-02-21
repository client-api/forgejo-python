# TagProtection

TagProtection represents a tag protection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**id** | **int** |  | [optional] 
**name_pattern** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**whitelist_teams** | **List[str]** |  | [optional] 
**whitelist_usernames** | **List[str]** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.tag_protection import TagProtection

# TODO update the JSON string below
json = "{}"
# create an instance of TagProtection from a JSON string
tag_protection_instance = TagProtection.from_json(json)
# print the JSON string representation of the object
print(TagProtection.to_json())

# convert the object into a dict
tag_protection_dict = tag_protection_instance.to_dict()
# create an instance of TagProtection from a dict
tag_protection_from_dict = TagProtection.from_dict(tag_protection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


