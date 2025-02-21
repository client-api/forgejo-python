# UpdateUserAvatarOption

UpdateUserAvatarUserOption options when updating the user avatar

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | **str** | image must be base64 encoded | [optional] 

## Example

```python
from clientapi_forgejo.models.update_user_avatar_option import UpdateUserAvatarOption

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserAvatarOption from a JSON string
update_user_avatar_option_instance = UpdateUserAvatarOption.from_json(json)
# print the JSON string representation of the object
print(UpdateUserAvatarOption.to_json())

# convert the object into a dict
update_user_avatar_option_dict = update_user_avatar_option_instance.to_dict()
# create an instance of UpdateUserAvatarOption from a dict
update_user_avatar_option_from_dict = UpdateUserAvatarOption.from_dict(update_user_avatar_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


