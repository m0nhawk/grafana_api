# Required for editable installs
# https://discuss.python.org/t/specification-of-editable-installation/1564/
from setuptools import setup
setup(
    use_scm_version=True,
)
