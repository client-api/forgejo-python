# PackageFile

PackageFile represents a package file

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**md5** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**sha1** | **str** |  | [optional] 
**sha256** | **str** |  | [optional] 
**sha512** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.package_file import PackageFile

# TODO update the JSON string below
json = "{}"
# create an instance of PackageFile from a JSON string
package_file_instance = PackageFile.from_json(json)
# print the JSON string representation of the object
print PackageFile.to_json()

# convert the object into a dict
package_file_dict = package_file_instance.to_dict()
# create an instance of PackageFile from a dict
package_file_form_dict = package_file.from_dict(package_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


