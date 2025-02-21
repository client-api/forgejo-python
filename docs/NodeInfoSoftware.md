# NodeInfoSoftware

NodeInfoSoftware contains Metadata about server software in use

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**homepage** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**repository** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.node_info_software import NodeInfoSoftware

# TODO update the JSON string below
json = "{}"
# create an instance of NodeInfoSoftware from a JSON string
node_info_software_instance = NodeInfoSoftware.from_json(json)
# print the JSON string representation of the object
print(NodeInfoSoftware.to_json())

# convert the object into a dict
node_info_software_dict = node_info_software_instance.to_dict()
# create an instance of NodeInfoSoftware from a dict
node_info_software_from_dict = NodeInfoSoftware.from_dict(node_info_software_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


