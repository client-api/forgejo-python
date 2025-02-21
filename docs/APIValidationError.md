# APIValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.api_validation_error import APIValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of APIValidationError from a JSON string
api_validation_error_instance = APIValidationError.from_json(json)
# print the JSON string representation of the object
print(APIValidationError.to_json())

# convert the object into a dict
api_validation_error_dict = api_validation_error_instance.to_dict()
# create an instance of APIValidationError from a dict
api_validation_error_from_dict = APIValidationError.from_dict(api_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


