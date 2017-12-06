from setuptools import setup

setup(name='grafana_api',
      version='0.1.2',
      description='',
      url='https://github.com/m0nhawk/grafana_api',
      author='Andrew Prokhorenkov',
      author_email='andrew.prokhorenkov@gmail.com',
      license='MIT',
      packages=['grafana_api'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)
