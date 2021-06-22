# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in ipcameras/__init__.py
from ipcameras import __version__ as version

setup(
	name='ipcameras',
	version=version,
	description='App to control and view the stream of Dahua IPCameras setup streaming in MJPEG format by using a proxy server built in NodeJS to authenticate using Digest Authentication.',
	author='Diogo Livio',
	author_email='d.livio@campus.fct.unl.pt',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
