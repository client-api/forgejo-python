# IssueFormField

IssueFormField represents a form field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | **Dict[str, object]** |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**validations** | **Dict[str, object]** |  | [optional] 
**visible** | **List[str]** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.issue_form_field import IssueFormField

# TODO update the JSON string below
json = "{}"
# create an instance of IssueFormField from a JSON string
issue_form_field_instance = IssueFormField.from_json(json)
# print the JSON string representation of the object
print(IssueFormField.to_json())

# convert the object into a dict
issue_form_field_dict = issue_form_field_instance.to_dict()
# create an instance of IssueFormField from a dict
issue_form_field_from_dict = IssueFormField.from_dict(issue_form_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


