# ServerVersion

ServerVersion wraps the version of the server

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.server_version import ServerVersion

# TODO update the JSON string below
json = "{}"
# create an instance of ServerVersion from a JSON string
server_version_instance = ServerVersion.from_json(json)
# print the JSON string representation of the object
print(ServerVersion.to_json())

# convert the object into a dict
server_version_dict = server_version_instance.to_dict()
# create an instance of ServerVersion from a dict
server_version_from_dict = ServerVersion.from_dict(server_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


