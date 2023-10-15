# NotificationThread

NotificationThread expose Notification on API

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**pinned** | **bool** |  | [optional] 
**repository** | [**Repository**](Repository.md) |  | [optional] 
**subject** | [**NotificationSubject**](NotificationSubject.md) |  | [optional] 
**unread** | **bool** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.notification_thread import NotificationThread

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationThread from a JSON string
notification_thread_instance = NotificationThread.from_json(json)
# print the JSON string representation of the object
print NotificationThread.to_json()

# convert the object into a dict
notification_thread_dict = notification_thread_instance.to_dict()
# create an instance of NotificationThread from a dict
notification_thread_form_dict = notification_thread.from_dict(notification_thread_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


