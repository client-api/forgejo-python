# QuotaUsedPackage

QuotaUsedPackage represents a package counting towards a user's quota

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**html_url** | **str** | HTML URL to the package version | [optional] 
**name** | **str** | Name of the package | [optional] 
**size** | **int** | Size of the package version | [optional] 
**type** | **str** | Type of the package | [optional] 
**version** | **str** | Version of the package | [optional] 

## Example

```python
from clientapi_forgejo.models.quota_used_package import QuotaUsedPackage

# TODO update the JSON string below
json = "{}"
# create an instance of QuotaUsedPackage from a JSON string
quota_used_package_instance = QuotaUsedPackage.from_json(json)
# print the JSON string representation of the object
print(QuotaUsedPackage.to_json())

# convert the object into a dict
quota_used_package_dict = quota_used_package_instance.to_dict()
# create an instance of QuotaUsedPackage from a dict
quota_used_package_from_dict = QuotaUsedPackage.from_dict(quota_used_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


