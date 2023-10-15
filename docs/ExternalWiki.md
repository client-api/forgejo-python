# ExternalWiki

ExternalWiki represents setting for external wiki

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_wiki_url** | **str** | URL of external wiki. | [optional] 

## Example

```python
from clientapi_forgejo.models.external_wiki import ExternalWiki

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalWiki from a JSON string
external_wiki_instance = ExternalWiki.from_json(json)
# print the JSON string representation of the object
print ExternalWiki.to_json()

# convert the object into a dict
external_wiki_dict = external_wiki_instance.to_dict()
# create an instance of ExternalWiki from a dict
external_wiki_form_dict = external_wiki.from_dict(external_wiki_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


