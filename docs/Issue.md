# Issue

Issue represents an issue in a repository

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assets** | [**List[Attachment]**](Attachment.md) |  | [optional] 
**assignee** | [**User**](User.md) |  | [optional] 
**assignees** | [**List[User]**](User.md) |  | [optional] 
**body** | **str** |  | [optional] 
**closed_at** | **datetime** |  | [optional] 
**comments** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**due_date** | **datetime** |  | [optional] 
**html_url** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**is_locked** | **bool** |  | [optional] 
**labels** | [**List[Label]**](Label.md) |  | [optional] 
**milestone** | [**Milestone**](Milestone.md) |  | [optional] 
**number** | **int** |  | [optional] 
**original_author** | **str** |  | [optional] 
**original_author_id** | **int** |  | [optional] 
**pin_order** | **int** |  | [optional] 
**pull_request** | [**PullRequestMeta**](PullRequestMeta.md) |  | [optional] 
**ref** | **str** |  | [optional] 
**repository** | [**RepositoryMeta**](RepositoryMeta.md) |  | [optional] 
**state** | **str** | StateType issue state type | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**url** | **str** |  | [optional] 
**user** | [**User**](User.md) |  | [optional] 

## Example

```python
from clientapi_forgejo.models.issue import Issue

# TODO update the JSON string below
json = "{}"
# create an instance of Issue from a JSON string
issue_instance = Issue.from_json(json)
# print the JSON string representation of the object
print Issue.to_json()

# convert the object into a dict
issue_dict = issue_instance.to_dict()
# create an instance of Issue from a dict
issue_form_dict = issue.from_dict(issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


