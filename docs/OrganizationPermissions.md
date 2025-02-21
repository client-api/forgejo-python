# OrganizationPermissions

OrganizationPermissions list different users permissions on an organization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_create_repository** | **bool** |  | [optional] 
**can_read** | **bool** |  | [optional] 
**can_write** | **bool** |  | [optional] 
**is_admin** | **bool** |  | [optional] 
**is_owner** | **bool** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.organization_permissions import OrganizationPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationPermissions from a JSON string
organization_permissions_instance = OrganizationPermissions.from_json(json)
# print the JSON string representation of the object
print(OrganizationPermissions.to_json())

# convert the object into a dict
organization_permissions_dict = organization_permissions_instance.to_dict()
# create an instance of OrganizationPermissions from a dict
organization_permissions_from_dict = OrganizationPermissions.from_dict(organization_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


