# UserHeatmapData

UserHeatmapData represents the data needed to create a heatmap

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contributions** | **int** |  | [optional] 
**timestamp** | **int** | TimeStamp defines a timestamp | [optional] 

## Example

```python
from clientapi_forgejo.models.user_heatmap_data import UserHeatmapData

# TODO update the JSON string below
json = "{}"
# create an instance of UserHeatmapData from a JSON string
user_heatmap_data_instance = UserHeatmapData.from_json(json)
# print the JSON string representation of the object
print(UserHeatmapData.to_json())

# convert the object into a dict
user_heatmap_data_dict = user_heatmap_data_instance.to_dict()
# create an instance of UserHeatmapData from a dict
user_heatmap_data_from_dict = UserHeatmapData.from_dict(user_heatmap_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


