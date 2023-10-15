# Activity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**act_user** | [**User**](User.md) |  | [optional] 
**act_user_id** | **int** |  | [optional] 
**comment** | [**Comment**](Comment.md) |  | [optional] 
**comment_id** | **int** |  | [optional] 
**content** | **str** |  | [optional] 
**created** | **datetime** |  | [optional] 
**id** | **int** |  | [optional] 
**is_private** | **bool** |  | [optional] 
**op_type** | **str** |  | [optional] 
**ref_name** | **str** |  | [optional] 
**repo** | [**Repository**](Repository.md) |  | [optional] 
**repo_id** | **int** |  | [optional] 
**user_id** | **int** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.activity import Activity

# TODO update the JSON string below
json = "{}"
# create an instance of Activity from a JSON string
activity_instance = Activity.from_json(json)
# print the JSON string representation of the object
print Activity.to_json()

# convert the object into a dict
activity_dict = activity_instance.to_dict()
# create an instance of Activity from a dict
activity_form_dict = activity.from_dict(activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


