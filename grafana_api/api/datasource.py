from .base import Base


class Datasource(Base):
    def __init__(self, api):
        super(Datasource, self).__init__(api)
        self.api = api

    def find_datasource(self, datasource_name):
        """

        :param datasource_name:
        :return:
        """
        get_datasource_path = "/datasources/name/%s" % datasource_name
        r = self.api.GET(get_datasource_path)
        return r

    def get_datasource_by_id(self, datasource_id):
        """

        :param datasource_id:
        :return:
        """
        get_datasource_path = "/datasources/%s" % datasource_id
        r = self.api.GET(get_datasource_path)
        return r

    def get_datasource_by_name(self, datasource_name):
        """

        :param datasource_name:
        :return:
        """
        get_datasource_path = "/datasources/name/%s" % datasource_name
        r = self.api.GET(get_datasource_path)
        return r

    def get_datasource_id_by_name(self, datasource_name):
        """

        :param datasource_name:
        :return:
        """
        get_datasource_path = "/datasources/id/%s" % datasource_name
        r = self.api.GET(get_datasource_path)
        return r

    def create_datasource(self, datasource):
        """

        :param datasource:
        :return:
        """
        create_datasources_path = "/datasources"
        r = self.api.POST(create_datasources_path, json=datasource)
        return r

    def update_datasource(self, datasource_id, datasource):
        """

        :param datasource_id:
        :param datasource:
        :return:
        """
        update_datasource = "/datasources/%s" % datasource_id
        r = self.api.PUT(update_datasource, json=datasource)
        return r

    def list_datasources(self):
        """

        :return:
        """
        list_datasources_path = "/datasources"
        r = self.api.GET(list_datasources_path)
        return r

    def delete_datasource_by_id(self, datasource_id):
        """

        :param datasource_id:
        :return:
        """
        delete_datasource = "/datasources/%s" % datasource_id
        r = self.api.DELETE(delete_datasource)
        return r

    def delete_datasource_by_name(self, datasource_name):
        """

        :param datasource_name:
        :return:
        """
        delete_datasource = "/datasources/name/%s" % datasource_name
        r = self.api.DELETE(delete_datasource)
        return r

    def get_datasource_proxy_data(self, datasource_id
	, query_type='query'
        , version='v1'
        , expr=None
	, time=None
	, start=None
	, end=None
	, step=None
    ):
        """

        :param datasource_id:
        :param version: api_version currently v1
        :param query_type: query_range |query
        :param expr: expr to query

        :return:
        """
        get_datasource_path = "/datasources/proxy/{}" \
		'/api/{}/{}?query={}'.format( datasource_id, version, query_type, expr)
        if query_type == 'query_range':
           get_datasource_path = get_datasource_path + '&start={}&end={}&step={}'.format(
		start, end, step)
        else:
           get_datasource_path = get_datasource_path + '&time={}'.format(time)
        r = self.api.GET(get_datasource_path)
        return r


