# Release

Release represents a repository release

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assets** | [**List[Attachment]**](Attachment.md) |  | [optional] 
**author** | [**User**](User.md) |  | [optional] 
**body** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**draft** | **bool** |  | [optional] 
**html_url** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**prerelease** | **bool** |  | [optional] 
**published_at** | **datetime** |  | [optional] 
**tag_name** | **str** |  | [optional] 
**tarball_url** | **str** |  | [optional] 
**target_commitish** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**zipball_url** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.release import Release

# TODO update the JSON string below
json = "{}"
# create an instance of Release from a JSON string
release_instance = Release.from_json(json)
# print the JSON string representation of the object
print Release.to_json()

# convert the object into a dict
release_dict = release_instance.to_dict()
# create an instance of Release from a dict
release_form_dict = release.from_dict(release_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


