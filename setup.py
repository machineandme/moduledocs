from setuptools import setup, find_packages
from os import path
import json


def requirements_from_pipfile_lock(file_path='Pipfile.lock'):
    with open(file_path) as file:
        pipfile = json.load(file)
    return [r + a['version'] for r, a in pipfile['default'].items()]


requirements = requirements_from_pipfile_lock()
here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()


setup(
    name='moduledocs',
    version='1.0.1',
    description='Static documentation extraction tool for python language',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/machineandme/moduledocs',
    author='Machine & Me',
    author_email='ceo@machineand.me',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Documentation',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        # These classifiers are *not* checked by 'pip install'. See instead
        # 'python_requires' below.
        'Programming Language :: Python :: 3',
    ],
    keywords='generate documentation markdown html static parser',
    packages=find_packages(exclude=['contrib', 'docs', 'tests', 'examples']),
    install_requires=requirements,
    python_requires='>=3.5.*',
    package_data={},
    entry_points={
        'console_scripts': [
            'moduledocs=moduledocs.cli:main',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/machineandme/moduledocs/issues',
        'Funding': 'https://www.patreon.com/machineandme',
        'Source': 'https://github.com/machineandme/moduledocs'
    },
)
