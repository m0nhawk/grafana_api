from .base import Base


class Alerts(Base):
    def __init__(self, api):
        super(Alerts, self).__init__(api)
        self.api = api

    def list_alerts(self,
                    dashboardId=None,
                    panelId=None,
                    query=None,
                    state=None,
                    limit=None,
                    folderId=None,
                    dashboardQuery=None,
                    dashboardTag=None):
        """

        :param dashboardId:
        :param panelId:
        :param query:
        :param state:
        :param limit:
        :param folderId:
        :param dashboardQuery:
        :param dashboardTag:
        :return:
        """
        search_alerts_path = "/alerts"
        params = []

        if dashboardId:
            params.append("dashboardId=%s" % dashboardId)

        if panelId:
            params.append("panelId=%s" % panelId)

        if query:
            params.append("query=%s" % query)

        if state:
            params.append("state=%s" % state)

        if limit:
            params.append("limit=%s" % limit)

        if folderId:
            params.append("folderId=%s" % folderId)

        if dashboardQuery:
            params.append("dashboardQuery=%s" % dashboardQuery)

        if dashboardTag:
            params.append("dashboardTag=%s" % dashboardTag)

        search_alerts_path += "?"
        search_alerts_path +=  "&".join(params)

        print(search_alerts_path)
        r = self.api.GET(search_alerts_path)
        print(r)
        return r

    def get_alert(self, alert_id):
        """

        :param alert_id:
        :return:
        """
        get_alert_path = "/alerts/%s" % alert_id
        r = self.api.GET(get_alert_path)
        return r

    def pause_alert(self, alert_id, isPaused):
        """

        :param isPaused:
        :param alert_id:
        :return:
        """
        json_data = dict(paused=isPaused)
        pause_alert_path = "/alerts/%s/pause" % alert_id
        r = self.api.POST(pause_alert_path, json=json_data)
        return r