# EditIssueOption

EditIssueOption options for editing an issue

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignee** | **str** | deprecated | [optional] 
**assignees** | **List[str]** |  | [optional] 
**body** | **str** |  | [optional] 
**due_date** | **datetime** |  | [optional] 
**milestone** | **int** |  | [optional] 
**ref** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**unset_due_date** | **bool** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.edit_issue_option import EditIssueOption

# TODO update the JSON string below
json = "{}"
# create an instance of EditIssueOption from a JSON string
edit_issue_option_instance = EditIssueOption.from_json(json)
# print the JSON string representation of the object
print(EditIssueOption.to_json())

# convert the object into a dict
edit_issue_option_dict = edit_issue_option_instance.to_dict()
# create an instance of EditIssueOption from a dict
edit_issue_option_from_dict = EditIssueOption.from_dict(edit_issue_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


