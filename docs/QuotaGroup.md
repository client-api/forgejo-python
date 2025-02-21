# QuotaGroup

QuotaGroup represents a quota group

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the group | [optional] 
**rules** | [**List[QuotaRuleInfo]**](QuotaRuleInfo.md) | Rules associated with the group | [optional] 

## Example

```python
from clientapi_forgejo.models.quota_group import QuotaGroup

# TODO update the JSON string below
json = "{}"
# create an instance of QuotaGroup from a JSON string
quota_group_instance = QuotaGroup.from_json(json)
# print the JSON string representation of the object
print(QuotaGroup.to_json())

# convert the object into a dict
quota_group_dict = quota_group_instance.to_dict()
# create an instance of QuotaGroup from a dict
quota_group_from_dict = QuotaGroup.from_dict(quota_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


