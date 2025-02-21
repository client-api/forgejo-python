# EditTeamOption

EditTeamOption options for editing a team

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_create_org_repo** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**includes_all_repositories** | **bool** |  | [optional] 
**name** | **str** |  | 
**permission** | **str** |  | [optional] 
**units** | **List[str]** |  | [optional] 
**units_map** | **Dict[str, str]** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.edit_team_option import EditTeamOption

# TODO update the JSON string below
json = "{}"
# create an instance of EditTeamOption from a JSON string
edit_team_option_instance = EditTeamOption.from_json(json)
# print the JSON string representation of the object
print(EditTeamOption.to_json())

# convert the object into a dict
edit_team_option_dict = edit_team_option_instance.to_dict()
# create an instance of EditTeamOption from a dict
edit_team_option_from_dict = EditTeamOption.from_dict(edit_team_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


