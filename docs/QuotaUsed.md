# QuotaUsed

QuotaUsed represents the quota usage of a user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | [**QuotaUsedSize**](QuotaUsedSize.md) |  | [optional] 

## Example

```python
from clientapi_forgejo.models.quota_used import QuotaUsed

# TODO update the JSON string below
json = "{}"
# create an instance of QuotaUsed from a JSON string
quota_used_instance = QuotaUsed.from_json(json)
# print the JSON string representation of the object
print(QuotaUsed.to_json())

# convert the object into a dict
quota_used_dict = quota_used_instance.to_dict()
# create an instance of QuotaUsed from a dict
quota_used_from_dict = QuotaUsed.from_dict(quota_used_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


