# SubmitPullReviewOptions

SubmitPullReviewOptions are options to submit a pending pull review

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** |  | [optional] 
**event** | **str** | ReviewStateType review state type | [optional] 

## Example

```python
from clientapi_forgejo.models.submit_pull_review_options import SubmitPullReviewOptions

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitPullReviewOptions from a JSON string
submit_pull_review_options_instance = SubmitPullReviewOptions.from_json(json)
# print the JSON string representation of the object
print(SubmitPullReviewOptions.to_json())

# convert the object into a dict
submit_pull_review_options_dict = submit_pull_review_options_instance.to_dict()
# create an instance of SubmitPullReviewOptions from a dict
submit_pull_review_options_from_dict = SubmitPullReviewOptions.from_dict(submit_pull_review_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


