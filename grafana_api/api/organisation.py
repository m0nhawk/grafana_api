from .base import Base


class Organisation(Base):
    def __init__(self, api):
        super().__init__(api)
        self.api = api

    def find_organisation(self, org_name):
        """

        :param org_name:
        :return:
        """
        get_org_path = '/orgs/name/%s' % org_name
        r = self.api.GET(get_org_path)
        return r

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
        return r

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
        update_user_current_organisation_path = '/org/users/%s' % user_id
        r = self.api.PATCH(update_user_current_organisation_path, json=user)
        return r

    def delete_user_current_organisation(self, user_id):
        """

        :param user_id:
        :return:
        """
        delete_user_current_organisation_path = '/org/users/%s' % user_id
        r = self.api.DELETE(delete_user_current_organisation_path)
        return r


class Organisations(Base):
    def __init__(self, api):
        super().__init__(api)
        self.api = api
        self.path = '/users'

    def update_organisation(self, organisation_id, organisation):
        """

        :param organisation_id:
        :param organisation:
        :return:
        """
        update_org_path = '/orgs/%s' % organisation_id
        r = self.api.PUT(update_org_path, json=organisation)
        return r

    def delete_organisation(self, organisation_id):
        """

        :param organisation_id:
        :return:
        """
        delete_org_path = '/orgs/%s' % organisation_id
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
        switch_user_organisation = '/user/using/%s' % organisation_id
        r = self.api.POST(switch_user_organisation)
        return r

    def organisation_user_list(self, organisation_id):
        """

        :param organisation_id:
        :return:
        """
        users_in_org = '/orgs/%s/users' % organisation_id
        r = self.api.GET(users_in_org)
        return r

    def organisation_user_add(self, organisation_id, user):
        """

        :param organisation_id:
        :param user:
        :return:
        """
        add_user_path = '/orgs/%s/users' % organisation_id
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

    def organisation_preference_get(self):
        """
        :return:
        """
        update_preference = '/org/preferences'
        r = self.api.GET(update_preference)
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
