# APIInvalidTopicsError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invalid_topics** | **List[str]** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.api_invalid_topics_error import APIInvalidTopicsError

# TODO update the JSON string below
json = "{}"
# create an instance of APIInvalidTopicsError from a JSON string
api_invalid_topics_error_instance = APIInvalidTopicsError.from_json(json)
# print the JSON string representation of the object
print(APIInvalidTopicsError.to_json())

# convert the object into a dict
api_invalid_topics_error_dict = api_invalid_topics_error_instance.to_dict()
# create an instance of APIInvalidTopicsError from a dict
api_invalid_topics_error_from_dict = APIInvalidTopicsError.from_dict(api_invalid_topics_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


