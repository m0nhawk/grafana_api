import json
from .grafana_api import GrafanaAPI


class GrafanaFace:
    def __init__(self, auth, host="localhost", port=None, url_path_prefix="", protocol="http"):
        self.api = GrafanaAPI(auth, host=host, port=port, url_path_prefix=url_path_prefix, protocol=protocol)

    def get_grafana_settings(self):
        """

        :return:
        """
        get_settings_path = '/admin/settings'
        r = self.api.GET(get_settings_path)
        return r

    def get_grafana_stats(self):
        """

        :return:
        """
        get_stats_path = '/admin/stats'
        r = self.api.GET(get_stats_path)
        return r

    def create_user(self, user):
        """

        :param user:
        :return:
        """
        create_user_path = '/admin/users'
        r = self.api.POST(create_user_path, json=user)
        return r

    def change_user_password(self, user_id, password):
        """

        :param user_id:
        :param password:
        :return:
        """
        change_user_password_path = '/admin/users/%s/password' % (user_id)
        r = self.api.PUT(change_user_password_path, json={'password': password})
        return r

    def change_user_permissions(self, user_id, is_grafana_admin):
        """

        :param user_id:
        :param is_grafana_admin:
        :return:
        """
        change_user_permissions = '/api/admin/users/%s/permissions' % (user_id)
        r = self.api.PUT(change_user_permissions, json={'isGrafanaAdmin': is_grafana_admin})
        return r

    def delete_user(self, user_id):
        """

        :param user_id:
        :return:
        """
        delete_user_path = '/admin/users/%s' % (user_id)
        r = self.api.DELETE(delete_user_path)
        return r

    def search_users(self, query=None):
        """

        :return:
        """
        list_of_users = []
        users_on_page = None
        page = 1

        while users_on_page != []:
            if query:
                # TODO: escape the query
                show_users_path = '/users?perpage=10&page=%s&query=%s' % (page, query)
            else:
                show_users_path = '/users?perpage=10&page=%s' % (page)
            users_on_page = self.api.GET(show_users_path)
            list_of_users += users_on_page
            page += 1

        return list_of_users

    def get_user(self, user_id):
        """

        :param user_id:
        :return:
        """
        get_user_path = '/users/%s' % (user_id)
        r = self.api.GET(get_user_path)
        return r

    def find_user(self, loginOrEmail):
        """

        :param loginOrEmail:
        :return:
        """
        search_user_path = '/users/lookup?loginOrEmail=%s' % (loginOrEmail)
        r = self.api.GET(search_user_path)
        if 'id' in r:
            return r['id']
        return -1

    def update_user(self, user_id, user):
        """

        :param user_id:
        :param user:
        :return:
        """
        update_user_path = '/users/%s' % (user_id)
        r = self.api.PUT(update_user_path, json=user)
        return r

    def get_user_organisations(self, user_id):
        """

        :param user_id:
        :return:
        """
        get_user_organisations_path = '/users/%s/orgs' % (user_id)
        r = self.api.GET(get_user_organisations_path)
        return r

    def get_actual_user(self):
        """

        :return:
        """
        get_actual_user_path = '/user'
        r = self.api.GET(get_actual_user_path)
        return r

    def change_actual_user_password(self, old_password, new_password):
        """

        :param old_password:
        :param new_password:
        :return:
        """
        change_actual_user_password_path = '/user/password'
        change_actual_user_password_json = {
            "oldPassword": old_password,
            "newPassword": new_password,
            "confirmNew": new_password
        }
        r = self.api.PUT(change_actual_user_password_path, json=change_actual_user_password_json)
        return r

    def switch_user_organisation(self, user_id, organisation_id):
        """

        :param user_id:
        :param organisation_id:
        :return:
        """
        switch_user_organisation_path = '/users/%s/using/%s' % (user_id, organisation_id)
        r = self.api.POST(switch_user_organisation_path)
        return r

    def switch_actual_user_organisation(self, organisation_id):
        """

        :param organisation_id:
        :return:
        """
        switch_actual_user_organisation_path = '/user/using/%s' % (organisation_id)
        r = self.api.POST(switch_actual_user_organisation_path)
        return r

    def get_actual_user_organisations(self):
        """

        :return:
        """
        get_actual_user_organisations_path = '/user/orgs'
        r = self.api.GET(get_actual_user_organisations_path)
        return r

    def star_actual_user_dashboard(self, dashboard_id):
        """

        :param dashboard_id:
        :return:
        """
        star_dashboard = '/user/stars/dashboard/%s' % (dashboard_id)
        r = self.api.POST(star_dashboard)
        return r

    def unstar_actual_user_dashboard(self, dashboard_id):
        """

        :param dashboard_id:
        :return:
        """
        unstar_dashboard = '/user/stars/dashboard/%s' % (dashboard_id)
        r = self.api.DELETE(unstar_dashboard)
        return r

    def find_organisation(self, org_name):
        get_org_path = '/orgs/name/%s' % (org_name)
        r = self.api.GET(get_org_path)
        if 'id' in r:
            return r['id']
        return -1

    def create_organisation(self, organisation):
        create_orgs_path = '/orgs'
        r = self.api.POST(create_orgs_path, json={'name': organisation['name']})
        organisation_id = r['orgId']
        return organisation_id, r

    def update_organisation(self, organisation_id, organisation):
        update_org_path = '/orgs/%s' % (organisation_id)
        r = self.api.PUT(update_org_path, json=organisation)
        return organisation_id, r

    def delete_organisation(self, organisation_id):
        delete_org_path = '/orgs/%s' % (organisation_id)
        r = self.api.DELETE(delete_org_path)
        return r

    def list_organisation(self):
        search_org_path = '/orgs'
        r = self.api.GET(search_org_path)
        return r

    def switch_organisation(self, organisation_id):
        switch_user_organisation = '/user/using/%s' % (organisation_id)
        r = self.api.POST(switch_user_organisation)
        return r

    def organisation_user_list(self, organisation_id):
        users_in_org = '/orgs/%s/users' % (organisation_id)
        r = self.api.GET(users_in_org)
        return r

    def organisation_user_add(self, organisation_id, user):
        add_user_path = '/orgs/%s/users' % (organisation_id)
        r = self.api.POST(add_user_path, json=user)
        return r

    def organisation_user_update(self, organisation_id, user_id, user_role):
        patch_user = '/orgs/%s/users/%s' % (organisation_id, user_id)
        r = self.api.PATCH(patch_user, json={'role': user_role})
        return r

    def organisation_user_delete(self, organisation_id, user_id):
        delete_user = '/orgs/%s/users/%s' % (organisation_id, user_id)
        r = self.api.DELETE(delete_user)
        return r

    def organisation_preference_update(self, theme='', home_dashboard_id=0, timezone='utc'):
        update_preference = '/org/preferences'
        r = self.api.PUT(update_preference, json={
            "theme": theme,
            "homeDashboardId": home_dashboard_id,
            "timezone": timezone
        })
        return r

    def find_datasource(self, datasource_name):
        get_datasource_path = '/datasources/name/%s' % (datasource_name)
        r = self.api.GET(get_datasource_path)
        if 'id' in r:
            return r['id']
        return -1

    def get_datasource(self, datasource_id):
        get_datasource_path = '/datasources/%s' % (datasource_id)
        r = self.api.GET(get_datasource_path)
        return r

    def create_datasource(self, datasource):
        create_datasources_path = '/datasources'
        r = self.api.POST(create_datasources_path, json=datasource)
        return r

    def update_datasource(self, datasource_id, datasource):
        update_datasource = '/datasources/%s' % (datasource_id)
        r = self.api.PUT(update_datasource, json=datasource)
        return r

    def list_datasource(self):
        list_datasource = '/datasources'
        r = self.api.GET(list_datasource)
        return r

    def delete_datasource(self, name):
        delete_datasource = '/datasources/name/%s' % (name)
        r = self.api.DELETE(delete_datasource)
        return r

    def list_dashboard(self):
        list_dashboard_path = '/search/'
        r = self.api.GET(list_dashboard_path)
        return r

    def get_dashboard(self, dashboard_slug):
        get_dashboard_path = '/dashboards/%s' % (dashboard_slug)
        r = self.api.GET(get_dashboard_path)
        return r

    def update_dashboard(self, dashboard):
        put_dashboard_path = '/dashboards/db'
        r = self.api.POST(put_dashboard_path, json=dashboard)
        return r

    def delete_dashboard(self, dashboard_slug):
        delete_dashboard_path = '/dashboards/%s' % (dashboard_slug)
        r = self.api.DELETE(delete_dashboard_path)
        return r

    def get_api_keys(self):
        get_api_keys_path = '/auth/keys'
        r = self.api.GET(get_api_keys_path)
        return r

    def create_api_key(self, json):
        create_api_key_path = '/auth/keys'
        r = self.api.POST(create_api_key_path, json=json)
        return r

    def delete_api_key(self, id):
        delete_api_key_path = '/auth/keys/%s' % (id)
        r = self.api.DELETE(delete_api_key_path)
        return r
