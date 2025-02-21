# NotificationSubject

NotificationSubject contains the notification subject (Issue/Pull/Commit)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**html_url** | **str** |  | [optional] 
**latest_comment_html_url** | **str** |  | [optional] 
**latest_comment_url** | **str** |  | [optional] 
**state** | **str** | StateType issue state type | [optional] 
**title** | **str** |  | [optional] 
**type** | **str** | NotifySubjectType represent type of notification subject | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.notification_subject import NotificationSubject

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationSubject from a JSON string
notification_subject_instance = NotificationSubject.from_json(json)
# print the JSON string representation of the object
print(NotificationSubject.to_json())

# convert the object into a dict
notification_subject_dict = notification_subject_instance.to_dict()
# create an instance of NotificationSubject from a dict
notification_subject_from_dict = NotificationSubject.from_dict(notification_subject_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


