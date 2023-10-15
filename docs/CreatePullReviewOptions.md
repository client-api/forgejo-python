# CreatePullReviewOptions

CreatePullReviewOptions are options to create a pull review

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** |  | [optional] 
**comments** | [**List[CreatePullReviewComment]**](CreatePullReviewComment.md) |  | [optional] 
**commit_id** | **str** |  | [optional] 
**event** | **str** | ReviewStateType review state type | [optional] 

## Example

```python
from clientapi_forgejo.models.create_pull_review_options import CreatePullReviewOptions

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePullReviewOptions from a JSON string
create_pull_review_options_instance = CreatePullReviewOptions.from_json(json)
# print the JSON string representation of the object
print CreatePullReviewOptions.to_json()

# convert the object into a dict
create_pull_review_options_dict = create_pull_review_options_instance.to_dict()
# create an instance of CreatePullReviewOptions from a dict
create_pull_review_options_form_dict = create_pull_review_options.from_dict(create_pull_review_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


