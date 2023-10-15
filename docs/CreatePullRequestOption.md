# CreatePullRequestOption

CreatePullRequestOption options when creating a pull request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignee** | **str** |  | [optional] 
**assignees** | **List[str]** |  | [optional] 
**base** | **str** |  | [optional] 
**body** | **str** |  | [optional] 
**due_date** | **datetime** |  | [optional] 
**head** | **str** |  | [optional] 
**labels** | **List[int]** |  | [optional] 
**milestone** | **int** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.create_pull_request_option import CreatePullRequestOption

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePullRequestOption from a JSON string
create_pull_request_option_instance = CreatePullRequestOption.from_json(json)
# print the JSON string representation of the object
print CreatePullRequestOption.to_json()

# convert the object into a dict
create_pull_request_option_dict = create_pull_request_option_instance.to_dict()
# create an instance of CreatePullRequestOption from a dict
create_pull_request_option_form_dict = create_pull_request_option.from_dict(create_pull_request_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


