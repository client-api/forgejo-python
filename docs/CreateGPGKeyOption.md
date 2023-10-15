# CreateGPGKeyOption

CreateGPGKeyOption options create user GPG key

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**armored_public_key** | **str** | An armored GPG key to add | 
**armored_signature** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.create_gpg_key_option import CreateGPGKeyOption

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGPGKeyOption from a JSON string
create_gpg_key_option_instance = CreateGPGKeyOption.from_json(json)
# print the JSON string representation of the object
print CreateGPGKeyOption.to_json()

# convert the object into a dict
create_gpg_key_option_dict = create_gpg_key_option_instance.to_dict()
# create an instance of CreateGPGKeyOption from a dict
create_gpg_key_option_form_dict = create_gpg_key_option.from_dict(create_gpg_key_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


