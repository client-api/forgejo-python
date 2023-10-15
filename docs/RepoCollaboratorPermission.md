# RepoCollaboratorPermission

RepoCollaboratorPermission to get repository permission for a collaborator

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permission** | **str** |  | [optional] 
**role_name** | **str** |  | [optional] 
**user** | [**User**](User.md) |  | [optional] 

## Example

```python
from clientapi_forgejo.models.repo_collaborator_permission import RepoCollaboratorPermission

# TODO update the JSON string below
json = "{}"
# create an instance of RepoCollaboratorPermission from a JSON string
repo_collaborator_permission_instance = RepoCollaboratorPermission.from_json(json)
# print the JSON string representation of the object
print RepoCollaboratorPermission.to_json()

# convert the object into a dict
repo_collaborator_permission_dict = repo_collaborator_permission_instance.to_dict()
# create an instance of RepoCollaboratorPermission from a dict
repo_collaborator_permission_form_dict = repo_collaborator_permission.from_dict(repo_collaborator_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


