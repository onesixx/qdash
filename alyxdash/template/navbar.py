import dash
from dash import Input, Output, State, dcc, html
import dash_bootstrap_components as dbc

# navbar_right = dbc.Collapse(navbar=True, children=[
#     html.Div(className="collapse navbar-collapse justify-content-end", children=[
#         html.Ul(className="nav navbar-nav mr-auto", children=[
#             # html.Form(className="navbar-form navbar-left navbar-search-form", role="search", children=[
#             #     html.Div(className="input-group", children=[
#             #         html.I(className="nc-icon nc-zoom-split"),
#             #         dbc.Input(className="form-control", type="text", placeholder="Search...")
#             #     ]),
#             # ]),
#         ]),

#         dbc.Nav(navbar=True, children=[
#             dbc.DropdownMenu(
#                 label=html.I(className="nc-icon nc-planet"),
#                 nav=True, in_navbar=True, children=[
#                     dbc.DropdownMenuItem("Create New Post", href="#"),
#                     dbc.DropdownMenuItem("Manage Something", href="#"),
#                     dbc.DropdownMenuItem("Do Nothing", href="#"),
#                     dbc.DropdownMenuItem("Submit to live", href="#"),
#                     dbc.DropdownMenuItem(divider=True),
#                     dbc.DropdownMenuItem("Another action", href="#"),
#                 ]),
#             dbc.DropdownMenu(
#                 label=[
#                     html.I(className="nc-icon nc-bell-55"),
#                     html.Span("5", className="notification"),
#                     html.Span("Notification", className="d-lg-none"),
#                 ],
#                 nav=True, in_navbar=True, children=[
#                     dbc.DropdownMenuItem("Notification 1", href="#"),
#                     dbc.DropdownMenuItem("Notification 2", href="#"),
#                     dbc.DropdownMenuItem("Notification 3", href="#"),
#                     dbc.DropdownMenuItem("Notification 4", href="#"),
#                 ]),
#             dbc.DropdownMenu(
#                 label=html.I(className="nc-icon nc-bullet-list-67"),
#                 nav=True, in_navbar=True, align_end=True, children=[
#                     dbc.DropdownMenuItem(href="#", children=[
#                         html.I(className="nc-icon nc-email-85"),
#                         " Messages",
#                     ]),
#                     dbc.DropdownMenuItem(divider=True),
#                     dbc.DropdownMenuItem(href="#", children=[
#                         html.I(className="nc-icon nc-lock-circle-open"),
#                         " Lock Screen",
#                     ]),
#                     dbc.DropdownMenuItem(className="text-danger", href="#", children=[
#                         html.I(className="nc-icon nc-button-power"),
#                         " Log out",
#                     ]),
#                 ]),
#         ]),
#     ]),
# ])

# navbar = dbc.Navbar(className="navbar-expand-lg sticky-top", color="light", dark=False,  children=[
navbar = dbc.Navbar(className="navbar-expand-lg", color="light", dark=False,  children=[
    html.Div(className="container-fluid", children=[
        html.Div(className="navbar-wrapper ",  children=[
            html.Div(className="navbar-minimize", children=[
                dbc.Button(id="sidebar-toggle", className="btn btn-warning btn-fill btn-round btn-icon d-none d-lg-block",  # id="minimizeSidebar",
                    children=[
                        html.I(
                            className="fa fa-ellipsis-v visible-on-sidebar-regular"),
                        html.I(
                            className="fa fa-navicon visible-on-sidebar-mini"),
                    ]),
            ]),
            html.A("Dashboard PRO", className="navbar-brand", href="#pablo")
        ]),

        # html.Div(className="navbar-toggler navbar-toggler-right", id="right_menu", children=[
        dbc.Button(id="right_menu", className="navbar-toggler navbar-toggler-right", children=[
            html.Span(className="navbar-toggler-bar burger-lines"),
            html.Span(className="navbar-toggler-bar burger-lines"),
            html.Span(className="navbar-toggler-bar burger-lines"),
        ])
        # navbar_right,
    ]),
])
