# EditIssueCommentOption

EditIssueCommentOption options for editing a comment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** |  | 

## Example

```python
from clientapi_forgejo.models.edit_issue_comment_option import EditIssueCommentOption

# TODO update the JSON string below
json = "{}"
# create an instance of EditIssueCommentOption from a JSON string
edit_issue_comment_option_instance = EditIssueCommentOption.from_json(json)
# print the JSON string representation of the object
print EditIssueCommentOption.to_json()

# convert the object into a dict
edit_issue_comment_option_dict = edit_issue_comment_option_instance.to_dict()
# create an instance of EditIssueCommentOption from a dict
edit_issue_comment_option_form_dict = edit_issue_comment_option.from_dict(edit_issue_comment_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


