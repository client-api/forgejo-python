# IssueTemplate

IssueTemplate represents an issue template for a repository

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**about** | **str** |  | [optional] 
**body** | [**List[IssueFormField]**](IssueFormField.md) |  | [optional] 
**content** | **str** |  | [optional] 
**file_name** | **str** |  | [optional] 
**labels** | **List[str]** |  | [optional] 
**name** | **str** |  | [optional] 
**ref** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.issue_template import IssueTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of IssueTemplate from a JSON string
issue_template_instance = IssueTemplate.from_json(json)
# print the JSON string representation of the object
print IssueTemplate.to_json()

# convert the object into a dict
issue_template_dict = issue_template_instance.to_dict()
# create an instance of IssueTemplate from a dict
issue_template_form_dict = issue_template.from_dict(issue_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


