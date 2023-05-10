# import base64
# import io
import alyxdash

import io
import base64
import os
import time
import pathlib

import dash
from dash import Input, Output, State, dcc, html
import dash_bootstrap_components as dbc

import pandas as pd
import plotly.graph_objs as go

DATA_PATH = pathlib.Path(
    alyxdash.__path__[0]).parent.joinpath("data").resolve()
