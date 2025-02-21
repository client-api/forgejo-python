# CreateAccessTokenOption

CreateAccessTokenOption options when create access token

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**scopes** | **List[str]** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.create_access_token_option import CreateAccessTokenOption

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAccessTokenOption from a JSON string
create_access_token_option_instance = CreateAccessTokenOption.from_json(json)
# print the JSON string representation of the object
print(CreateAccessTokenOption.to_json())

# convert the object into a dict
create_access_token_option_dict = create_access_token_option_instance.to_dict()
# create an instance of CreateAccessTokenOption from a dict
create_access_token_option_from_dict = CreateAccessTokenOption.from_dict(create_access_token_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


