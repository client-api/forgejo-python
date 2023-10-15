# clientapi_forgejo.PackageApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_package**](PackageApi.md#delete_package) | **DELETE** /packages/{owner}/{type}/{name}/{version} | Delete a package
[**get_package**](PackageApi.md#get_package) | **GET** /packages/{owner}/{type}/{name}/{version} | Gets a package
[**list_package_files**](PackageApi.md#list_package_files) | **GET** /packages/{owner}/{type}/{name}/{version}/files | Gets all files of a package
[**list_packages**](PackageApi.md#list_packages) | **GET** /packages/{owner} | Gets all packages of an owner


# **delete_package**
> delete_package(owner, type, name, version)

Delete a package

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):
```python
import time
import os
import clientapi_forgejo
from clientapi_forgejo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = clientapi_forgejo.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = clientapi_forgejo.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with clientapi_forgejo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clientapi_forgejo.PackageApi(api_client)
    owner = 'owner_example' # str | owner of the package
    type = 'type_example' # str | type of the package
    name = 'name_example' # str | name of the package
    version = 'version_example' # str | version of the package

    try:
        # Delete a package
        api_instance.delete_package(owner, type, name, version)
    except Exception as e:
        print("Exception when calling PackageApi->delete_package: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the package | 
 **type** | **str**| type of the package | 
 **name** | **str**| name of the package | 
 **version** | **str**| version of the package | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_package**
> Package get_package(owner, type, name, version)

Gets a package

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):
```python
import time
import os
import clientapi_forgejo
from clientapi_forgejo.models.package import Package
from clientapi_forgejo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = clientapi_forgejo.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = clientapi_forgejo.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with clientapi_forgejo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clientapi_forgejo.PackageApi(api_client)
    owner = 'owner_example' # str | owner of the package
    type = 'type_example' # str | type of the package
    name = 'name_example' # str | name of the package
    version = 'version_example' # str | version of the package

    try:
        # Gets a package
        api_response = api_instance.get_package(owner, type, name, version)
        print("The response of PackageApi->get_package:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PackageApi->get_package: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the package | 
 **type** | **str**| type of the package | 
 **name** | **str**| name of the package | 
 **version** | **str**| version of the package | 

### Return type

[**Package**](Package.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Package |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_package_files**
> List[PackageFile] list_package_files(owner, type, name, version)

Gets all files of a package

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):
```python
import time
import os
import clientapi_forgejo
from clientapi_forgejo.models.package_file import PackageFile
from clientapi_forgejo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = clientapi_forgejo.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = clientapi_forgejo.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with clientapi_forgejo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clientapi_forgejo.PackageApi(api_client)
    owner = 'owner_example' # str | owner of the package
    type = 'type_example' # str | type of the package
    name = 'name_example' # str | name of the package
    version = 'version_example' # str | version of the package

    try:
        # Gets all files of a package
        api_response = api_instance.list_package_files(owner, type, name, version)
        print("The response of PackageApi->list_package_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PackageApi->list_package_files: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the package | 
 **type** | **str**| type of the package | 
 **name** | **str**| name of the package | 
 **version** | **str**| version of the package | 

### Return type

[**List[PackageFile]**](PackageFile.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PackageFileList |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_packages**
> List[Package] list_packages(owner, page=page, limit=limit, type=type, q=q)

Gets all packages of an owner

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):
```python
import time
import os
import clientapi_forgejo
from clientapi_forgejo.models.package import Package
from clientapi_forgejo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = clientapi_forgejo.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = clientapi_forgejo.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with clientapi_forgejo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clientapi_forgejo.PackageApi(api_client)
    owner = 'owner_example' # str | owner of the packages
    page = 56 # int | page number of results to return (1-based) (optional)
    limit = 56 # int | page size of results (optional)
    type = 'type_example' # str | package type filter (optional)
    q = 'q_example' # str | name filter (optional)

    try:
        # Gets all packages of an owner
        api_response = api_instance.list_packages(owner, page=page, limit=limit, type=type, q=q)
        print("The response of PackageApi->list_packages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PackageApi->list_packages: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the packages | 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 
 **type** | **str**| package type filter | [optional] 
 **q** | **str**| name filter | [optional] 

### Return type

[**List[Package]**](Package.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PackageList |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

