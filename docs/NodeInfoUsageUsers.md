# NodeInfoUsageUsers

NodeInfoUsageUsers contains statistics about the users of this server

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_halfyear** | **int** |  | [optional] 
**active_month** | **int** |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.node_info_usage_users import NodeInfoUsageUsers

# TODO update the JSON string below
json = "{}"
# create an instance of NodeInfoUsageUsers from a JSON string
node_info_usage_users_instance = NodeInfoUsageUsers.from_json(json)
# print the JSON string representation of the object
print(NodeInfoUsageUsers.to_json())

# convert the object into a dict
node_info_usage_users_dict = node_info_usage_users_instance.to_dict()
# create an instance of NodeInfoUsageUsers from a dict
node_info_usage_users_from_dict = NodeInfoUsageUsers.from_dict(node_info_usage_users_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


