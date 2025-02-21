# AddCollaboratorOption

AddCollaboratorOption options when adding a user as a collaborator of a repository

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permission** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.add_collaborator_option import AddCollaboratorOption

# TODO update the JSON string below
json = "{}"
# create an instance of AddCollaboratorOption from a JSON string
add_collaborator_option_instance = AddCollaboratorOption.from_json(json)
# print the JSON string representation of the object
print(AddCollaboratorOption.to_json())

# convert the object into a dict
add_collaborator_option_dict = add_collaborator_option_instance.to_dict()
# create an instance of AddCollaboratorOption from a dict
add_collaborator_option_from_dict = AddCollaboratorOption.from_dict(add_collaborator_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


