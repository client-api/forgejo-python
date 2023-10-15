# PullReviewComment

PullReviewComment represents a comment on a pull request review

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** |  | [optional] 
**commit_id** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**diff_hunk** | **str** |  | [optional] 
**html_url** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**original_commit_id** | **str** |  | [optional] 
**original_position** | **int** |  | [optional] 
**path** | **str** |  | [optional] 
**position** | **int** |  | [optional] 
**pull_request_review_id** | **int** |  | [optional] 
**pull_request_url** | **str** |  | [optional] 
**resolver** | [**User**](User.md) |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**user** | [**User**](User.md) |  | [optional] 

## Example

```python
from clientapi_forgejo.models.pull_review_comment import PullReviewComment

# TODO update the JSON string below
json = "{}"
# create an instance of PullReviewComment from a JSON string
pull_review_comment_instance = PullReviewComment.from_json(json)
# print the JSON string representation of the object
print PullReviewComment.to_json()

# convert the object into a dict
pull_review_comment_dict = pull_review_comment_instance.to_dict()
# create an instance of PullReviewComment from a dict
pull_review_comment_form_dict = pull_review_comment.from_dict(pull_review_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


