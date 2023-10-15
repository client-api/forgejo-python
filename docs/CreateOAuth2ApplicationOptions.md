# CreateOAuth2ApplicationOptions

CreateOAuth2ApplicationOptions holds options to create an oauth2 application

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confidential_client** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**redirect_uris** | **List[str]** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.create_o_auth2_application_options import CreateOAuth2ApplicationOptions

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOAuth2ApplicationOptions from a JSON string
create_o_auth2_application_options_instance = CreateOAuth2ApplicationOptions.from_json(json)
# print the JSON string representation of the object
print CreateOAuth2ApplicationOptions.to_json()

# convert the object into a dict
create_o_auth2_application_options_dict = create_o_auth2_application_options_instance.to_dict()
# create an instance of CreateOAuth2ApplicationOptions from a dict
create_o_auth2_application_options_form_dict = create_o_auth2_application_options.from_dict(create_o_auth2_application_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


