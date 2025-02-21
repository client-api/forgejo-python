# EditPullRequestOption

EditPullRequestOption options when modify pull request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_maintainer_edit** | **bool** |  | [optional] 
**assignee** | **str** |  | [optional] 
**assignees** | **List[str]** |  | [optional] 
**base** | **str** |  | [optional] 
**body** | **str** |  | [optional] 
**due_date** | **datetime** |  | [optional] 
**labels** | **List[int]** |  | [optional] 
**milestone** | **int** |  | [optional] 
**state** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**unset_due_date** | **bool** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.edit_pull_request_option import EditPullRequestOption

# TODO update the JSON string below
json = "{}"
# create an instance of EditPullRequestOption from a JSON string
edit_pull_request_option_instance = EditPullRequestOption.from_json(json)
# print the JSON string representation of the object
print(EditPullRequestOption.to_json())

# convert the object into a dict
edit_pull_request_option_dict = edit_pull_request_option_instance.to_dict()
# create an instance of EditPullRequestOption from a dict
edit_pull_request_option_from_dict = EditPullRequestOption.from_dict(edit_pull_request_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


