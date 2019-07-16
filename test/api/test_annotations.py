import unittest

import requests_mock

from grafana_api.grafana_face import GrafanaFace


class AnnotationsTestCase(unittest.TestCase):
    def setUp(self):
        self.cli = GrafanaFace(
            ("admin", "admin"), host="localhost", url_path_prefix="", protocol="http"
        )

    @requests_mock.Mocker()
    def test_annotations(self, m):
        m.get(
            "http://localhost/api/annotations?time_from=1563183710618&time_to=1563185212275"
            "&alertId=11&dashboardID=111&panelId=22&tags=tags-test&limit=1",
            json=[
                {
                    "id": 80,
                    "alertId": 11,
                    "alertName": "",
                    "dashboardId": 111,
                    "panelId": 22,
                    "userId": 0,
                    "newState": "",
                    "prevState": "",
                    "created": 1563280160455,
                    "updated": 1563280160455,
                    "time": 1563156456006,
                    "text": "Annotation Description",
                    "regionId": 79,
                    "tags": [
                        "tags-test"
                    ],
                    "login": "",
                    "email": "",
                    "avatarUrl": "",
                    "data": {}
                },
            ]
        )
        annotations = self.cli.annotations.get_annotation(time_from=1563183710618, time_to=1563185212275, alert_id=11,
                                                          dashboard_id=111, panel_id=22, tags="tags-test", limit=1)
        self.assertEqual(annotations[0]["text"], "Annotation Description")
        self.assertEqual(annotations[0]["alertId"], 11)
        self.assertEqual(annotations[0]["dashboardId"], 111)
        self.assertEqual(annotations[0]["panelId"], 22)
        self.assertEqual(annotations[0]["tags"][0], "tags-test")

        self.assertEqual(len(annotations), 1)

    @requests_mock.Mocker()
    def test_delete_annotations_by_region_id(self, m):
        m.delete("http://localhost/api/annotations/region/99", json={"message": "Annotation region deleted"})
        response = self.cli.annotations.delete_annotations_by_region_id(99)
        self.assertEqual(response['message'], "Annotation region deleted")

    @requests_mock.Mocker()
    def delete_annotations_by_id(self, m):
        m.delete("http://localhost/api/annotations/99", json={"message": "Annotation deleted"})
        response = self.cli.annotations.delete_annotations_by_id(99)
        self.assertEqual(response['message'], "Annotation region deleted")

    @requests_mock.Mocker()
    def test_add_annotation(self, m):
        m.post(
            "http://localhost/api/annotations",
            json={"endId": 80, "id": 79, "message": "Annotation added"},
        )
        annotation = self.cli.annotations.add_annotation(time_from=1563183710618, time_to=1563185212275
                                                         , is_region=True, tags="tags-test", text="Test")
        self.assertEqual(annotation["endId"], 80)
        self.assertEqual(annotation["id"], 79)
        self.assertEqual(annotation["message"], "Annotation added")

    @requests_mock.Mocker()
    def test_update_annotation(self, m):
        m.put(
            "http://localhost/api/annotations",
            json={"endId": 80, "id": 79, "message": "Annotation updated"},
        )
        annotation = self.cli.annotations.update_annotation(time_from=1563183710618, time_to=1563185212275
                                                            , is_region=True, tags="tags-test", text="Test")
        self.assertEqual(annotation["endId"], 80)
        self.assertEqual(annotation["id"], 79)
        self.assertEqual(annotation["message"], "Annotation updated")

    @requests_mock.Mocker()
    def test_add_annotation(self, m):
        m.post(
            "http://localhost/api/annotations/graphite",
            json={"message": "Graphite annotation added", "id": 1},
        )
        annotation = self.cli.annotations.add_annotation_graphite(what="Event - deploy", tags="deploy, production",
                                                                  when=1467844481, data="Data")

        self.assertEqual(annotation["id"], 1)
        self.assertEqual(annotation["message"], "Graphite annotation added")
