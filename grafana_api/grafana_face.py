from .grafana_api import GrafanaAPI
from .api import Base


class GrafanaFace:
    def __init__(self, auth, host="localhost", port=None, url_path_prefix="", protocol="http", verify=True):
        self.api = GrafanaAPI(auth, host=host, port=port, url_path_prefix=url_path_prefix, protocol=protocol, verify=verify)

    def __getattr__(self, item):
        for cls in Base.__subclasses__():
            if cls.__name__.lower() == item:
                return cls(api=self.api)
        return
