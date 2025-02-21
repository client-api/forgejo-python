# IssueConfigValidation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**valid** | **bool** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.issue_config_validation import IssueConfigValidation

# TODO update the JSON string below
json = "{}"
# create an instance of IssueConfigValidation from a JSON string
issue_config_validation_instance = IssueConfigValidation.from_json(json)
# print the JSON string representation of the object
print(IssueConfigValidation.to_json())

# convert the object into a dict
issue_config_validation_dict = issue_config_validation_instance.to_dict()
# create an instance of IssueConfigValidation from a dict
issue_config_validation_from_dict = IssueConfigValidation.from_dict(issue_config_validation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


