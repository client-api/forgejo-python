# PullReviewRequestOptions

PullReviewRequestOptions are options to add or remove pull review requests

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reviewers** | **List[str]** |  | [optional] 
**team_reviewers** | **List[str]** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.pull_review_request_options import PullReviewRequestOptions

# TODO update the JSON string below
json = "{}"
# create an instance of PullReviewRequestOptions from a JSON string
pull_review_request_options_instance = PullReviewRequestOptions.from_json(json)
# print the JSON string representation of the object
print(PullReviewRequestOptions.to_json())

# convert the object into a dict
pull_review_request_options_dict = pull_review_request_options_instance.to_dict()
# create an instance of PullReviewRequestOptions from a dict
pull_review_request_options_from_dict = PullReviewRequestOptions.from_dict(pull_review_request_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


