import unittest

import requests_mock

from grafana_api.grafana_face import GrafanaFace
from grafana_api.grafana_api import GrafanaBadInputError


class AlertingTestCase(unittest.TestCase):
    def setUp(self):
        self.cli = GrafanaFace(
            ("admin", "admin"), host="localhost", url_path_prefix="", protocol="http"
        )

    # acutally idk how to write appropriate unit test