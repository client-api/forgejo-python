# EditReleaseOption

EditReleaseOption options when editing a release

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** |  | [optional] 
**draft** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**prerelease** | **bool** |  | [optional] 
**tag_name** | **str** |  | [optional] 
**target_commitish** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.edit_release_option import EditReleaseOption

# TODO update the JSON string below
json = "{}"
# create an instance of EditReleaseOption from a JSON string
edit_release_option_instance = EditReleaseOption.from_json(json)
# print the JSON string representation of the object
print EditReleaseOption.to_json()

# convert the object into a dict
edit_release_option_dict = edit_release_option_instance.to_dict()
# create an instance of EditReleaseOption from a dict
edit_release_option_form_dict = edit_release_option.from_dict(edit_release_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


