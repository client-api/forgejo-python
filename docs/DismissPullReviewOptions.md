# DismissPullReviewOptions

DismissPullReviewOptions are options to dismiss a pull review

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**priors** | **bool** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.dismiss_pull_review_options import DismissPullReviewOptions

# TODO update the JSON string below
json = "{}"
# create an instance of DismissPullReviewOptions from a JSON string
dismiss_pull_review_options_instance = DismissPullReviewOptions.from_json(json)
# print the JSON string representation of the object
print(DismissPullReviewOptions.to_json())

# convert the object into a dict
dismiss_pull_review_options_dict = dismiss_pull_review_options_instance.to_dict()
# create an instance of DismissPullReviewOptions from a dict
dismiss_pull_review_options_from_dict = DismissPullReviewOptions.from_dict(dismiss_pull_review_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


