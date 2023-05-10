# alyxdash/utils.py
import pandas as pd
import plotly.express as px

def formatter_2_decimals(x):
    return "{:.2f}".format(x)


def rleid(aserise):
    # aserise = df[col]
    char = "sixx"
    group = 0
    result = []
    for i in aserise.index:  # range(0, len(aserise)):
        # i = 11
        if aserise[i] == char:
            result.append(group)
        else:
            group = group + 1
            result.append(group)
            char = aserise[i]
    return result


def make_pdata_undup(df, col, part=False):
    # df = px.data.iris()
    # col = "sepal_length"
    uniqueIdx = ~(pd.Series(rleid(df[col])).duplicated(keep='first')) | \
                ~(pd.Series(rleid(df[col])).duplicated(keep='last'))
    pdata = df.loc[uniqueIdx.tolist()]
    if part :
        pdata = df.loc[:, [col]]
    return pdata


def clean_data(data):
    """
    A function to clean data before processing.
    """
    # implementation code here
    cleaned_data = ...
    return cleaned_data


def validate_input(input):
    """
    A function to validate user input.
    """
    # implementation code here
    valid_input = ...
    return valid_input


def format_output(output):
    """
    A function to format the output of a process or calculation.
    """
    # implementation code here
    formatted_output = ...
    return formatted_output



from pathlib import Path

def get_project_root() -> Path:
    return str(Path(__file__).parent.parent)