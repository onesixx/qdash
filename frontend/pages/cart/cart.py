import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, ClientsideFunction

import numpy as np
import pandas as pd
import datetime
from datetime import datetime as dt
import pathlib

dash.register_page(__name__)

# Path
BASE_PATH = pathlib.Path(__file__).parent.resolve()
DATA_PATH = BASE_PATH.joinpath("data").resolve()

# Read data
#df = pd.read_csv(DATA_PATH.joinpath("clinical_analytics.csv.gz"))


layout = html.Div(children=[
    html.Div(
        id = "banner",
        className = 'banner',
        children=[
            f'This is our {__name__} pageKKKK'
        ]
    ),

    html.Div(
        id= "left_column",
        className = "four columns",
        children=[
            description_card(),
            generate_control_card(),
        ],
    ),

    html.Div(
        id= "right_column",
        className = "eight columns",
        children=[
            html.Div(
                id="patient_volume_card",
                children=[
                    html.B("Patient Volume"),
                    html.Hr(),
                    dcc.Graph(id="patient_volume_hm"),
                ],
            ),
        ],
    ),    
])


