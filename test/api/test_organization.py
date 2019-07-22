import unittest

import requests_mock

from grafana_api.grafana_face import GrafanaFace


class OrganizationTestCase(unittest.TestCase):
    def setUp(self):
        self.cli = GrafanaFace(
            ("admin", "admin"), host="localhost", url_path_prefix="", protocol="http"
        )

    @requests_mock.Mocker()
    def test_delete_snapshot_by_key(self, m):
        m.delete('http://localhost/api/orgs/1/users/2', json={"message": "User removed from organization"})
        annotation = self.cli.organizations.organization_user_delete(organization_id=1, user_id=2)
        self.assertEqual(annotation['message'], "User removed from organization")

    @requests_mock.Mocker()
    def test_organization_preference_get(self, m):
        m.get(
            "http://localhost/api/org/preferences",
            json={"theme":"","homeDashboardId":0,"timezone":""}
        )

        result = self.cli.organizations.organization_preference_get()
        self.assertEqual(result["homeDashboardId"], 0)
