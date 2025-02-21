# BlockedUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_id** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.blocked_user import BlockedUser

# TODO update the JSON string below
json = "{}"
# create an instance of BlockedUser from a JSON string
blocked_user_instance = BlockedUser.from_json(json)
# print the JSON string representation of the object
print(BlockedUser.to_json())

# convert the object into a dict
blocked_user_dict = blocked_user_instance.to_dict()
# create an instance of BlockedUser from a dict
blocked_user_from_dict = BlockedUser.from_dict(blocked_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


