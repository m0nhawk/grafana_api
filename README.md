# grafana_api [![CircleCI](https://img.shields.io/circleci/project/github/m0nhawk/grafana_api.svg?style=flat-square&logo=circleci)](https://circleci.com/gh/m0nhawk/workflows/grafana_api/tree/master) [![GitHub license](https://img.shields.io/github/license/m0nhawk/grafana_api.svg?style=flat-square)](https://github.com/m0nhawk/grafana_api/blob/master/LICENSE)  [![Codecov](https://img.shields.io/codecov/c/gh/m0nhawk/grafana_api.svg?style=flat-square)](https://codecov.io/gh/m0nhawk/grafana_api/)

[![PyPI](https://img.shields.io/pypi/v/grafana_api.svg?style=flat-square)](https://pypi.org/project/grafana-api/) [![Conda](https://img.shields.io/conda/v/m0nhawk/grafana_api.svg?style=flat-square)](https://anaconda.org/m0nhawk/grafana_api)

## What is this library for?

Yet another Grafana API library for Python. Support both 2 and 3 Python versions.

## Requirements

You need either 2nd or 3rd version of Python and only the `requests` library installed.

## Quick start

Install the pip package:

```
pip install -U grafana_api
```

And then connect to your Grafana API endpoint:

```python
from grafana_api.grafana_face import GrafanaFace

grafana_api = GrafanaFace(auth='abcde....', host='api.my-grafana-host.com')

# Search dashboards based on tag
grafana_api.search.search_dashboards(tag='applications')

# Find a user by email
grafana_api.users.find_user('test@test.com')

# Create or update a dashboard
grafana_api.dashboard.update_dashboard(dashboard={'dashboard': {...}, 'folderId': 0, 'overwrite': True})

# Delete a dashboard by UID
grafana_api.dashboard.delete_dashboard(dashboard_uid='abcdefgh')
```

## Status of REST API realization [![Coverage Status](https://coveralls.io/repos/github/m0nhawk/grafana_api/badge.svg?branch=master)](https://coveralls.io/github/m0nhawk/grafana_api?branch=master)

Work on API implementation still in progress.

| API | Status |
|---|---|
| Admin | + |
| Alerting | - |
| Annotations | - |
| Authentication | +- |
| Dashboard | + |
| Dashboard Versions | - |
| Dashboard Permissions | + |
| Data Source | + |
| Folder | + |
| Folder Permissions | + |
| Folder/Dashboard Search | +- |
| Organisation | + |
| Other | + |
| Preferences | + |
| Snapshot | - |
| Teams | - |
| User | + |

## Issue tracker

Please report any bugs and enhancement ideas using the `grafana_api` issue tracker:

  https://github.com/m0nhawk/grafana_api/issues

Feel free to also ask questions on the tracker.

## License

`grafana_api` is licensed under the terms of the MIT License (see the file
[LICENSE](LICENSE)).
