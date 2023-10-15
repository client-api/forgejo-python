# RepositoryMeta

RepositoryMeta basic repository information

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full_name** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**owner** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.repository_meta import RepositoryMeta

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryMeta from a JSON string
repository_meta_instance = RepositoryMeta.from_json(json)
# print the JSON string representation of the object
print RepositoryMeta.to_json()

# convert the object into a dict
repository_meta_dict = repository_meta_instance.to_dict()
# create an instance of RepositoryMeta from a dict
repository_meta_form_dict = repository_meta.from_dict(repository_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


