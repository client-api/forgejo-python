# PayloadCommit

PayloadCommit represents a commit

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**added** | **List[str]** |  | [optional] 
**author** | [**PayloadUser**](PayloadUser.md) |  | [optional] 
**committer** | [**PayloadUser**](PayloadUser.md) |  | [optional] 
**id** | **str** | sha1 hash of the commit | [optional] 
**message** | **str** |  | [optional] 
**modified** | **List[str]** |  | [optional] 
**removed** | **List[str]** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**url** | **str** |  | [optional] 
**verification** | [**PayloadCommitVerification**](PayloadCommitVerification.md) |  | [optional] 

## Example

```python
from clientapi_forgejo.models.payload_commit import PayloadCommit

# TODO update the JSON string below
json = "{}"
# create an instance of PayloadCommit from a JSON string
payload_commit_instance = PayloadCommit.from_json(json)
# print the JSON string representation of the object
print PayloadCommit.to_json()

# convert the object into a dict
payload_commit_dict = payload_commit_instance.to_dict()
# create an instance of PayloadCommit from a dict
payload_commit_form_dict = payload_commit.from_dict(payload_commit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


