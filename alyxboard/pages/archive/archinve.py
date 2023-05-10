# https://youtu.be/G65iy0AmthM

import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

from dash import dash_table
from dash.dash_table.Format import Group

import pandas as pd
dash.register_page(__name__)

layout = dbc.Row(children=[
    # screen sizes: xs(eXtra Small), sm (SMall), md(MeDium), lg (large)
    dbc.Col(lg=3, sm=6, children=[
        dcc.Input(id='adding-rows-name', placeholder="enter", value='', style={'padding':"10px"}),
        html.Button('add col', )
    ]),

    dbc.Col(children='''
        xx This is our Archive page content.
    '''),
])
