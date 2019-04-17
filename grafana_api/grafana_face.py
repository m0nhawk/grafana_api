from .grafana_api import GrafanaAPI
from .api import (Admin, Dashboard, Datasource, Folder, Organization, Organizations, Search, User, Users)


class GrafanaFace:
    def __init__(self, auth, host="localhost", port=None, url_path_prefix="", protocol="http", verify=True):
        api = GrafanaAPI(auth, host=host, port=port, url_path_prefix=url_path_prefix, protocol=protocol, verify=verify)
        self.admin = Admin(api)
        self.dashboard = Dashboard(api)
        self.datasource = Datasource(api)
        self.folder = Folder(api)
        self.organization = Organization(api)
        self.organizations = Organizations(api)
        self.search = Search(api)
        self.user = User(api)
        self.users = Users(api)
