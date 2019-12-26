from .base import Base


class Annotations(Base):
    def __init__(self, api):
        super(Annotations, self).__init__(api)
        self.api = api

    def get_annotation(
        self,
        time_from=None,
        time_to=None,
        alert_id=None,
        dashboard_id=None,
        panel_id=None,
        tags=None,
        limit=None,
    ):

        """
        :param time_from:
        :param time_to:
        :param alert_id:
        :param dashboard_id:
        :param panel_id:
        :param tags:
        :param limit:
        :return:
        """
        list_annotations_path = "/annotations"
        params = []

        if time_from:
            params.append("time_from=%s" % time_from)

        if time_to:
            params.append("time_to=%s" % time_to)

        if alert_id:
            params.append("alertId=%s" % alert_id)

        if dashboard_id:
            params.append("dashboardID=%s" % dashboard_id)

        if panel_id:
            params.append("panelId=%s" % panel_id)

        if tags:
            for tag in tags:
                params.append("tags=%s" % tag)

        if limit:
            params.append("limit=%s" % limit)

        list_annotations_path += "?"
        list_annotations_path += "&".join(params)

        r = self.api.GET(list_annotations_path)

        return r

    def add_annotation(
            self,
            time_from=None,
            time_to=None,
            is_region=True,
            tags=[],
            text=None,
    ):

        """
        :param time_from:
        :param time_to:
        :param is_region:
        :param tags:
        :param text:
        :return:
        """
        annotations_path = "/annotations"
        payload = {
            "time": time_from,
            "timeEnd": time_to,
            "isRegion": bool(is_region),
            "tags": tags,
            "text": text

        }

        r = self.api.POST(annotations_path, json=payload)

        return r

    def add_annotation_graphite(
            self,
            what=None,
            tags=[],
            when=None,
            data=None,
    ):
        """
        :param what:
        :param tags:
        :param when:
        :param data:
        :return:
        """

        annotations_path = "/annotations/graphite"
        payload = {
            "what": what,
            "tags": tags,
            "when": when,
            "data": data

        }

        r = self.api.POST(annotations_path, json=payload)

        return r

    def update_annotation(
            self,
            annotations_id,
            time_from=None,
            time_to=None,
            is_region=True,
            tags=[],
            text=None,
    ):
        """

        :param time_from:
        :param time_to:
        :param is_region:
        :param tags:
        :param text:
        :return:
        """
        annotations_path = "/annotations/{}".format(annotations_id)
        payload = {
            "time": time_from,
            "timeEnd": time_to,
            "isRegion": bool(is_region),
            "tags": tags,
            "text": text

        }

        r = self.api.PUT(annotations_path, json=payload)

        return r

    def partial_update_annotation(
            self,
            annotations_id,
            time_from=None,
            time_to=None,
            is_region=None,
            tags=[],
            text=None,
    ):
        """

        :param annotations_id:
        :param time_from:
        :param time_to:
        :param is_region:
        :param tags:
        :param text:
        :return:
        """
        annotations_path = "/annotations/{}".format(annotations_id)
        payload = {}
        if time_from:
            payload['time'] = time_from
        if time_to:
            payload['timeEnd'] = time_to
        if is_region:
            payload['isRegion'] = bool(is_region)
        if tags:
            payload['tags'] = tags
        if text:
            payload['text'] = text

        r = self.api.PATCH(annotations_path, json=payload)

        return r

    def delete_annotations_by_region_id(
            self,
            region_id=None
    ):

        """
        :param region_id:
        :return:
        """
        annotations_path = "/annotations/region/{}".format(region_id)
        r = self.api.DELETE(annotations_path)

        return r

    def delete_annotations_by_id(
            self,
            annotations_id=None
    ):

        """
        :param annotations_id:
        :return:
        """
        annotations_path = "/annotations/{}".format(annotations_id)
        r = self.api.DELETE(annotations_path)

        return r
