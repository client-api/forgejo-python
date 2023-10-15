# NodeInfoUsage

NodeInfoUsage contains usage statistics for this server

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_comments** | **int** |  | [optional] 
**local_posts** | **int** |  | [optional] 
**users** | [**NodeInfoUsageUsers**](NodeInfoUsageUsers.md) |  | [optional] 

## Example

```python
from clientapi_forgejo.models.node_info_usage import NodeInfoUsage

# TODO update the JSON string below
json = "{}"
# create an instance of NodeInfoUsage from a JSON string
node_info_usage_instance = NodeInfoUsage.from_json(json)
# print the JSON string representation of the object
print NodeInfoUsage.to_json()

# convert the object into a dict
node_info_usage_dict = node_info_usage_instance.to_dict()
# create an instance of NodeInfoUsage from a dict
node_info_usage_form_dict = node_info_usage.from_dict(node_info_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


