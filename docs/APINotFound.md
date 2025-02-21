# APINotFound


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | **List[str]** |  | [optional] 
**message** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.api_not_found import APINotFound

# TODO update the JSON string below
json = "{}"
# create an instance of APINotFound from a JSON string
api_not_found_instance = APINotFound.from_json(json)
# print the JSON string representation of the object
print(APINotFound.to_json())

# convert the object into a dict
api_not_found_dict = api_not_found_instance.to_dict()
# create an instance of APINotFound from a dict
api_not_found_from_dict = APINotFound.from_dict(api_not_found_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


