# IssueLabelsOption

IssueLabelsOption a collection of labels

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | **List[object]** | Labels can be a list of integers representing label IDs or a list of strings representing label names | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.issue_labels_option import IssueLabelsOption

# TODO update the JSON string below
json = "{}"
# create an instance of IssueLabelsOption from a JSON string
issue_labels_option_instance = IssueLabelsOption.from_json(json)
# print the JSON string representation of the object
print(IssueLabelsOption.to_json())

# convert the object into a dict
issue_labels_option_dict = issue_labels_option_instance.to_dict()
# create an instance of IssueLabelsOption from a dict
issue_labels_option_from_dict = IssueLabelsOption.from_dict(issue_labels_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


