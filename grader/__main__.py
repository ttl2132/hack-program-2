#!/usr/bin/env python

"""
Command line argparser for grader
"""

import argparse
from .grader import grade


def parse_arguments():
    """
    Parses CLI arguments using argparse
    """

    # init argparse class object
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-g",
        "--gradefile",
        required=True,
        help="the file containing grades"
    )

    parser.add_argument(
        "-s",
        "--syllabus",
        required=True,
        help="the file containing the syllabus grade breakdown"
    )

    parser.add_argument(
        "-t",
        "--type",
        required=True,
        help="input grade type"
    )

    parser.add_argument(
        "-n",
        "--newgrade",
        required=True,
        help="input grade as number out of 100",
        type=int
    )
    # return arg dict-like object containing user arguments
    args = parser.parse_args()
    return args


def run_program():
    "runs the command line program"
    # get CLI arguments
    args = parse_arguments()
    grade(args.gradefile, args.syllabus, args.type, args.newgrade)
