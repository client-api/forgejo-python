# TeamSearch200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Team]**](Team.md) |  | [optional] 
**ok** | **bool** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.team_search200_response import TeamSearch200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TeamSearch200Response from a JSON string
team_search200_response_instance = TeamSearch200Response.from_json(json)
# print the JSON string representation of the object
print TeamSearch200Response.to_json()

# convert the object into a dict
team_search200_response_dict = team_search200_response_instance.to_dict()
# create an instance of TeamSearch200Response from a dict
team_search200_response_form_dict = team_search200_response.from_dict(team_search200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


