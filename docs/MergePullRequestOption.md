# MergePullRequestOption

MergePullRequestForm form for merging Pull Request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**do** | **str** |  | 
**merge_commit_id** | **str** |  | [optional] 
**merge_message_field** | **str** |  | [optional] 
**merge_title_field** | **str** |  | [optional] 
**delete_branch_after_merge** | **bool** |  | [optional] 
**force_merge** | **bool** |  | [optional] 
**head_commit_id** | **str** |  | [optional] 
**merge_when_checks_succeed** | **bool** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.merge_pull_request_option import MergePullRequestOption

# TODO update the JSON string below
json = "{}"
# create an instance of MergePullRequestOption from a JSON string
merge_pull_request_option_instance = MergePullRequestOption.from_json(json)
# print the JSON string representation of the object
print MergePullRequestOption.to_json()

# convert the object into a dict
merge_pull_request_option_dict = merge_pull_request_option_instance.to_dict()
# create an instance of MergePullRequestOption from a dict
merge_pull_request_option_form_dict = merge_pull_request_option.from_dict(merge_pull_request_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


