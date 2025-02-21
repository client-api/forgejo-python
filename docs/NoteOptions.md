# NoteOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.note_options import NoteOptions

# TODO update the JSON string below
json = "{}"
# create an instance of NoteOptions from a JSON string
note_options_instance = NoteOptions.from_json(json)
# print the JSON string representation of the object
print(NoteOptions.to_json())

# convert the object into a dict
note_options_dict = note_options_instance.to_dict()
# create an instance of NoteOptions from a dict
note_options_from_dict = NoteOptions.from_dict(note_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


