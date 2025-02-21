from pprint import pprint

from clientapi_forgejo.forgejo import Forgejo
from clientapi_forgejo.exceptions import UnauthorizedException

try:
    forgejo = Forgejo(host="https://<domain>/api/v1", api_key="<your_api_key>")
    repository = forgejo.RepositoryApi()
    result = repository.repo_search(q="Search...")
    pprint(result)
except UnauthorizedException as e:
    print(e)