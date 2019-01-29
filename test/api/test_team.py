import unittest
import requests_mock
from grafana_api.grafana_face import GrafanaFace

class TeamsTestCase(unittest.TestCase):

    def setUp(self):
        self.cli = GrafanaFace(('admin', 'admin'), host='localhost',
                url_path_prefix='', protocol='http')

    @requests_mock.Mocker()
    def test_get_team(self, m):
        m.get('http://localhost/api/teams/1', json=
        {"id": 1,
            "orgId": 1,
            "name": "MyTestTeam",
            "email": "",
            "created": "2017-12-15T10:40:45+01:00",
            "updated": "2017-12-15T10:40:45+01:00"
        })
        team = self.cli.teams.get_team('1')
        self.assertEqual(team["name"], "MyTestTeam")

    @requests_mock.Mocker()
    def test_add_team(self, m):
        m.post('http://localhost/api/teams', json=
        {
            "message":"Team created","teamId":2
        })
        team = {
                "name": "MySecondTestTeam",
                "email": "email@test.com"
                }
        new_team = self.cli.teams.add_team(team)
        self.assertEqual(new_team["teamId"], 2)

    @requests_mock.Mocker()
    def test_update_team(self, m):
        m.put('http://localhost/api/teams/3', json=
        {
            "message":"Team updated"
        })
        team = {
                "name": "MyThirdTestTeam",
                "email": "email@test.com"
                }
        response = self.cli.teams.update_team(3, team)
        self.assertEqual(response["message"], "Team updated")

    @requests_mock.Mocker()
    def test_delete_team(self, m):
        m.delete('http://localhost/api/teams/3', json=
        {
            "message":"Team deleted"
        })
        response = self.cli.teams.delete_team(3)
        self.assertEqual(response, True)
