# CreateQuotaGroupOptions

CreateQutaGroupOptions represents the options for creating a quota group

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the quota group to create | [optional] 
**rules** | [**List[CreateQuotaRuleOptions]**](CreateQuotaRuleOptions.md) | Rules to add to the newly created group. If a rule does not exist, it will be created. | [optional] 

## Example

```python
from clientapi_forgejo.models.create_quota_group_options import CreateQuotaGroupOptions

# TODO update the JSON string below
json = "{}"
# create an instance of CreateQuotaGroupOptions from a JSON string
create_quota_group_options_instance = CreateQuotaGroupOptions.from_json(json)
# print the JSON string representation of the object
print(CreateQuotaGroupOptions.to_json())

# convert the object into a dict
create_quota_group_options_dict = create_quota_group_options_instance.to_dict()
# create an instance of CreateQuotaGroupOptions from a dict
create_quota_group_options_from_dict = CreateQuotaGroupOptions.from_dict(create_quota_group_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


