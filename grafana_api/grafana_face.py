import json
from .grafana_api import GrafanaAPI


class GrafanaFace:
    def __init__(self, auth, host="localhost", port=None, url_path_prefix="", protocol="http"):
        self.api = GrafanaAPI(auth, host=host, port=port, url_path_prefix=url_path_prefix, protocol=protocol)

    def get_grafana_settings(self):
        get_settings_path = '/admin/settings'
        r = self.api.GET(get_settings_path)
        return r

    def get_grafana_stats(self):
        get_stats_path = '/admin/stats'
        r = self.api.GET(get_stats_path)
        return r

    def create_user(self, user):
        create_user_path = '/admin/users'
        r = self.api.POST(create_user_path, json=user)
        return r

    def change_user_password(self, user_id, password):
        change_user_password_path = '/admin/users/%s/password' % (user_id)
        r = self.api.PUT(change_user_password_path, json={'password': password})
        return r

    def change_user_permissions(self, user_id, is_grafana_admin):
        change_user_permissions = '/api/admin/users/%s/permissions' % (user_id)
        r = self.api.PUT(change_user_permissions, json={'isGrafanaAdmin': is_grafana_admin})
        return r

    def delete_user(self, user_id):
        delete_user_path = '/admin/users/%s' % (user_id)
        r = self.api.DELETE(delete_user_path)
        return r

    def user_exist(self, loginOrEmail):
        search_user_path = '/users/lookup?loginOrEmail=%s' % (loginOrEmail)
        r = self.api.GET(search_user_path)

        resp = json.loads(r.content)
        if 'id' in resp:
            return resp['id']
        return -1

    def user_update(self, user_id, user):
        update_user_path = '/users/%s' % (user_id)
        r = self.api.PUT(update_user_path, json=user)
        return r

    def user_list(self):
        list_of_users = []
        users_on_page = None
        page = 1

        while users_on_page:
            show_users_path = '/users?perpage=10&page=%s' % (page)
            r = self.api.GET(show_users_path)
            users_on_page = r
            list_of_users += users_on_page
            page += 1

        return list_of_users

    def user_organisations(self):
        get_user_organisations = '/user/orgs'
        r = self.api.GET(get_user_organisations)
        return r

    def user_star_dashboard(self, dashboard_id):
        post_star_dashboard = '/user/stars/dashboard/%s' % (dashboard_id)
        r = self.api.POST(post_star_dashboard)
        return r

    def user_unstar_dashboard(self, dashboard_id):
        delete_unstar_dashboard = '/user/stars/dashboard/%s' % (dashboard_id)
        r = self.api.DELETE(delete_unstar_dashboard)
        return r

    def organisation_exist(self, org_name):
        get_org_path = '/orgs/name/%s' % (org_name)
        r = self.api.GET(get_org_path)

        resp = json.loads(r.content)
        if 'id' in resp:
            return resp['id']
        return -1

    def organisation_create(self, organisation):
        create_orgs_path = '/orgs'
        r = self.api.POST(create_orgs_path, json={'name': organisation['name']})
        organisation_id = r['orgId']
        return organisation_id, r

    def organisation_update(self, organisation_id, organisation):
        update_org_path = '/orgs/%s' % (organisation_id)
        r = self.api.PUT(update_org_path, json=organisation)
        return organisation_id, r

    def organisation_delete(self, organisation_id):
        delete_org_path = '/orgs/%s' % (organisation_id)
        r = self.api.DELETE(delete_org_path)
        return r

    def organisation_list(self):
        search_org_path = '/orgs'
        r = self.api.GET(search_org_path)
        return r

    def organisation_switch(self, organisation_id):
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

    def datasource_exist(self, datasource_name):
        get_datasource_path = '/datasources/name/%s' % (datasource_name)
        r = self.api.GET(get_datasource_path)

        resp = json.loads(r.content)
        if 'id' in resp:
            return resp['id']
        return -1

    def datasource_get(self, datasource_id):
        get_datasource_path = '/datasources/%s' % (datasource_id)
        r = self.api.GET(get_datasource_path)
        return r

    def datasource_create(self, datasource):
        create_datasources_path = '/datasources'
        r = self.api.POST(create_datasources_path, json=datasource)
        return r

    def datasource_update(self, datasource_id, datasource):
        update_datasource = '/datasources/%s' % (datasource_id)
        r = self.api.PUT(update_datasource, json=datasource)
        return r

    def datasource_list(self):
        list_datasource = '/datasources'
        r = self.api.GET(list_datasource)
        return r

    def datasource_delete(self, name):
        delete_datasource = '/datasources/name/%s' % (name)
        r = self.api.DELETE(delete_datasource)
        return r

    def dashboard_list(self):
        list_dashboard_path = '/search/'
        r = self.api.GET(list_dashboard_path)
        return r

    def dashboard_get(self, dashboard_slug):
        get_dashboard_path = '/dashboards/%s' % (dashboard_slug)
        r = self.api.GET(get_dashboard_path)
        return r

    def dashboard_put(self, dashboard):
        put_dashboard_path = '/dashboards/db'
        r = self.api.POST(put_dashboard_path, json=dashboard)
        return r

    def dashboard_delete(self, dashboard_slug):
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
