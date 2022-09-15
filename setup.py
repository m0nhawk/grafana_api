# Required for editable installs
# https://discuss.python.org/t/specification-of-editable-installation/1564/
from setuptools import setup
setup(
    use_scm_version={
        "local_scheme": "no-local-version",
        "version_scheme": "python-simplified-semver",
        "write_to": "grafana_api/version.py",
    },
    # For all dependent libraries
    install_requires=['requests'],
)
