# Cron

Cron represents a Cron task

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exec_times** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**next** | **datetime** |  | [optional] 
**prev** | **datetime** |  | [optional] 
**schedule** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.cron import Cron

# TODO update the JSON string below
json = "{}"
# create an instance of Cron from a JSON string
cron_instance = Cron.from_json(json)
# print the JSON string representation of the object
print(Cron.to_json())

# convert the object into a dict
cron_dict = cron_instance.to_dict()
# create an instance of Cron from a dict
cron_from_dict = Cron.from_dict(cron_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


