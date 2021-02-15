#!/usr/bin/env python

"""
Calculates new grade based on input value
"""

import pandas as pd

def grade(grade_file, syllabus, new_type, new_grade):
    """
    Shows the current grade and expected grade based on the csv file given.

    Parameters
    ----------
    grade_file (str):
        the name of the grade file
    syllabus (str):
        the name of the syllabus file
    new_type (str):
        the type of the new grade to be added
    new_grade (int):
        the percentage of the new grade to be added
    """
    data = pd.read_csv(grade_file)
    syll_data = pd.read_csv(syllabus)
    print(f"Previous Grade: {calculate_grade(data, syll_data)}")
    row_list = ["Possible Grade", new_type, new_grade]
    row = {i: j for (i, j) in zip(list(data), row_list)}
    data = data.append(row, ignore_index=True)
    print(f"New Grade: {calculate_grade(data, syll_data)}")

def calculate_grade(grade_df, syllabus_df):
    """
    Calculates the final grade based on the breakdowns given in the syllabus.

    Parameters
    ----------
    grade_df (DataFrame):
        Pandas DataFrame with grade information.
    syllabus_df (DataFrame):
        Pandas DataFrame with grade breakdown from syllabus.
    """
    grade_means = grade_df.groupby("Type").mean()
    df = grade_means.join(syllabus_df.set_index("Type"), on="Type")
    df = df.assign(Raw = df["Grade"] * df["Percentage"]/100)
    return df["Raw"].sum()