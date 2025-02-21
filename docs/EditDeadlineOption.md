# EditDeadlineOption

EditDeadlineOption options for creating a deadline

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**due_date** | **datetime** |  | 

## Example

```python
from clientapi_forgejo.models.edit_deadline_option import EditDeadlineOption

# TODO update the JSON string below
json = "{}"
# create an instance of EditDeadlineOption from a JSON string
edit_deadline_option_instance = EditDeadlineOption.from_json(json)
# print the JSON string representation of the object
print(EditDeadlineOption.to_json())

# convert the object into a dict
edit_deadline_option_dict = edit_deadline_option_instance.to_dict()
# create an instance of EditDeadlineOption from a dict
edit_deadline_option_from_dict = EditDeadlineOption.from_dict(edit_deadline_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


