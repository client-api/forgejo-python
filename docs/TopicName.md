# TopicName

TopicName a list of repo topic names

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topics** | **List[str]** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.topic_name import TopicName

# TODO update the JSON string below
json = "{}"
# create an instance of TopicName from a JSON string
topic_name_instance = TopicName.from_json(json)
# print the JSON string representation of the object
print(TopicName.to_json())

# convert the object into a dict
topic_name_dict = topic_name_instance.to_dict()
# create an instance of TopicName from a dict
topic_name_from_dict = TopicName.from_dict(topic_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


