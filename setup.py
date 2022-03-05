from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in cityeletricitydistribution/__init__.py
from cityeletricitydistribution import __version__ as version

setup(
	name="cityeletricitydistribution",
	version=version,
	description="this app is about electricity bill",
	author="Rajnish Yadav",
	author_email="rajnishyadav.powerit@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
