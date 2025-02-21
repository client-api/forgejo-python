# CreateOrUpdateSecretOption

CreateOrUpdateSecretOption options when creating or updating secret

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** | Data of the secret to update | 

## Example

```python
from clientapi_forgejo.models.create_or_update_secret_option import CreateOrUpdateSecretOption

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrUpdateSecretOption from a JSON string
create_or_update_secret_option_instance = CreateOrUpdateSecretOption.from_json(json)
# print the JSON string representation of the object
print(CreateOrUpdateSecretOption.to_json())

# convert the object into a dict
create_or_update_secret_option_dict = create_or_update_secret_option_instance.to_dict()
# create an instance of CreateOrUpdateSecretOption from a dict
create_or_update_secret_option_from_dict = CreateOrUpdateSecretOption.from_dict(create_or_update_secret_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


