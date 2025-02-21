# ChangedFile

ChangedFile store information about files affected by the pull request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additions** | **int** |  | [optional] 
**changes** | **int** |  | [optional] 
**contents_url** | **str** |  | [optional] 
**deletions** | **int** |  | [optional] 
**filename** | **str** |  | [optional] 
**html_url** | **str** |  | [optional] 
**previous_filename** | **str** |  | [optional] 
**raw_url** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.changed_file import ChangedFile

# TODO update the JSON string below
json = "{}"
# create an instance of ChangedFile from a JSON string
changed_file_instance = ChangedFile.from_json(json)
# print the JSON string representation of the object
print(ChangedFile.to_json())

# convert the object into a dict
changed_file_dict = changed_file_instance.to_dict()
# create an instance of ChangedFile from a dict
changed_file_from_dict = ChangedFile.from_dict(changed_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


