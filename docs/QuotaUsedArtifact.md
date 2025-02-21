# QuotaUsedArtifact

QuotaUsedArtifact represents an artifact counting towards a user's quota

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**html_url** | **str** | HTML URL to the action run containing the artifact | [optional] 
**name** | **str** | Name of the artifact | [optional] 
**size** | **int** | Size of the artifact (compressed) | [optional] 

## Example

```python
from clientapi_forgejo.models.quota_used_artifact import QuotaUsedArtifact

# TODO update the JSON string below
json = "{}"
# create an instance of QuotaUsedArtifact from a JSON string
quota_used_artifact_instance = QuotaUsedArtifact.from_json(json)
# print the JSON string representation of the object
print(QuotaUsedArtifact.to_json())

# convert the object into a dict
quota_used_artifact_dict = quota_used_artifact_instance.to_dict()
# create an instance of QuotaUsedArtifact from a dict
quota_used_artifact_from_dict = QuotaUsedArtifact.from_dict(quota_used_artifact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


