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
        """

        :param org_name:
        :return:
        """
        get_org_path = '/orgs/name/%s' % (org_name)
        r = self.api.GET(get_org_path)
        if 'id' in r:
            return r['id']
        return -1

    def get_current_organisation(self):
        """

        :return:
        """
        get_current_organisation_path = '/org'
        r = self.api.GET(get_current_organisation_path)
        return r

    def create_organisation(self, organisation):
        """

        :param organisation:
        :return:
        """
        create_orgs_path = '/orgs'
        r = self.api.POST(create_orgs_path, json={'name': organisation['name']})
        organisation_id = r['orgId']
        return organisation_id, r

    def update_current_organisation(self, organisation):
        """

        :param organisation:
        :return:
        """
        update_current_organisation_path = '/org'
        r = self.api.PUT(update_current_organisation_path, json=organisation)
        return r

    def get_current_organisation_users(self):
        """

        :return:
        """
        get_current_organisation_users_path = '/org/users'
        r = self.api.GET(get_current_organisation_users_path)
        return r

    def add_user_current_organisation(self, user):
        """

        :param user:
        :return:
        """
        add_user_current_organisation_path = '/org/users'
        r = self.api.POST(add_user_current_organisation_path, json=user)
        return r

    def update_user_current_organisation(self, user_id, user):
        """

        :param user_id:
        :param user:
        :return:
        """
        update_user_current_organisation_path = '/org/users/%s' % (user_id)
        r = self.api.PATCH(update_user_current_organisation_path, json=user)
        return r

    def delete_user_current_organisation(self, user_id):
        """

        :param user_id:
        :return:
        """
        delete_user_current_organisation_path = '/org/users/%s' % (user_id)
        r = self.api.DELETE(delete_user_current_organisation_path)
        return r

    def update_organisation(self, organisation_id, organisation):
        """

        :param organisation_id:
        :param organisation:
        :return:
        """
        update_org_path = '/orgs/%s' % (organisation_id)
        r = self.api.PUT(update_org_path, json=organisation)
        return organisation_id, r

    def delete_organisation(self, organisation_id):
        """

        :param organisation_id:
        :return:
        """
        delete_org_path = '/orgs/%s' % (organisation_id)
        r = self.api.DELETE(delete_org_path)
        return r

    def list_organisation(self):
        """

        :return:
        """
        search_org_path = '/orgs'
        r = self.api.GET(search_org_path)
        return r

    def switch_organisation(self, organisation_id):
        """

        :param organisation_id:
        :return:
        """
        switch_user_organisation = '/user/using/%s' % (organisation_id)
        r = self.api.POST(switch_user_organisation)
        return r

    def organisation_user_list(self, organisation_id):
        """

        :param organisation_id:
        :return:
        """
        users_in_org = '/orgs/%s/users' % (organisation_id)
        r = self.api.GET(users_in_org)
        return r

    def organisation_user_add(self, organisation_id, user):
        """

        :param organisation_id:
        :param user:
        :return:
        """
        add_user_path = '/orgs/%s/users' % (organisation_id)
        r = self.api.POST(add_user_path, json=user)
        return r

    def organisation_user_update(self, organisation_id, user_id, user_role):
        """

        :param organisation_id:
        :param user_id:
        :param user_role:
        :return:
        """
        patch_user = '/orgs/%s/users/%s' % (organisation_id, user_id)
        r = self.api.PATCH(patch_user, json={'role': user_role})
        return r

    def organisation_user_delete(self, organisation_id, user_id):
        """

        :param organisation_id:
        :param user_id:
        :return:
        """
        delete_user = '/orgs/%s/users/%s' % (organisation_id, user_id)
        r = self.api.DELETE(delete_user)
        return r

    def organisation_preference_update(self, theme='', home_dashboard_id=0, timezone='utc'):
        """

        :param theme:
        :param home_dashboard_id:
        :param timezone:
        :return:
        """
        update_preference = '/org/preferences'
        r = self.api.PUT(update_preference, json={
            "theme": theme,
            "homeDashboardId": home_dashboard_id,
            "timezone": timezone
        })
        return r

    def find_datasource(self, datasource_name):
        """

        :param datasource_name:
        :return:
        """
        get_datasource_path = '/datasources/name/%s' % (datasource_name)
        r = self.api.GET(get_datasource_path)
        if 'id' in r:
            return r['id']
        return -1

    def get_datasource_by_id(self, datasource_id):
        """

        :param datasource_id:
        :return:
        """
        get_datasource_path = '/datasources/%s' % (datasource_id)
        r = self.api.GET(get_datasource_path)
        return r

    def get_datasource_by_name(self, datasource_name):
        """

        :param datasource_name:
        :return:
        """
        get_datasource_path = '/datasources/name/%s' % (datasource_name)
        r = self.api.GET(get_datasource_path)
        return r

    def get_datasource_id_by_name(self, datasource_name):
        """

        :param datasource_name:
        :return:
        """
        get_datasource_path = '/datasources/id/%s' % (datasource_name)
        r = self.api.GET(get_datasource_path)
        return r

    def create_datasource(self, datasource):
        """

        :param datasource:
        :return:
        """
        create_datasources_path = '/datasources'
        r = self.api.POST(create_datasources_path, json=datasource)
        return r

    def update_datasource(self, datasource_id, datasource):
        """

        :param datasource_id:
        :param datasource:
        :return:
        """
        update_datasource = '/datasources/%s' % (datasource_id)
        r = self.api.PUT(update_datasource, json=datasource)
        return r

    def list_datasources(self):
        """

        :return:
        """
        list_datasources_path = '/datasources'
        r = self.api.GET(list_datasources_path)
        return r

    def delete_datasource_by_id(self, datasource_id):
        """

        :param datasource_id:
        :return:
        """
        delete_datasource = '/datasources/%s' % (datasource_id)
        r = self.api.DELETE(delete_datasource)
        return r

    def delete_datasource_by_name(self, datasource_name):
        """

        :param datasource_name:
        :return:
        """
        delete_datasource = '/datasources/name/%s' % (datasource_name)
        r = self.api.DELETE(delete_datasource)
        return r

    def list_dashboard(self, query=None, tag=None, starred=None, tagcloud=None):
        """

        :param query:
        :param tag:
        :param starred:
        :param tagcloud:
        :return:
        """
        list_dashboard_path = '/search?'
        params = []

        if query:
            params.append('query=%s' % (query))

        if tag:
            params.append('tag=%s' % (tag))

        if starred:
            params.append('starred=%s' % (starred))

        if tagcloud:
            params.append('tagcloud=%s' % (tagcloud))

        list_dashboard_path += '&'.join(params)

        r = self.api.GET(list_dashboard_path)
        return r

    def get_dashboard(self, dashboard_slug):
        """

        :param dashboard_slug:
        :return:
        """
        get_dashboard_path = '/dashboards/%s' % (dashboard_slug)
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

    def delete_dashboard(self, dashboard_slug):
        """

        :param dashboard_slug:
        :return:
        """
        delete_dashboard_path = '/dashboards/%s' % (dashboard_slug)
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

    def get_api_keys(self):
        """

        :return:
        """
        get_api_keys_path = '/auth/keys'
        r = self.api.GET(get_api_keys_path)
        return r

    def create_api_key(self, json_data):
        """

        :param json_data:
        :return:
        """
        create_api_key_path = '/auth/keys'
        r = self.api.POST(create_api_key_path, json=json_data)
        return r

    def delete_api_key(self, id):
        """

        :param id:
        :return:
        """
        delete_api_key_path = '/auth/keys/%s' % (id)
        r = self.api.DELETE(delete_api_key_path)
        return r

# Other section
    def get_frontend_settings(self):
        """

        :return:
        """
        get_frontend_settings_path = '/frontend/settings'
        r = self.api.GET(get_frontend_settings_path)
        return r

    def get_login_ping(self):
        """

        :return:
        """
        get_login_ping_path = '/login/ping'
        r = self.api.GET(get_login_ping_path)
        return r
