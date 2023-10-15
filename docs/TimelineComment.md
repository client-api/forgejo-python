# TimelineComment

TimelineComment represents a timeline comment (comment of any type) on a commit or issue

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignee** | [**User**](User.md) |  | [optional] 
**assignee_team** | [**Team**](Team.md) |  | [optional] 
**body** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**dependent_issue** | [**Issue**](Issue.md) |  | [optional] 
**html_url** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**issue_url** | **str** |  | [optional] 
**label** | [**Label**](Label.md) |  | [optional] 
**milestone** | [**Milestone**](Milestone.md) |  | [optional] 
**new_ref** | **str** |  | [optional] 
**new_title** | **str** |  | [optional] 
**old_milestone** | [**Milestone**](Milestone.md) |  | [optional] 
**old_project_id** | **int** |  | [optional] 
**old_ref** | **str** |  | [optional] 
**old_title** | **str** |  | [optional] 
**project_id** | **int** |  | [optional] 
**pull_request_url** | **str** |  | [optional] 
**ref_action** | **str** |  | [optional] 
**ref_comment** | [**Comment**](Comment.md) |  | [optional] 
**ref_commit_sha** | **str** | commit SHA where issue/PR was referenced | [optional] 
**ref_issue** | [**Issue**](Issue.md) |  | [optional] 
**removed_assignee** | **bool** | whether the assignees were removed or added | [optional] 
**resolve_doer** | [**User**](User.md) |  | [optional] 
**review_id** | **int** |  | [optional] 
**tracked_time** | [**TrackedTime**](TrackedTime.md) |  | [optional] 
**type** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**user** | [**User**](User.md) |  | [optional] 

## Example

```python
from clientapi_forgejo.models.timeline_comment import TimelineComment

# TODO update the JSON string below
json = "{}"
# create an instance of TimelineComment from a JSON string
timeline_comment_instance = TimelineComment.from_json(json)
# print the JSON string representation of the object
print TimelineComment.to_json()

# convert the object into a dict
timeline_comment_dict = timeline_comment_instance.to_dict()
# create an instance of TimelineComment from a dict
timeline_comment_form_dict = timeline_comment.from_dict(timeline_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


