# CreateEmailOption

CreateEmailOption options when creating email addresses

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emails** | **List[str]** | email addresses to add | [optional] 

## Example

```python
from clientapi_forgejo.models.create_email_option import CreateEmailOption

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEmailOption from a JSON string
create_email_option_instance = CreateEmailOption.from_json(json)
# print the JSON string representation of the object
print(CreateEmailOption.to_json())

# convert the object into a dict
create_email_option_dict = create_email_option_instance.to_dict()
# create an instance of CreateEmailOption from a dict
create_email_option_from_dict = CreateEmailOption.from_dict(create_email_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


