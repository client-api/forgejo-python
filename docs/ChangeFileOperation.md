# ChangeFileOperation

ChangeFileOperation for creating, updating or deleting a file

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | new or updated file content, must be base64 encoded | [optional] 
**from_path** | **str** | old path of the file to move | [optional] 
**operation** | **str** | indicates what to do with the file | 
**path** | **str** | path to the existing or new file | 
**sha** | **str** | sha is the SHA for the file that already exists, required for update or delete | [optional] 

## Example

```python
from clientapi_forgejo.models.change_file_operation import ChangeFileOperation

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeFileOperation from a JSON string
change_file_operation_instance = ChangeFileOperation.from_json(json)
# print the JSON string representation of the object
print(ChangeFileOperation.to_json())

# convert the object into a dict
change_file_operation_dict = change_file_operation_instance.to_dict()
# create an instance of ChangeFileOperation from a dict
change_file_operation_from_dict = ChangeFileOperation.from_dict(change_file_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


