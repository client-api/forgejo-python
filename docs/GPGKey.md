# GPGKey

GPGKey a user GPG key to sign commit and tag in repository

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_certify** | **bool** |  | [optional] 
**can_encrypt_comms** | **bool** |  | [optional] 
**can_encrypt_storage** | **bool** |  | [optional] 
**can_sign** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**emails** | [**List[GPGKeyEmail]**](GPGKeyEmail.md) |  | [optional] 
**expires_at** | **datetime** |  | [optional] 
**id** | **int** |  | [optional] 
**key_id** | **str** |  | [optional] 
**primary_key_id** | **str** |  | [optional] 
**public_key** | **str** |  | [optional] 
**subkeys** | [**List[GPGKey]**](GPGKey.md) |  | [optional] 
**verified** | **bool** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.gpg_key import GPGKey

# TODO update the JSON string below
json = "{}"
# create an instance of GPGKey from a JSON string
gpg_key_instance = GPGKey.from_json(json)
# print the JSON string representation of the object
print GPGKey.to_json()

# convert the object into a dict
gpg_key_dict = gpg_key_instance.to_dict()
# create an instance of GPGKey from a dict
gpg_key_form_dict = gpg_key.from_dict(gpg_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


