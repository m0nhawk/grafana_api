from .base import Base


class Search(Base):
    def __init__(self, api):
        super().__init__(api)
        self.api = api
        self.path = '/users'

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
