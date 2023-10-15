# AddTimeOption

AddTimeOption options for adding time to an issue

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** |  | [optional] 
**time** | **int** | time in seconds | 
**user_name** | **str** | User who spent the time (optional) | [optional] 

## Example

```python
from clientapi_forgejo.models.add_time_option import AddTimeOption

# TODO update the JSON string below
json = "{}"
# create an instance of AddTimeOption from a JSON string
add_time_option_instance = AddTimeOption.from_json(json)
# print the JSON string representation of the object
print AddTimeOption.to_json()

# convert the object into a dict
add_time_option_dict = add_time_option_instance.to_dict()
# create an instance of AddTimeOption from a dict
add_time_option_form_dict = add_time_option.from_dict(add_time_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


