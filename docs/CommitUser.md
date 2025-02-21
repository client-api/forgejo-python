# CommitUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.commit_user import CommitUser

# TODO update the JSON string below
json = "{}"
# create an instance of CommitUser from a JSON string
commit_user_instance = CommitUser.from_json(json)
# print the JSON string representation of the object
print(CommitUser.to_json())

# convert the object into a dict
commit_user_dict = commit_user_instance.to_dict()
# create an instance of CommitUser from a dict
commit_user_from_dict = CommitUser.from_dict(commit_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


