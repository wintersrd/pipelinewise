#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.md") as f:
    long_description = f.read()

setup(
    name="pipelinewise",
    version="0.10.3",
    description="PipelineWise",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="TransferWise",
    url="https://github.com/transferwise/pipelinewise",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3 :: Only",
    ],
    install_requires=[
        "argparse==1.4.0",
        "botocore==1.13.49",
        "tabulate==0.8.6",
        "PyYAML==5.1.0",
        "jsonschema==3.0.1",
        "ansible==2.9.2",
        "joblib==0.14.1",
        "attrs==17.4.0",
        "idna==2.8",
        "PyMySQL==0.9.3",
        "psycopg2==2.8.4",
        "boto3==1.10.49",
        "pytz==2018.4",
        "backoff==1.8.0",
        "psutil==5.6.7",
        "snowflake-connector-python==2.1.1",
    ],
    extras_require={
        "test": [
            "pytest==5.0.1",
            "pytest-dependency==0.4.0",
            "coverage==4.5.3",
            "python-dotenv==0.10.3",
        ]
    },
    entry_points="""
        [console_scripts]
        pipelinewise=pipelinewise.cli:main
        mysql-to-snowflake=pipelinewise.fastsync.mysql_to_snowflake:main
        postgres-to-snowflake=pipelinewise.fastsync.postgres_to_snowflake:main
        mysql-to-redshift=pipelinewise.fastsync.mysql_to_redshift:main
        postgres-to-redshift=pipelinewise.fastsync.postgres_to_redshift:main
    """,
    packages=find_packages(exclude=["tests*"]),
    package_data={"schemas": ["pipelinewise/cli/schemas/*.json"]},
    include_package_data=True,
)
