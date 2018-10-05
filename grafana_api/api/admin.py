from .base import Base


class Admin(Base):
    def __init__(self, api):
        super().__init__(api)
        self.api = api
        self.path = '/admin'

    def settings(self):
        path = 'settings'
        r = self.api.GET('/'.join([self.path, path]))
        return r

    def stats(self):
        path = 'stats'
        r = self.api.GET('/'.join([self.path, path]))
        return r

    def create_user(self, user):
        create_user_path = 'users'
        r = self.api.POST(create_user_path, json=user)
        return r

    def change_user_password(self, user_id, password):
        change_user_password_path = self.path + '/users/%s/password' % (user_id)
        r = self.api.PUT(change_user_password_path, json={'password': password})
        return r

    def change_user_permissions(self, user_id, is_grafana_admin):
        change_user_permissions = self.path + '/users/%s/permissions' % (user_id)
        r = self.api.PUT(change_user_permissions, json={'isGrafanaAdmin': is_grafana_admin})
        return r

    def delete_user(self, user_id):
        delete_user_path = '/admin/users/%s' % (user_id)
        r = self.api.DELETE(delete_user_path)
        return r

    def pause_all_alerts(self, pause):
        change_user_permissions = self.path + '/pause-all-alerts'
        r = self.api.POST(change_user_permissions, json={'paused': pause})
        return r
