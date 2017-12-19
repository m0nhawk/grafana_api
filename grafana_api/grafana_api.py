import requests


class GrafanaAPI:
    def __init__(self, auth, host='localhost', port=None, url_path_prefix='', protocol='http'):
        self.auth = auth
        self.url_host = host
        self.url_port = port
        self.url_path_prefix = url_path_prefix
        self.url_protocol = protocol

        def construct_api_url():
            params = {
                'protocol': self.url_protocol,
                'host': self.url_host,
                'url_path_prefix': self.url_path_prefix,
            }

            if self.url_port is None:
                url_pattern = '{protocol}://{host}/{url_path_prefix}api'
            else:
                params['port'] = self.url_port
                url_pattern = '{protocol}://{host}:{port}/{url_path_prefix}api'

            return url_pattern.format(**params)

        self.url = construct_api_url()

    def __getattr__(self, item):
        def __requests_run(url, json=None, headers=None):
            __url = '%s%s' % (self.url, url)
            runner = getattr(requests, item.lower())
            r = runner(__url, json=json, headers=headers, auth=self.auth)
            return r

        return __requests_run
