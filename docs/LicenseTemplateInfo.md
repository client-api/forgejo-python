# LicenseTemplateInfo

LicensesInfo contains information about a License

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** |  | [optional] 
**implementation** | **str** |  | [optional] 
**key** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.license_template_info import LicenseTemplateInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseTemplateInfo from a JSON string
license_template_info_instance = LicenseTemplateInfo.from_json(json)
# print the JSON string representation of the object
print(LicenseTemplateInfo.to_json())

# convert the object into a dict
license_template_info_dict = license_template_info_instance.to_dict()
# create an instance of LicenseTemplateInfo from a dict
license_template_info_from_dict = LicenseTemplateInfo.from_dict(license_template_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


