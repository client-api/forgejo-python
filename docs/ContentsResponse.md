# ContentsResponse

ContentsResponse contains information about a repo's entry's (dir, file, symlink, submodule) metadata and content

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**FileLinksResponse**](FileLinksResponse.md) |  | [optional] 
**content** | **str** | &#x60;content&#x60; is populated when &#x60;type&#x60; is &#x60;file&#x60;, otherwise null | [optional] 
**download_url** | **str** |  | [optional] 
**encoding** | **str** | &#x60;encoding&#x60; is populated when &#x60;type&#x60; is &#x60;file&#x60;, otherwise null | [optional] 
**git_url** | **str** |  | [optional] 
**html_url** | **str** |  | [optional] 
**last_commit_sha** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**sha** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**submodule_git_url** | **str** | &#x60;submodule_git_url&#x60; is populated when &#x60;type&#x60; is &#x60;submodule&#x60;, otherwise null | [optional] 
**target** | **str** | &#x60;target&#x60; is populated when &#x60;type&#x60; is &#x60;symlink&#x60;, otherwise null | [optional] 
**type** | **str** | &#x60;type&#x60; will be &#x60;file&#x60;, &#x60;dir&#x60;, &#x60;symlink&#x60;, or &#x60;submodule&#x60; | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.contents_response import ContentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContentsResponse from a JSON string
contents_response_instance = ContentsResponse.from_json(json)
# print the JSON string representation of the object
print ContentsResponse.to_json()

# convert the object into a dict
contents_response_dict = contents_response_instance.to_dict()
# create an instance of ContentsResponse from a dict
contents_response_form_dict = contents_response.from_dict(contents_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


