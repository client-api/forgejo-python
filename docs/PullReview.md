# PullReview

PullReview represents a pull request review

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** |  | [optional] 
**comments_count** | **int** |  | [optional] 
**commit_id** | **str** |  | [optional] 
**dismissed** | **bool** |  | [optional] 
**html_url** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**official** | **bool** |  | [optional] 
**pull_request_url** | **str** |  | [optional] 
**stale** | **bool** |  | [optional] 
**state** | **str** | ReviewStateType review state type | [optional] 
**submitted_at** | **datetime** |  | [optional] 
**team** | [**Team**](Team.md) |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**user** | [**User**](User.md) |  | [optional] 

## Example

```python
from clientapi_forgejo.models.pull_review import PullReview

# TODO update the JSON string below
json = "{}"
# create an instance of PullReview from a JSON string
pull_review_instance = PullReview.from_json(json)
# print the JSON string representation of the object
print(PullReview.to_json())

# convert the object into a dict
pull_review_dict = pull_review_instance.to_dict()
# create an instance of PullReview from a dict
pull_review_from_dict = PullReview.from_dict(pull_review_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


