# IssueDeadline

IssueDeadline represents an issue deadline

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**due_date** | **datetime** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.issue_deadline import IssueDeadline

# TODO update the JSON string below
json = "{}"
# create an instance of IssueDeadline from a JSON string
issue_deadline_instance = IssueDeadline.from_json(json)
# print the JSON string representation of the object
print IssueDeadline.to_json()

# convert the object into a dict
issue_deadline_dict = issue_deadline_instance.to_dict()
# create an instance of IssueDeadline from a dict
issue_deadline_form_dict = issue_deadline.from_dict(issue_deadline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


