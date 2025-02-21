# APIUnauthorizedError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.api_unauthorized_error import APIUnauthorizedError

# TODO update the JSON string below
json = "{}"
# create an instance of APIUnauthorizedError from a JSON string
api_unauthorized_error_instance = APIUnauthorizedError.from_json(json)
# print the JSON string representation of the object
print(APIUnauthorizedError.to_json())

# convert the object into a dict
api_unauthorized_error_dict = api_unauthorized_error_instance.to_dict()
# create an instance of APIUnauthorizedError from a dict
api_unauthorized_error_from_dict = APIUnauthorizedError.from_dict(api_unauthorized_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


