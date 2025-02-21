# CreatePullReviewComment

CreatePullReviewComment represent a review comment for creation api

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** |  | [optional] 
**new_position** | **int** | if comment to new file line or 0 | [optional] 
**old_position** | **int** | if comment to old file line or 0 | [optional] 
**path** | **str** | the tree path | [optional] 

## Example

```python
from clientapi_forgejo.models.create_pull_review_comment import CreatePullReviewComment

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePullReviewComment from a JSON string
create_pull_review_comment_instance = CreatePullReviewComment.from_json(json)
# print the JSON string representation of the object
print(CreatePullReviewComment.to_json())

# convert the object into a dict
create_pull_review_comment_dict = create_pull_review_comment_instance.to_dict()
# create an instance of CreatePullReviewComment from a dict
create_pull_review_comment_from_dict = CreatePullReviewComment.from_dict(create_pull_review_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


