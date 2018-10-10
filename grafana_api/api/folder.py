from .base import Base


class Folder(Base):
    def __init__(self, api):
        super().__init__(api)
        self.api = api

    def get_all_folders(self):
        """

        :return:
        """
        path = '/folders'
        r = self.api.GET(path)
        return r

    def get_folder(self, uid):
        """

        :param uid:
        :return:
        """
        path = '/folders/%s' % uid
        r = self.api.GET(path)
        return r

    def create_folder(self, title, uid=None):
        """

        :param title:
        :param uid:
        :return:
        """
        json_data = dict(title=title)
        if uid is not None:
            json_data['uid'] = uid
        return self.api.POST('/folders', json=json_data)

    def update_folder(self, uid, title):
        """

        :param uid:
        :param title:
        :return:
        """
        path = '/folders' % uid
        r = self.api.PUT(path, json={
            "title": title
        })
        return r

    def delete_folder(self, uid):
        """

        :param uid:
        :return:
        """
        path = '/folders/%s' % uid
        r = self.api.DELETE(path)
        return r

    def get_folder_by_id(self, folder_id):
        """

        :param folder_id:
        :return:
        """
        path = '/folders/id/%s' % folder_id
        r = self.api.GET(path)
        return r

    def get_folder_permissions(self):
        """

        :return:
        """
        path = '/folders/%s/permissions'
        r = self.api.GET(path)
        return r

    def update_folder_permissions(self, uid, items):
        """

        :param uid:
        :param items:
        :return:
        """
        update_folder_permissions_path = '/folders/%s/permissions' % uid
        r = self.api.POST(update_folder_permissions_path, json=items)
        return r
