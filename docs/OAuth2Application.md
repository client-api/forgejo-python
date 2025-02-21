# OAuth2Application


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**confidential_client** | **bool** |  | [optional] 
**created** | **datetime** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**redirect_uris** | **List[str]** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.o_auth2_application import OAuth2Application

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2Application from a JSON string
o_auth2_application_instance = OAuth2Application.from_json(json)
# print the JSON string representation of the object
print(OAuth2Application.to_json())

# convert the object into a dict
o_auth2_application_dict = o_auth2_application_instance.to_dict()
# create an instance of OAuth2Application from a dict
o_auth2_application_from_dict = OAuth2Application.from_dict(o_auth2_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


