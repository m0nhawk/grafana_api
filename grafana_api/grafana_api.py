import requests


class GrafanaAPI:
    def __init__(self, host, auth):
        self.host = host
        self.auth = auth

    def GET(self, url, headers=None):
        _url = '%s%s' % (self.host, url)
        r = requests.get(_url, headers=headers, auth=self.auth)
        return r

    def POST(self, url, json=None, headers=None):
        _url = '%s%s' % (self.host, url)
        r = requests.post(_url, json=json, headers=headers, auth=self.auth)
        return r

    def PUT(self, url, json=None, headers=None):
        _url = '%s%s' % (self.host, url)
        r = requests.put(_url, json=json, headers=headers, auth=self.auth)
        return r

    def PATCH(self, url, json=None, headers=None):
        _url = '%s%s' % (self.host, url)
        r = requests.patch(_url, json=json, headers=headers, auth=self.auth)
        return r

    def DELETE(self, url, headers=None):
        _url = '%s%s' % (self.host, url)
        r = requests.delete(_url, headers=headers, auth=self.auth)
        return r
