# WatchInfo

WatchInfo represents an API watch status of one repository

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**ignored** | **bool** |  | [optional] 
**reason** | **object** |  | [optional] 
**repository_url** | **str** |  | [optional] 
**subscribed** | **bool** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.watch_info import WatchInfo

# TODO update the JSON string below
json = "{}"
# create an instance of WatchInfo from a JSON string
watch_info_instance = WatchInfo.from_json(json)
# print the JSON string representation of the object
print WatchInfo.to_json()

# convert the object into a dict
watch_info_dict = watch_info_instance.to_dict()
# create an instance of WatchInfo from a dict
watch_info_form_dict = watch_info.from_dict(watch_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


