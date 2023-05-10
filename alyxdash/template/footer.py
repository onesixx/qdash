import dash
from dash import Input, Output, State, dcc, html
import dash_bootstrap_components as dbc


footer = html.Footer(className="footer", children=[
    html.Div(className="container", children=[
        html.Nav(children=[
            html.Ul(className="footer-menu", children=[
                html.Li(html.A("Home", href="#")),
                html.Li(html.A("Company", href="#")),
                html.Li(html.A("Portfolio", href="#")),
                html.Li(html.A("Blog", href="#")),
            ]),
            html.P(className="copyright text-center", children=[
                "©",
                html.Script(
                    children="document.write(new Date().getFullYear())"
                ),
                html.A("BECOM",
                       href="http://onesixx.com"),
                ", made with love for a better solution",
            ]),
        ]),
    ]),
])
