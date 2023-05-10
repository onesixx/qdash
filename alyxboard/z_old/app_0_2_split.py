import dash
from dash import Input, Output, State, dcc, html
import dash_bootstrap_components as dbc

from cathydash import sidebar, navbar, content, footer, template_callbacks
# from cathydash.sidebar import *
# https://dash-bootstrap-components.opensource.faculty.ai/docs/
# https://dash.plotly.com/dash-core-components

app = dash.Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        dbc.icons.FONT_AWESOME,
    ],
    meta_tags=[
        # for desktop, notebook, tablelet, smartphone
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ],
)
server = app.server

# sidebar
# navbar
# content
# footer

main = html.Div(className="main-panel", children=[
    navbar,
    content,
    footer
])

app.layout = html.Div(id="mybody",  className="sidebar-mini", children=[
    html.Div(id="mybody_wrapper", className="wrapper", children=[
        dcc.Location(id="urlpath"),
        sidebar,
        main
    ])
])

template_callbacks(app)

if __name__ == "__main__":
    app.run_server(debug=True, port=8881)
