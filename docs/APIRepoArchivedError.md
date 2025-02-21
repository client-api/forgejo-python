# APIRepoArchivedError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.api_repo_archived_error import APIRepoArchivedError

# TODO update the JSON string below
json = "{}"
# create an instance of APIRepoArchivedError from a JSON string
api_repo_archived_error_instance = APIRepoArchivedError.from_json(json)
# print the JSON string representation of the object
print(APIRepoArchivedError.to_json())

# convert the object into a dict
api_repo_archived_error_dict = api_repo_archived_error_instance.to_dict()
# create an instance of APIRepoArchivedError from a dict
api_repo_archived_error_from_dict = APIRepoArchivedError.from_dict(api_repo_archived_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


