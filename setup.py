import os.path
import pathlib
from os.path import exists
from setuptools import setup, find_packages


CURRENT_DIR = pathlib.Path(__file__).parent
long_description = ""
readme_md_file = os.path.join(CURRENT_DIR, "README.md")
if exists(readme_md_file):
    long_description = pathlib.Path(readme_md_file).read_text()

env = os.environ.get('source')


def get_dependencies():
    dependency = []

    if env and env == "code":
        return dependency

    return dependency + []


setup(
    name='mweb-dev',
    version='0.0.1',
    long_description=long_description,
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    py_modules=["mweb_app"],
    entry_points={'console_scripts': ['mweb=mweb_app:cli']},
    install_requires=get_dependencies(),
    classifiers=[]
)
