# EditQuotaRuleOptions

EditQuotaRuleOptions represents the options for editing a quota rule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | The limit set by the rule | [optional] 
**subjects** | **List[str]** | The subjects affected by the rule | [optional] 

## Example

```python
from clientapi_forgejo.models.edit_quota_rule_options import EditQuotaRuleOptions

# TODO update the JSON string below
json = "{}"
# create an instance of EditQuotaRuleOptions from a JSON string
edit_quota_rule_options_instance = EditQuotaRuleOptions.from_json(json)
# print the JSON string representation of the object
print(EditQuotaRuleOptions.to_json())

# convert the object into a dict
edit_quota_rule_options_dict = edit_quota_rule_options_instance.to_dict()
# create an instance of EditQuotaRuleOptions from a dict
edit_quota_rule_options_from_dict = EditQuotaRuleOptions.from_dict(edit_quota_rule_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


