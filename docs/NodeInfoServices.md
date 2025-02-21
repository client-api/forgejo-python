# NodeInfoServices

NodeInfoServices contains the third party sites this server can connect to via their application API

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inbound** | **List[str]** |  | [optional] 
**outbound** | **List[str]** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.node_info_services import NodeInfoServices

# TODO update the JSON string below
json = "{}"
# create an instance of NodeInfoServices from a JSON string
node_info_services_instance = NodeInfoServices.from_json(json)
# print the JSON string representation of the object
print(NodeInfoServices.to_json())

# convert the object into a dict
node_info_services_dict = node_info_services_instance.to_dict()
# create an instance of NodeInfoServices from a dict
node_info_services_from_dict = NodeInfoServices.from_dict(node_info_services_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


