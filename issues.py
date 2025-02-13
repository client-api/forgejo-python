import time
#import pdb
import json
import os
import clientapi_forgejo
from clientapi_forgejo.models.timeline_comment import TimelineComment
from clientapi_forgejo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = clientapi_forgejo.Configuration(
    host = "https://codeberg.org/api/v1"
)

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]


# Configure API key authorization: AccessToken
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'
from datetime import date, datetime

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))

# Enter a context with an instance of the API client
with clientapi_forgejo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clientapi_forgejo.IssueApi(api_client)
    owner = 'introspector' # str | owner of the repo
    repo = 'SOLFUNMEME' # str | name of the repo
    limit = 100 # int | page size of results (optional)
    page = 0
    results = 1
    tickets = []
    while results>0:
        api_response = api_instance.issue_list_issues(owner, repo,  page=page, limit=limit)
        if api_response:
            for issue in api_response:
                comments = []            
                parent = issue.to_json()
                clean_data = json.loads(parent)
                detail_api_response = api_instance.issue_get_comments(owner, repo, index=issue.number,
                                                                      #page=detail_page,
                                                                      #limit=limit
                                                                      )
                for c in detail_api_response:
                    data = json.loads(c.to_json())
                    comments.append(data)
            clean_data['details'] = comments
            print(json.dumps(clean_data,default=json_serial,sort_keys=True))                            
        page = page + 1

