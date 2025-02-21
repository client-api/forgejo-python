# Compare


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commits** | [**List[Commit]**](Commit.md) |  | [optional] 
**total_commits** | **int** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.compare import Compare

# TODO update the JSON string below
json = "{}"
# create an instance of Compare from a JSON string
compare_instance = Compare.from_json(json)
# print the JSON string representation of the object
print(Compare.to_json())

# convert the object into a dict
compare_dict = compare_instance.to_dict()
# create an instance of Compare from a dict
compare_from_dict = Compare.from_dict(compare_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


