# CreateWikiPageOptions

CreateWikiPageOptions form for creating wiki

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_base64** | **str** | content must be base64 encoded | [optional] 
**message** | **str** | optional commit message summarizing the change | [optional] 
**title** | **str** | page title. leave empty to keep unchanged | [optional] 

## Example

```python
from clientapi_forgejo.models.create_wiki_page_options import CreateWikiPageOptions

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWikiPageOptions from a JSON string
create_wiki_page_options_instance = CreateWikiPageOptions.from_json(json)
# print the JSON string representation of the object
print CreateWikiPageOptions.to_json()

# convert the object into a dict
create_wiki_page_options_dict = create_wiki_page_options_instance.to_dict()
# create an instance of CreateWikiPageOptions from a dict
create_wiki_page_options_form_dict = create_wiki_page_options.from_dict(create_wiki_page_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


