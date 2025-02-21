# CreateQuotaRuleOptions

CreateQuotaRuleOptions represents the options for creating a quota rule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | The limit set by the rule | [optional] 
**name** | **str** | Name of the rule to create | [optional] 
**subjects** | **List[str]** | The subjects affected by the rule | [optional] 

## Example

```python
from clientapi_forgejo.models.create_quota_rule_options import CreateQuotaRuleOptions

# TODO update the JSON string below
json = "{}"
# create an instance of CreateQuotaRuleOptions from a JSON string
create_quota_rule_options_instance = CreateQuotaRuleOptions.from_json(json)
# print the JSON string representation of the object
print(CreateQuotaRuleOptions.to_json())

# convert the object into a dict
create_quota_rule_options_dict = create_quota_rule_options_instance.to_dict()
# create an instance of CreateQuotaRuleOptions from a dict
create_quota_rule_options_from_dict = CreateQuotaRuleOptions.from_dict(create_quota_rule_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


