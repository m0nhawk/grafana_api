import unittest
from unittest.mock import patch, Mock

from grafana_api.grafana_face import GrafanaFace


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
        cli = GrafanaFace(('admin', 'admin'), host='localhost', url_path_prefix='', protocol='https')
        cli.find_user('test@test.com')


if __name__ == '__main__':
    unittest.main()
