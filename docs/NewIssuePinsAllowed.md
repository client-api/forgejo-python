# NewIssuePinsAllowed

NewIssuePinsAllowed represents an API response that says if new Issue Pins are allowed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issues** | **bool** |  | [optional] 
**pull_requests** | **bool** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.new_issue_pins_allowed import NewIssuePinsAllowed

# TODO update the JSON string below
json = "{}"
# create an instance of NewIssuePinsAllowed from a JSON string
new_issue_pins_allowed_instance = NewIssuePinsAllowed.from_json(json)
# print the JSON string representation of the object
print(NewIssuePinsAllowed.to_json())

# convert the object into a dict
new_issue_pins_allowed_dict = new_issue_pins_allowed_instance.to_dict()
# create an instance of NewIssuePinsAllowed from a dict
new_issue_pins_allowed_from_dict = NewIssuePinsAllowed.from_dict(new_issue_pins_allowed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


