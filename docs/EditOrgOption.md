# EditOrgOption

EditOrgOption options for editing an organization

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**full_name** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**repo_admin_change_team_access** | **bool** |  | [optional] 
**visibility** | **str** | possible values are &#x60;public&#x60;, &#x60;limited&#x60; or &#x60;private&#x60; | [optional] 
**website** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.edit_org_option import EditOrgOption

# TODO update the JSON string below
json = "{}"
# create an instance of EditOrgOption from a JSON string
edit_org_option_instance = EditOrgOption.from_json(json)
# print the JSON string representation of the object
print EditOrgOption.to_json()

# convert the object into a dict
edit_org_option_dict = edit_org_option_instance.to_dict()
# create an instance of EditOrgOption from a dict
edit_org_option_form_dict = edit_org_option.from_dict(edit_org_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


