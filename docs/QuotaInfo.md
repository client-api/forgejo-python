# QuotaInfo

QuotaInfo represents information about a user's quota

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | [**List[QuotaGroup]**](QuotaGroup.md) | QuotaGroupList represents a list of quota groups | [optional] 
**used** | [**QuotaUsed**](QuotaUsed.md) |  | [optional] 

## Example

```python
from clientapi_forgejo.models.quota_info import QuotaInfo

# TODO update the JSON string below
json = "{}"
# create an instance of QuotaInfo from a JSON string
quota_info_instance = QuotaInfo.from_json(json)
# print the JSON string representation of the object
print(QuotaInfo.to_json())

# convert the object into a dict
quota_info_dict = quota_info_instance.to_dict()
# create an instance of QuotaInfo from a dict
quota_info_from_dict = QuotaInfo.from_dict(quota_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


