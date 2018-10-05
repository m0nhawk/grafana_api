from .base import Base


class Dashboard(Base):
    def __init__(self, api):
        super().__init__(api)
        self.api = api
        self.path = '/users'

    def get_dashboard(self, dashboard_uid):
        get_dashboard_path = '/dashboards/uid/%s' % (dashboard_uid)
        r = self.api.GET(get_dashboard_path)
        return r

    def update_dashboard(self, dashboard):
        """

        :param dashboard:
        :return:
        """
        put_dashboard_path = '/dashboards/db'
        r = self.api.POST(put_dashboard_path, json=dashboard)
        return r

    def delete_dashboard(self, dashboard_uid):
        delete_dashboard_path = '/dashboards/uid/%s' % (dashboard_uid)
        r = self.api.DELETE(delete_dashboard_path)
        return r

    def get_home_dashboard(self):
        """

        :return:
        """
        get_home_dashboard_path = '/dashboards/home'
        r = self.api.GET(get_home_dashboard_path)
        return r

    def get_dashboards_tags(self):
        """

        :return:
        """
        get_dashboards_tags_path = '/dashboards/tags'
        r = self.api.GET(get_dashboards_tags_path)
        return r

    def get_dashboard_permissions(self, dashboardId):
        """
        Gets all existing permissions for the dashboard with the given dashboardId.

        :param dashboardId:
        """
        return self.api.GET('/dashboards/id/%s/permissions' % dashboardId)

    def update_dashboard_permissions(self, dashboardId, items):
        """
        Updates permissions for a dashboard.

        This operation will remove existing permissions if they’re not included in the request.

        :param dashboardId: Dashboard id
        """
        # TODO really relevant to return something?
        return self.api.POST('/dashboards/id/%s/permissions' % dashboardId, json=dict(items=items))
