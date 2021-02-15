#!/usr/bin/env python

"""
Install grader package. To install locally use:
    'pip install -e ."
"""

from setuptools import setup

setup(
    name="grader",
    version="0.0.1",
    packages=[],
    install_requires=["pandas"],
    entry_points={
        "console_scripts": ["grader = grader.__main__:run_program"]
    }
)
