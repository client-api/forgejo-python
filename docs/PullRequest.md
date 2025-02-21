# PullRequest

PullRequest represents a pull request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additions** | **int** |  | [optional] 
**allow_maintainer_edit** | **bool** |  | [optional] 
**assignee** | [**User**](User.md) |  | [optional] 
**assignees** | [**List[User]**](User.md) |  | [optional] 
**base** | [**PRBranchInfo**](PRBranchInfo.md) |  | [optional] 
**body** | **str** |  | [optional] 
**changed_files** | **int** |  | [optional] 
**closed_at** | **datetime** |  | [optional] 
**comments** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**deletions** | **int** |  | [optional] 
**diff_url** | **str** |  | [optional] 
**draft** | **bool** |  | [optional] 
**due_date** | **datetime** |  | [optional] 
**head** | [**PRBranchInfo**](PRBranchInfo.md) |  | [optional] 
**html_url** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**is_locked** | **bool** |  | [optional] 
**labels** | [**List[Label]**](Label.md) |  | [optional] 
**merge_base** | **str** |  | [optional] 
**merge_commit_sha** | **str** |  | [optional] 
**mergeable** | **bool** |  | [optional] 
**merged** | **bool** |  | [optional] 
**merged_at** | **datetime** |  | [optional] 
**merged_by** | [**User**](User.md) |  | [optional] 
**milestone** | [**Milestone**](Milestone.md) |  | [optional] 
**number** | **int** |  | [optional] 
**patch_url** | **str** |  | [optional] 
**pin_order** | **int** |  | [optional] 
**requested_reviewers** | [**List[User]**](User.md) |  | [optional] 
**requested_reviewers_teams** | [**List[Team]**](Team.md) |  | [optional] 
**review_comments** | **int** | number of review comments made on the diff of a PR review (not including comments on commits or issues in a PR) | [optional] 
**state** | **str** | StateType issue state type | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**url** | **str** |  | [optional] 
**user** | [**User**](User.md) |  | [optional] 

## Example

```python
from clientapi_forgejo.models.pull_request import PullRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PullRequest from a JSON string
pull_request_instance = PullRequest.from_json(json)
# print the JSON string representation of the object
print(PullRequest.to_json())

# convert the object into a dict
pull_request_dict = pull_request_instance.to_dict()
# create an instance of PullRequest from a dict
pull_request_from_dict = PullRequest.from_dict(pull_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


