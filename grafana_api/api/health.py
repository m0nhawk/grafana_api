from .base import Base


class Health(Base):
    def __init__(self, api):
        super(Health, self).__init__(api)
        self.api = api

    def check(self):
        """

        :return:
        """
        path = "/health"
        r = self.api.GET(path)
        return r


