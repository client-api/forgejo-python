# ActivityPub

ActivityPub type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.activity_pub import ActivityPub

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityPub from a JSON string
activity_pub_instance = ActivityPub.from_json(json)
# print the JSON string representation of the object
print(ActivityPub.to_json())

# convert the object into a dict
activity_pub_dict = activity_pub_instance.to_dict()
# create an instance of ActivityPub from a dict
activity_pub_from_dict = ActivityPub.from_dict(activity_pub_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


