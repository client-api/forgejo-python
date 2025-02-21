# UpdateRepoAvatarOption

UpdateRepoAvatarUserOption options when updating the repo avatar

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | **str** | image must be base64 encoded | [optional] 

## Example

```python
from clientapi_forgejo.models.update_repo_avatar_option import UpdateRepoAvatarOption

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRepoAvatarOption from a JSON string
update_repo_avatar_option_instance = UpdateRepoAvatarOption.from_json(json)
# print the JSON string representation of the object
print(UpdateRepoAvatarOption.to_json())

# convert the object into a dict
update_repo_avatar_option_dict = update_repo_avatar_option_instance.to_dict()
# create an instance of UpdateRepoAvatarOption from a dict
update_repo_avatar_option_from_dict = UpdateRepoAvatarOption.from_dict(update_repo_avatar_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


