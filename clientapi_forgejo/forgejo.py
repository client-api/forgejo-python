import clientapi_forgejo
from clientapi_forgejo import ActivitypubApi, AdminApi, IssueApi, MiscellaneousApi, NotificationApi, OrganizationApi, PackageApi, RepositoryApi, SettingsApi, UserApi

class Forgejo:

    def __init__(self, host: str, api_key: str):
        self.configuration = clientapi_forgejo.Configuration(
            host=host,
        )
        self.configuration.api_key['Token'] = api_key
        self.validate()
    
    def validate(self):
        if not self.configuration.api_key:
            raise Exception("The Forgejo API key is not set.")

    def ActivitypubApi(self) -> ActivitypubApi:
        with clientapi_forgejo.ApiClient(self.configuration) as api_client:
            return clientapi_forgejo.ActivitypubApi(api_client)

    def AdminApi(self) -> AdminApi:
        with clientapi_forgejo.ApiClient(self.configuration) as api_client:
            return clientapi_forgejo.AdminApi(api_client)

    def IssueApi(self) -> IssueApi:
        with clientapi_forgejo.ApiClient(self.configuration) as api_client:
            return clientapi_forgejo.IssueApi(api_client)

    def MiscellaneousApi(self) -> MiscellaneousApi:
        with clientapi_forgejo.ApiClient(self.configuration) as api_client:
            return clientapi_forgejo.MiscellaneousApi(api_client)

    def NotificationApi(self) -> NotificationApi:
        with clientapi_forgejo.ApiClient(self.configuration) as api_client:
            return clientapi_forgejo.NotificationApi(api_client)

    def OrganizationApi(self) -> OrganizationApi:
        with clientapi_forgejo.ApiClient(self.configuration) as api_client:
            return clientapi_forgejo.OrganizationApi(api_client)

    def PackageApi(self) -> PackageApi:
        with clientapi_forgejo.ApiClient(self.configuration) as api_client:
            return clientapi_forgejo.PackageApi(api_client)

    def RepositoryApi(self) -> RepositoryApi:
        with clientapi_forgejo.ApiClient(self.configuration) as api_client:
            return clientapi_forgejo.RepositoryApi(api_client)

    def SettingsApi(self) -> SettingsApi:
        with clientapi_forgejo.ApiClient(self.configuration) as api_client:
            return clientapi_forgejo.SettingsApi(api_client)

    def UserApi(self) -> UserApi:
        with clientapi_forgejo.ApiClient(self.configuration) as api_client:
            return clientapi_forgejo.UserApi(api_client)