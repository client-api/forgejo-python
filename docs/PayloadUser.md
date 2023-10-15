# PayloadUser

PayloadUser represents the author or committer of a commit

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**name** | **str** | Full name of the commit author | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.payload_user import PayloadUser

# TODO update the JSON string below
json = "{}"
# create an instance of PayloadUser from a JSON string
payload_user_instance = PayloadUser.from_json(json)
# print the JSON string representation of the object
print PayloadUser.to_json()

# convert the object into a dict
payload_user_dict = payload_user_instance.to_dict()
# create an instance of PayloadUser from a dict
payload_user_form_dict = payload_user.from_dict(payload_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


