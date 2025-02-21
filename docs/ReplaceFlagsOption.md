# ReplaceFlagsOption

ReplaceFlagsOption options when replacing the flags of a repository

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flags** | **List[str]** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.replace_flags_option import ReplaceFlagsOption

# TODO update the JSON string below
json = "{}"
# create an instance of ReplaceFlagsOption from a JSON string
replace_flags_option_instance = ReplaceFlagsOption.from_json(json)
# print the JSON string representation of the object
print(ReplaceFlagsOption.to_json())

# convert the object into a dict
replace_flags_option_dict = replace_flags_option_instance.to_dict()
# create an instance of ReplaceFlagsOption from a dict
replace_flags_option_from_dict = ReplaceFlagsOption.from_dict(replace_flags_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


