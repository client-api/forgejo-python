# CreateReleaseOption

CreateReleaseOption options when creating a release

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** |  | [optional] 
**draft** | **bool** |  | [optional] 
**hide_archive_links** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**prerelease** | **bool** |  | [optional] 
**tag_name** | **str** |  | 
**target_commitish** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.create_release_option import CreateReleaseOption

# TODO update the JSON string below
json = "{}"
# create an instance of CreateReleaseOption from a JSON string
create_release_option_instance = CreateReleaseOption.from_json(json)
# print the JSON string representation of the object
print(CreateReleaseOption.to_json())

# convert the object into a dict
create_release_option_dict = create_release_option_instance.to_dict()
# create an instance of CreateReleaseOption from a dict
create_release_option_from_dict = CreateReleaseOption.from_dict(create_release_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


