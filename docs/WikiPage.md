# WikiPage

WikiPage a wiki page

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commit_count** | **int** |  | [optional] 
**content_base64** | **str** | Page content, base64 encoded | [optional] 
**footer** | **str** |  | [optional] 
**html_url** | **str** |  | [optional] 
**last_commit** | [**WikiCommit**](WikiCommit.md) |  | [optional] 
**sidebar** | **str** |  | [optional] 
**sub_url** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.wiki_page import WikiPage

# TODO update the JSON string below
json = "{}"
# create an instance of WikiPage from a JSON string
wiki_page_instance = WikiPage.from_json(json)
# print the JSON string representation of the object
print(WikiPage.to_json())

# convert the object into a dict
wiki_page_dict = wiki_page_instance.to_dict()
# create an instance of WikiPage from a dict
wiki_page_from_dict = WikiPage.from_dict(wiki_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


