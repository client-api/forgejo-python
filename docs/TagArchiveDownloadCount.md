# TagArchiveDownloadCount

TagArchiveDownloadCount counts how many times a archive was downloaded

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tar_gz** | **int** |  | [optional] 
**zip** | **int** |  | [optional] 

## Example

```python
from clientapi_forgejo.models.tag_archive_download_count import TagArchiveDownloadCount

# TODO update the JSON string below
json = "{}"
# create an instance of TagArchiveDownloadCount from a JSON string
tag_archive_download_count_instance = TagArchiveDownloadCount.from_json(json)
# print the JSON string representation of the object
print(TagArchiveDownloadCount.to_json())

# convert the object into a dict
tag_archive_download_count_dict = tag_archive_download_count_instance.to_dict()
# create an instance of TagArchiveDownloadCount from a dict
tag_archive_download_count_from_dict = TagArchiveDownloadCount.from_dict(tag_archive_download_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


