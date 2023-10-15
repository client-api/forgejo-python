# NodeInfo

NodeInfo contains standardized way of exposing metadata about a server running one of the distributed social networks

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **object** |  | [optional] 
**open_registrations** | **bool** |  | [optional] 
**protocols** | **List[str]** |  | [optional] 
**services** | [**NodeInfoServices**](NodeInfoServices.md) |  | [optional] 
**software** | [**NodeInfoSoftware**](NodeInfoSoftware.md) |  | [optional] 
**usage** | [**NodeInfoUsage**](NodeInfoUsage.md) |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.node_info import NodeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NodeInfo from a JSON string
node_info_instance = NodeInfo.from_json(json)
# print the JSON string representation of the object
print NodeInfo.to_json()

# convert the object into a dict
node_info_dict = node_info_instance.to_dict()
# create an instance of NodeInfo from a dict
node_info_form_dict = node_info.from_dict(node_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


