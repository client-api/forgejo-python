# CreateIssueOption

CreateIssueOption options to create one issue

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignee** | **str** | deprecated | [optional] 
**assignees** | **List[str]** |  | [optional] 
**body** | **str** |  | [optional] 
**closed** | **bool** |  | [optional] 
**due_date** | **datetime** |  | [optional] 
**labels** | **List[int]** | list of label ids | [optional] 
**milestone** | **int** | milestone id | [optional] 
**ref** | **str** |  | [optional] 
**title** | **str** |  | 

## Example

```python
from clientapi_forgejo.models.create_issue_option import CreateIssueOption

# TODO update the JSON string below
json = "{}"
# create an instance of CreateIssueOption from a JSON string
create_issue_option_instance = CreateIssueOption.from_json(json)
# print the JSON string representation of the object
print(CreateIssueOption.to_json())

# convert the object into a dict
create_issue_option_dict = create_issue_option_instance.to_dict()
# create an instance of CreateIssueOption from a dict
create_issue_option_from_dict = CreateIssueOption.from_dict(create_issue_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


