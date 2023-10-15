# DeleteEmailOption

DeleteEmailOption options when deleting email addresses

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emails** | **List[str]** | email addresses to delete | [optional] 

## Example

```python
from clientapi_forgejo.models.delete_email_option import DeleteEmailOption

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteEmailOption from a JSON string
delete_email_option_instance = DeleteEmailOption.from_json(json)
# print the JSON string representation of the object
print DeleteEmailOption.to_json()

# convert the object into a dict
delete_email_option_dict = delete_email_option_instance.to_dict()
# create an instance of DeleteEmailOption from a dict
delete_email_option_form_dict = delete_email_option.from_dict(delete_email_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


