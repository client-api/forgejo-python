# AccessToken


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**scopes** | **List[str]** |  | [optional] 
**sha1** | **str** |  | [optional] 
**token_last_eight** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.access_token import AccessToken

# TODO update the JSON string below
json = "{}"
# create an instance of AccessToken from a JSON string
access_token_instance = AccessToken.from_json(json)
# print the JSON string representation of the object
print AccessToken.to_json()

# convert the object into a dict
access_token_dict = access_token_instance.to_dict()
# create an instance of AccessToken from a dict
access_token_form_dict = access_token.from_dict(access_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


