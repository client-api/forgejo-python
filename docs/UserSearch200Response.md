# UserSearch200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[User]**](User.md) |  | [optional] 
**ok** | **bool** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.user_search200_response import UserSearch200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UserSearch200Response from a JSON string
user_search200_response_instance = UserSearch200Response.from_json(json)
# print the JSON string representation of the object
print(UserSearch200Response.to_json())

# convert the object into a dict
user_search200_response_dict = user_search200_response_instance.to_dict()
# create an instance of UserSearch200Response from a dict
user_search200_response_from_dict = UserSearch200Response.from_dict(user_search200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


