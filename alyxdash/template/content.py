import dash
from dash import Input, Output, State, dcc, html
import dash_bootstrap_components as dbc


# content_home = dbc.Row(className="row", children=[
#     dbc.Col(lg=3, sm=6, children=[
#         dbc.Card(className="card-stats", children=[
#             dbc.CardBody(children=[
#                 html.Div(className="row", children=[
#                     dbc.Col(width=5,  children=[
#                         html.Div(className="icon-big text-center icon-warning",  children=[
#                             html.I(
#                                 className="nc-icon nc-chart text-warning"),
#                         ]),
#                     ]),
#                     dbc.Col(width=7, children=[
#                         html.Div(className="numbers", children=[
#                             html.P(className="card-category",
#                                            children="Number"),
#                             html.H4(className="card-title",
#                                     children="150GB"),
#                         ])
#                     ]),
#                 ]),
#             ]),
#             dbc.CardFooter(children=[
#                 html.Hr(),
#                 html.Div(className="stats", children=[
#                     html.I(className="fa fa-refresh"),
#                     " Update Now",
#                 ],
#                 ),
#             ]),
#         ]),
#     ]),
# ])

content = html.Div(className="content", children=[
    html.Div(id="page-content", #className="container-fluid",
             children=[
        # content_home
        dash.page_container
    ]),
])
