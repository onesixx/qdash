import dash
from dash import html, dcc

dash.register_page(__name__, path='/', order=0)

layout = html.Div(children=[
    html.H1(children='This is our Home page'),

    html.Div(children='''
        xx This is our Home page content.
    '''),

])
