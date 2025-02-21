# CreateIssueCommentOption

CreateIssueCommentOption options for creating a comment on an issue

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** |  | 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.create_issue_comment_option import CreateIssueCommentOption

# TODO update the JSON string below
json = "{}"
# create an instance of CreateIssueCommentOption from a JSON string
create_issue_comment_option_instance = CreateIssueCommentOption.from_json(json)
# print the JSON string representation of the object
print(CreateIssueCommentOption.to_json())

# convert the object into a dict
create_issue_comment_option_dict = create_issue_comment_option_instance.to_dict()
# create an instance of CreateIssueCommentOption from a dict
create_issue_comment_option_from_dict = CreateIssueCommentOption.from_dict(create_issue_comment_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


