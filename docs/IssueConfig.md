# IssueConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blank_issues_enabled** | **bool** |  | [optional] 
**contact_links** | [**List[IssueConfigContactLink]**](IssueConfigContactLink.md) |  | [optional] 

## Example

```python
from clientapi_forgejo.models.issue_config import IssueConfig

# TODO update the JSON string below
json = "{}"
# create an instance of IssueConfig from a JSON string
issue_config_instance = IssueConfig.from_json(json)
# print the JSON string representation of the object
print IssueConfig.to_json()

# convert the object into a dict
issue_config_dict = issue_config_instance.to_dict()
# create an instance of IssueConfig from a dict
issue_config_form_dict = issue_config.from_dict(issue_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


