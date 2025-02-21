# CreateKeyOption

CreateKeyOption options when creating a key

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | An armored SSH key to add | 
**read_only** | **bool** | Describe if the key has only read access or read/write | [optional] 
**title** | **str** | Title of the key to add | 

## Example

```python
from clientapi_forgejo.models.create_key_option import CreateKeyOption

# TODO update the JSON string below
json = "{}"
# create an instance of CreateKeyOption from a JSON string
create_key_option_instance = CreateKeyOption.from_json(json)
# print the JSON string representation of the object
print(CreateKeyOption.to_json())

# convert the object into a dict
create_key_option_dict = create_key_option_instance.to_dict()
# create an instance of CreateKeyOption from a dict
create_key_option_from_dict = CreateKeyOption.from_dict(create_key_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


