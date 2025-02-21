# QuotaRuleInfo

QuotaRuleInfo contains information about a quota rule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | The limit set by the rule | [optional] 
**name** | **str** | Name of the rule (only shown to admins) | [optional] 
**subjects** | **List[str]** | Subjects the rule affects | [optional] 

## Example

```python
from clientapi_forgejo.models.quota_rule_info import QuotaRuleInfo

# TODO update the JSON string below
json = "{}"
# create an instance of QuotaRuleInfo from a JSON string
quota_rule_info_instance = QuotaRuleInfo.from_json(json)
# print the JSON string representation of the object
print(QuotaRuleInfo.to_json())

# convert the object into a dict
quota_rule_info_dict = quota_rule_info_instance.to_dict()
# create an instance of QuotaRuleInfo from a dict
quota_rule_info_from_dict = QuotaRuleInfo.from_dict(quota_rule_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


