import unittest
from unittest.mock import patch, Mock
import requests

from grafana_api.grafana_face import GrafanaFace
from grafana_api.grafana_api import TokenAuth


class TestGrafanaAPI(unittest.TestCase):
    @patch('grafana_api.grafana_api.GrafanaAPI.__getattr__')
    def test_grafana_api(self, mock_get):
        mock_get.return_value = Mock()
        mock_get.return_value.return_value = """{
  "email": "user@mygraf.com",
  "name": "admin",
  "login": "admin",
  "theme": "light",
  "orgId": 1,
  "isGrafanaAdmin": true
}"""
        cli = GrafanaFace(('admin', 'admin'), host='localhost',
                          url_path_prefix='', protocol='https')
        cli.users.find_user('test@test.com')

    def test_grafana_api_basic_auth(self):
        cli = GrafanaFace(('admin', 'admin'), host='localhost',
                          url_path_prefix='', protocol='https')
        self.assertTrue(isinstance(cli.api.auth, requests.auth.HTTPBasicAuth))

    def test_grafana_api_token_auth(self):
        cli = GrafanaFace('alongtoken012345etc', host='localhost',
                          url_path_prefix='', protocol='https')
        self.assertTrue(isinstance(cli.api.auth, TokenAuth))


if __name__ == '__main__':
    unittest.main()
