# CreateUserOption

CreateUserOption create user options

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | For explicitly setting the user creation timestamp. Useful when users are migrated from other systems. When omitted, the user&#39;s creation timestamp will be set to \&quot;now\&quot;. | [optional] 
**email** | **str** |  | 
**full_name** | **str** |  | [optional] 
**login_name** | **str** |  | [optional] 
**must_change_password** | **bool** |  | [optional] 
**password** | **str** |  | [optional] 
**restricted** | **bool** |  | [optional] 
**send_notify** | **bool** |  | [optional] 
**source_id** | **int** |  | [optional] 
**username** | **str** |  | 
**visibility** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.create_user_option import CreateUserOption

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserOption from a JSON string
create_user_option_instance = CreateUserOption.from_json(json)
# print the JSON string representation of the object
print(CreateUserOption.to_json())

# convert the object into a dict
create_user_option_dict = create_user_option_instance.to_dict()
# create an instance of CreateUserOption from a dict
create_user_option_from_dict = CreateUserOption.from_dict(create_user_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


