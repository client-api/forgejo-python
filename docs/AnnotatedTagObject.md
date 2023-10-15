# AnnotatedTagObject

AnnotatedTagObject contains meta information of the tag object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sha** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.annotated_tag_object import AnnotatedTagObject

# TODO update the JSON string below
json = "{}"
# create an instance of AnnotatedTagObject from a JSON string
annotated_tag_object_instance = AnnotatedTagObject.from_json(json)
# print the JSON string representation of the object
print AnnotatedTagObject.to_json()

# convert the object into a dict
annotated_tag_object_dict = annotated_tag_object_instance.to_dict()
# create an instance of AnnotatedTagObject from a dict
annotated_tag_object_form_dict = annotated_tag_object.from_dict(annotated_tag_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


