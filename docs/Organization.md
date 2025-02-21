# Organization

Organization represents an organization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatar_url** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**full_name** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**location** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**repo_admin_change_team_access** | **bool** |  | [optional] 
**username** | **str** | deprecated | [optional] 
**visibility** | **str** |  | [optional] 
**website** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.organization import Organization

# TODO update the JSON string below
json = "{}"
# create an instance of Organization from a JSON string
organization_instance = Organization.from_json(json)
# print the JSON string representation of the object
print(Organization.to_json())

# convert the object into a dict
organization_dict = organization_instance.to_dict()
# create an instance of Organization from a dict
organization_from_dict = Organization.from_dict(organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


