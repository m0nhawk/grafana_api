from .base import Base


class Notifications(Base):
    def __init__(self, api):
        super(Notifications, self).__init__(api)
        self.api = api

    def get_channels(self):
        get_channels_path = "/alert-notifications"
        return self.api.GET(get_channels_path)

    def lookup_channels(self):
        lookup_channels_path = "/alert-notifications/lookup"
        return self.api.GET(lookup_channels_path)

    def get_channel_by_uid(self, channel_uid):
        get_channel_by_uid_path = "/alert-notifications/uid/%s" % channel_uid
        return self.api.GET(get_channel_by_uid_path)

    def get_channel_by_id(self, channel_id):
        get_channel_by_id_path = "/alert-notifications/%s" % channel_id
        return self.api.GET(get_channel_by_id_path)

    def create_channel(self, channel):
        create_channel_path = "/alert-notifications"
        return self.api.POST(create_channel_path, json=channel)

    def update_channel_by_uid(self, uid, channel):
        update_channel_by_uid_path = "/alert-notifications/uid/%s" % uid
        return self.api.PUT(update_channel_by_uid_path, json=channel)

    def update_channel_by_id(self, id, channel):
        update_channel_by_id_path = "/alert-notifications/%s" % id
        return self.api.PUT(update_channel_by_id_path, json=channel)

    def delete_notification_by_uid(self, notification_uid):
        delete_notification_by_uid_path = "alert-notifications/uid/%s" % notification_uid
        return self.api.DELETE(delete_notification_by_uid_path)

    def delete_notification_by_id(self, notification_id):
        delete_notification_by_id_path = "alert-notifications/uid/%s" % notification_id
        return self.api.DELETE(delete_notification_by_id_path)


