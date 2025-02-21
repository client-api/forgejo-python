# RepoTopicOptions

RepoTopicOptions a collection of repo topic names

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topics** | **List[str]** | list of topic names | [optional] 

## Example

```python
from clientapi_forgejo.models.repo_topic_options import RepoTopicOptions

# TODO update the JSON string below
json = "{}"
# create an instance of RepoTopicOptions from a JSON string
repo_topic_options_instance = RepoTopicOptions.from_json(json)
# print the JSON string representation of the object
print(RepoTopicOptions.to_json())

# convert the object into a dict
repo_topic_options_dict = repo_topic_options_instance.to_dict()
# create an instance of RepoTopicOptions from a dict
repo_topic_options_from_dict = RepoTopicOptions.from_dict(repo_topic_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


