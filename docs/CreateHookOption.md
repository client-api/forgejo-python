# CreateHookOption

CreateHookOption options when create a hook

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] [default to False]
**authorization_header** | **str** |  | [optional] 
**branch_filter** | **str** |  | [optional] 
**config** | **Dict[str, str]** | CreateHookOptionConfig has all config options in it required are \&quot;content_type\&quot; and \&quot;url\&quot; Required | 
**events** | **List[str]** |  | [optional] 
**type** | **str** |  | 

## Example

```python
from clientapi_forgejo.models.create_hook_option import CreateHookOption

# TODO update the JSON string below
json = "{}"
# create an instance of CreateHookOption from a JSON string
create_hook_option_instance = CreateHookOption.from_json(json)
# print the JSON string representation of the object
print(CreateHookOption.to_json())

# convert the object into a dict
create_hook_option_dict = create_hook_option_instance.to_dict()
# create an instance of CreateHookOption from a dict
create_hook_option_from_dict = CreateHookOption.from_dict(create_hook_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


