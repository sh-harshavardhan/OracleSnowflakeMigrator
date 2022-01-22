#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This module sets up the package for the oracle_snowflake_migrator"""

from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="oracle_snowflake_migrator",
    author="Sai Harshavardhan Tallapalli",
    author_email="ekharshavardhan851@gmail.com",
    maintainer="Sai Harshavardhan Tallapalli",
    maintainer_email="ekharshavardhan851@gmail.com",
    version="0.1.2",
    url="https://github.com/sh-harshavardhan/OracleSnowflakeMigrator.git",
    download_url='https://github.com/sh-harshavardhan/OracleSnowflakeMigrator.git',
    keywords=['oracle', 'snowflake', 'migration', 'etl', 'schema'],
    license="GNU GENERAL PUBLIC LICENSE",
    description="Logs you into work",
    long_description=long_description,
    # long_description_content_type="text/markdown",
    project_urls={
        "Bug Tracker": "https://github.com/sh-harshavardhan/OracleSnowflakeMigrator/issues",
    },
    python_requires=">=3.6",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'cx_Oralce',
        'snowflake-connector-python',
    ],
    entry_points={
        'console_scripts': [
            'migrate = __main__:main',
            'test = __main__:test_setup',
        ]},
    # setup_requires=['pytest-runner'],
    # tests_require=['pytest'],
)
