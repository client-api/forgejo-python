# CommitMeta


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** |  | [optional] 
**sha** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.commit_meta import CommitMeta

# TODO update the JSON string below
json = "{}"
# create an instance of CommitMeta from a JSON string
commit_meta_instance = CommitMeta.from_json(json)
# print the JSON string representation of the object
print CommitMeta.to_json()

# convert the object into a dict
commit_meta_dict = commit_meta_instance.to_dict()
# create an instance of CommitMeta from a dict
commit_meta_form_dict = commit_meta.from_dict(commit_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


