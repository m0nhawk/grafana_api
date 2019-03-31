import unittest
import sys

if (sys.version_info > (3, 0)):
    from unittest.mock import patch, Mock
else:
    from mock import patch, Mock

import requests

from grafana_api.grafana_face import GrafanaFace
from grafana_api.grafana_api import TokenAuth


class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data


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

    def test_grafana_api_no_verify(self):
        cli = GrafanaFace(('admin', 'admin'), host='localhost',
                          url_path_prefix='', protocol='https', verify=False)
        cli.api.s.get = Mock(name='get')
        cli.api.s.get.return_value = MockResponse({
  "email": "user@mygraf.com",
  "name": "admin",
  "login": "admin",
  "theme": "light",
  "orgId": 1,
  "isGrafanaAdmin": True}, 200)

        basicAuth = requests.auth.HTTPBasicAuth('admin', 'admin')
        cli.users.find_user('test@test.com')
        cli.api.s.get.assert_called_once_with('https://localhost/api/users/lookup?loginOrEmail=test@test.com', auth=basicAuth, headers=None, json=None, verify=False)

    def test_grafana_api_basic_auth(self):
        cli = GrafanaFace(('admin', 'admin'), host='localhost',
                          url_path_prefix='', protocol='https')
        self.assertTrue(isinstance(cli.api.auth, requests.auth.HTTPBasicAuth))

    def test_grafana_api_token_auth(self):
        cli = GrafanaFace('alongtoken012345etc', host='localhost',
                          url_path_prefix='', protocol='https')
        self.assertTrue(isinstance(cli.api.auth, TokenAuth))


if __name__ == '__main__':
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
