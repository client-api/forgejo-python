# RenameUserOption

RenameUserOption options when renaming a user

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_username** | **str** | New username for this user. This name cannot be in use yet by any other user. | 

## Example

```python
from clientapi_forgejo.models.rename_user_option import RenameUserOption

# TODO update the JSON string below
json = "{}"
# create an instance of RenameUserOption from a JSON string
rename_user_option_instance = RenameUserOption.from_json(json)
# print the JSON string representation of the object
print RenameUserOption.to_json()

# convert the object into a dict
rename_user_option_dict = rename_user_option_instance.to_dict()
# create an instance of RenameUserOption from a dict
rename_user_option_form_dict = rename_user_option.from_dict(rename_user_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


