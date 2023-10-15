# MigrateRepoOptions

MigrateRepoOptions options for migrating repository's this is used to interact with api v1

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_password** | **str** |  | [optional] 
**auth_token** | **str** |  | [optional] 
**auth_username** | **str** |  | [optional] 
**clone_addr** | **str** |  | 
**description** | **str** |  | [optional] 
**issues** | **bool** |  | [optional] 
**labels** | **bool** |  | [optional] 
**lfs** | **bool** |  | [optional] 
**lfs_endpoint** | **str** |  | [optional] 
**milestones** | **bool** |  | [optional] 
**mirror** | **bool** |  | [optional] 
**mirror_interval** | **str** |  | [optional] 
**private** | **bool** |  | [optional] 
**pull_requests** | **bool** |  | [optional] 
**releases** | **bool** |  | [optional] 
**repo_name** | **str** |  | 
**repo_owner** | **str** | Name of User or Organisation who will own Repo after migration | [optional] 
**service** | **str** |  | [optional] 
**uid** | **int** | deprecated (only for backwards compatibility) | [optional] 
**wiki** | **bool** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.migrate_repo_options import MigrateRepoOptions

# TODO update the JSON string below
json = "{}"
# create an instance of MigrateRepoOptions from a JSON string
migrate_repo_options_instance = MigrateRepoOptions.from_json(json)
# print the JSON string representation of the object
print MigrateRepoOptions.to_json()

# convert the object into a dict
migrate_repo_options_dict = migrate_repo_options_instance.to_dict()
# create an instance of MigrateRepoOptions from a dict
migrate_repo_options_form_dict = migrate_repo_options.from_dict(migrate_repo_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


