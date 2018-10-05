from .base import Base


class Folder(Base):
    def __init__(self, api):
        super().__init__(api)
        self.api = api
        self.path = '/users'

    def get_all_folders(self):
        path = '/folders'
        r = self.api.GET(path)
        return r

    def get_folder(self, uid):
        path = '/folders/%s' % (uid)
        r = self.api.GET(path)
        return r

    def create_folder(self, title, uid=None):
        """
        Creates a new folder.

        :param title: The title of the folder.
        :param uid: Optional unique identifier.
        """
        json_data = dict(title=title)
        if uid is not None:
            json_data['uid'] = uid
        return self.api.POST('/folders', json=json_data)

    def update_folder(self, uid, title):
        path = '/folders' % (uid)
        r = self.api.PUT(path, json={
            "title": title
        })
        return r

    def delete_folder(self, uid):
        path = '/folders/%s' % (uid)
        r = self.api.DELETE(path)
        return r

    def get_folder_by_id(self, id):
        path = '/folders/id/%s' % (id)
        r = self.api.GET(path)
        return r

    def get_folder_permissions(self):
        path = '/folders/%s/permissions'
        r = self.api.GET(path)
        return r

    def update_folder_permissions(self, uid, items):
        """
        Updates permissions for a folder.

        This operation will remove existing permissions if they’re not included in the request.

        :param uid: Folder uid
        """
        # TODO really relevant to return something?
        return self.api.POST('/folders/%s/permissions' % uid, json=dict(items=items))
