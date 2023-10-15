# NotificationCount

NotificationCount number of unread notifications

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new** | **int** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.notification_count import NotificationCount

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationCount from a JSON string
notification_count_instance = NotificationCount.from_json(json)
# print the JSON string representation of the object
print NotificationCount.to_json()

# convert the object into a dict
notification_count_dict = notification_count_instance.to_dict()
# create an instance of NotificationCount from a dict
notification_count_form_dict = notification_count.from_dict(notification_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


