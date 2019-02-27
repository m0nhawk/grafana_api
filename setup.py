from setuptools import setup

with open('README.md') as file:
    long_description = file.read()

setup(name='grafana_api',
      version='0.5.2',
      description='Yet another Python library for Grafana API',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/m0nhawk/grafana_api',
      author='Andrew Prokhorenkov',
      author_email='andrew.prokhorenkov@gmail.com',
      license='MIT',
      packages=[
          'grafana_api',
          'grafana_api.api'
      ],
      install_requires=[
          'requests',
      ],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Topic :: Internet',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Operating System :: OS Independent',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
      ],
      zip_safe=False)
