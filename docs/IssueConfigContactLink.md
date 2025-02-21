# IssueConfigContactLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**about** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.issue_config_contact_link import IssueConfigContactLink

# TODO update the JSON string below
json = "{}"
# create an instance of IssueConfigContactLink from a JSON string
issue_config_contact_link_instance = IssueConfigContactLink.from_json(json)
# print the JSON string representation of the object
print(IssueConfigContactLink.to_json())

# convert the object into a dict
issue_config_contact_link_dict = issue_config_contact_link_instance.to_dict()
# create an instance of IssueConfigContactLink from a dict
issue_config_contact_link_from_dict = IssueConfigContactLink.from_dict(issue_config_contact_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


