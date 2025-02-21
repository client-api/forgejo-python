# IssueMeta

IssueMeta basic issue information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** |  | [optional] 
**owner** | **str** |  | [optional] 
**repo** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.issue_meta import IssueMeta

# TODO update the JSON string below
json = "{}"
# create an instance of IssueMeta from a JSON string
issue_meta_instance = IssueMeta.from_json(json)
# print the JSON string representation of the object
print(IssueMeta.to_json())

# convert the object into a dict
issue_meta_dict = issue_meta_instance.to_dict()
# create an instance of IssueMeta from a dict
issue_meta_from_dict = IssueMeta.from_dict(issue_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


