# CreateStatusOption

CreateStatusOption holds the information needed to create a new CommitStatus for a Commit

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**state** | **str** | CommitStatusState holds the state of a CommitStatus It can be \&quot;pending\&quot;, \&quot;success\&quot;, \&quot;error\&quot;, \&quot;failure\&quot;, and \&quot;warning\&quot; | [optional] 
**target_url** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.create_status_option import CreateStatusOption

# TODO update the JSON string below
json = "{}"
# create an instance of CreateStatusOption from a JSON string
create_status_option_instance = CreateStatusOption.from_json(json)
# print the JSON string representation of the object
print CreateStatusOption.to_json()

# convert the object into a dict
create_status_option_dict = create_status_option_instance.to_dict()
# create an instance of CreateStatusOption from a dict
create_status_option_form_dict = create_status_option.from_dict(create_status_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


