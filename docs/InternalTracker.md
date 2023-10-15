# InternalTracker

InternalTracker represents settings for internal tracker

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_only_contributors_to_track_time** | **bool** | Let only contributors track time (Built-in issue tracker) | [optional] 
**enable_issue_dependencies** | **bool** | Enable dependencies for issues and pull requests (Built-in issue tracker) | [optional] 
**enable_time_tracker** | **bool** | Enable time tracking (Built-in issue tracker) | [optional] 

## Example

```python
from clientapi_forgejo.models.internal_tracker import InternalTracker

# TODO update the JSON string below
json = "{}"
# create an instance of InternalTracker from a JSON string
internal_tracker_instance = InternalTracker.from_json(json)
# print the JSON string representation of the object
print InternalTracker.to_json()

# convert the object into a dict
internal_tracker_dict = internal_tracker_instance.to_dict()
# create an instance of InternalTracker from a dict
internal_tracker_form_dict = internal_tracker.from_dict(internal_tracker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


