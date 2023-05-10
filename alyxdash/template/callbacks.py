import dash
from dash import Input, Output, State, dcc, html
import dash_bootstrap_components as dbc


def callbacks_template(app):
    # @app.callback(
    #     Output("page-content", "children"),
    #     [Input("urlpath", "pathname")])
    # def render_page_content(pathname):
    #     if pathname == "/":
    #         return html.P("This is the content of the HOME page!")
    #     elif pathname == "/page-1":
    #         return html.P("This is the content of page 1. Yay!")
    #     elif pathname == "/page-2":
    #         return html.P("Oh cool, this is page 2!")
    #     # If the user tries to reach a different page, return a 404 message
    #     return html.Div(className="p-3 bg-light rounded-3", children=[
    #         html.H1("404: Not found", className="text-danger"),
    #         html.Hr(),
    #         html.P(f"The pathname {pathname} was not recognised..."),
    #     ])

    @app.callback(
        Output("mybody", "className"),
        [Input("sidebar-toggle", "n_clicks")],
        [State("mybody", "className")],
    )
    def toggle_classname(n, classname):
        print(f"classname: {n}|{classname}")
        if n == None:
            return "sidebar-mini"
        elif n and classname == "":
            return "sidebar-mini"
        return ""  # removeClass('sidebar-mini')

    # @app.callback(
    #     dash.dependencies.Output("mybody", "style"),
    #     [dash.dependencies.Input("right_menu", "n_clicks")]
    # )
    # def toggle_hidden_content(clicks1):
    #     print(clicks1)
    #     if clicks1 != None:
    #         if clicks1 > 0:
    #             return {"right": "0 !important"}
    #         else:
    #             return {"display": "none"}

    @app.callback(
        Output("mybody_wrapper", "className"),
        Input("right_menu", "n_clicks"),
        State("mybody_wrapper", "className"),
    )
    def toggle_class(n_clicks, class_name):
        if n_clicks == None:
            return class_name
        elif n_clicks and n_clicks % 2 == 0:
            return class_name.replace("nav-open", "")
        else:
            return class_name + " nav-open"
    # wrapper nav-open

    # @app.callback(
    #     Output("collapse", "is_open"),
    #     [Input("navbar-toggle", "n_clicks")],
    #     [State("collapse", "is_open")],
    # )
    # def toggle_collapse(n, is_open_yn):
    #     if n:
    #         return not is_open_yn
    #     return is_open_yn
