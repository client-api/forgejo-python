# ExternalTracker

ExternalTracker represents settings for external tracker

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_tracker_format** | **str** | External Issue Tracker URL Format. Use the placeholders {user}, {repo} and {index} for the username, repository name and issue index. | [optional] 
**external_tracker_regexp_pattern** | **str** | External Issue Tracker issue regular expression | [optional] 
**external_tracker_style** | **str** | External Issue Tracker Number Format, either &#x60;numeric&#x60;, &#x60;alphanumeric&#x60;, or &#x60;regexp&#x60; | [optional] 
**external_tracker_url** | **str** | URL of external issue tracker. | [optional] 

## Example

```python
from clientapi_forgejo.models.external_tracker import ExternalTracker

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalTracker from a JSON string
external_tracker_instance = ExternalTracker.from_json(json)
# print the JSON string representation of the object
print(ExternalTracker.to_json())

# convert the object into a dict
external_tracker_dict = external_tracker_instance.to_dict()
# create an instance of ExternalTracker from a dict
external_tracker_from_dict = ExternalTracker.from_dict(external_tracker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


