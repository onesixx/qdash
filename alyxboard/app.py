import dash

import alyxdash
from alyxdash.templates import layout

# from dash import dcc, html
import dash_bootstrap_components as dbc
# from dash.dependencies import Input, Output
# =============================================================================
# Dash App and Flask Server
# =============================================================================
app_dash = dash.Dash(
    __name__,
    meta_tags=[

        {"charset": "utf-8",
         "content": "width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0, shrink-to-fit=no",
         "name": "viewport"}
    ],
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        # <!-- Fonts and icons - ->
        "https://fonts.googleapis.com/css?family=Montserrat:400,700,200",
        "https://maxcdn.bootstrapcdn.com/font-awesome/latest/css/font-awesome.min.css",
        # <!-- CSS Files - ->
        "bootstrap.min.css",
        "light-bootstrap-dashboard.css?v=2.0.1",
        # < link href=rel="stylesheet" / >
        # <!-- CSS Just for demo purpose, don't include it in your project - ->
        "demo.css"
    ],
    # <head>
    # < link rel="apple-touch-icon" sizes="76x76" href="../assets/img/apple-icon.png" >
    # < link rel="icon" type="image/png"          href="../assets/img/favicon.png" >
    # < meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" / >
    # < /head >
)
app_dash.title = "Alyx Dashboard from Light Bootstrap Dashboard"
server = app_dash.server

# =============================================================================
# App Layout
# =============================================================================
app_dash.layout = layout

alyxdash.callbacks.get_callbacks(app_dash)


if __name__ == "__main__":
    app_dash.run_server(debug=True, port=8887)
