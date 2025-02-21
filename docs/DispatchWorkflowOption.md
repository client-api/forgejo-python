# DispatchWorkflowOption

DispatchWorkflowOption options when dispatching a workflow

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inputs** | **Dict[str, str]** | Input keys and values configured in the workflow file. | [optional] 
**ref** | **str** | Git reference for the workflow | 

## Example

```python
from clientapi_forgejo.models.dispatch_workflow_option import DispatchWorkflowOption

# TODO update the JSON string below
json = "{}"
# create an instance of DispatchWorkflowOption from a JSON string
dispatch_workflow_option_instance = DispatchWorkflowOption.from_json(json)
# print the JSON string representation of the object
print(DispatchWorkflowOption.to_json())

# convert the object into a dict
dispatch_workflow_option_dict = dispatch_workflow_option_instance.to_dict()
# create an instance of DispatchWorkflowOption from a dict
dispatch_workflow_option_from_dict = DispatchWorkflowOption.from_dict(dispatch_workflow_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


