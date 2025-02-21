# APIForbiddenError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.api_forbidden_error import APIForbiddenError

# TODO update the JSON string below
json = "{}"
# create an instance of APIForbiddenError from a JSON string
api_forbidden_error_instance = APIForbiddenError.from_json(json)
# print the JSON string representation of the object
print(APIForbiddenError.to_json())

# convert the object into a dict
api_forbidden_error_dict = api_forbidden_error_instance.to_dict()
# create an instance of APIForbiddenError from a dict
api_forbidden_error_from_dict = APIForbiddenError.from_dict(api_forbidden_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


