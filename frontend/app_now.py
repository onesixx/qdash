import dash
from dash import Input, Output, State, dcc, html
import dash_bootstrap_components as dbc

from alyxdash import sidebar_icon, sidebar_header, navbar, content, footer, callbacks_template

# from alyxdash.sidebar import *
# https://dash-bootstrap-components.opensource.faculty.ai/docs/
# https://dash.plotly.com/dash-core-components

app = dash.Dash(
    __name__,
    url_base_pathname="/",
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        dbc.icons.FONT_AWESOME,
    ],
    meta_tags=[
        # for desktop, notebook, tablelet, smartphone
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ],
    use_pages=True
)
# app.config.suppress_callback_exceptions = True
server = app.server

# sidebar
sidebar = html.Div(className="sidebar", **{"data-color": "orange"}, children=[  #
    html.Div(className="sidebar-wrapper", children=[
        sidebar_header,
        # sidebar_user,
        dbc.Collapse(id="collapse",  className="nav", children=[
            # html.Div(className="nav", children=[
            dbc.Nav(className="nav nav-item", vertical=True, pills=True, children=[
                dbc.NavLink(href=page["relative_path"], active="exact", className="nav-link", children=[
                    html.I(className=sidebar_icon[index]),
                    html.Span(page['name']),
                ])
            ]) for index, page in enumerate(dash.page_registry.values())
            if page["module"] != "pages.not_found_404"
        ]),
    ])
])

# navbar, content, footer  => main
main = html.Div(className="main-panel", children=[
    navbar,
    content,  # dash.page_container
    footer
])

app.layout = dbc.Container(id="mybody", className="", fluid=True,
    children=[
    html.Div(id="mybody_wrapper", className="wrapper",
        children=[
        sidebar,
        main
    ])
])

callbacks_template(app)

if __name__ == "__main__":
    app.run_server(debug=True, port=8883)
