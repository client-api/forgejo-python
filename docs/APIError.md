# APIError

APIError is an api error with a message

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.api_error import APIError

# TODO update the JSON string below
json = "{}"
# create an instance of APIError from a JSON string
api_error_instance = APIError.from_json(json)
# print the JSON string representation of the object
print APIError.to_json()

# convert the object into a dict
api_error_dict = api_error_instance.to_dict()
# create an instance of APIError from a dict
api_error_form_dict = api_error.from_dict(api_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


