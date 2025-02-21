# DeleteLabelsOption

DeleteLabelOption options for deleting a label

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.delete_labels_option import DeleteLabelsOption

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteLabelsOption from a JSON string
delete_labels_option_instance = DeleteLabelsOption.from_json(json)
# print the JSON string representation of the object
print(DeleteLabelsOption.to_json())

# convert the object into a dict
delete_labels_option_dict = delete_labels_option_instance.to_dict()
# create an instance of DeleteLabelsOption from a dict
delete_labels_option_from_dict = DeleteLabelsOption.from_dict(delete_labels_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


