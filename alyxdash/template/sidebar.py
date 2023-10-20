
import dash
from dash import Input, Output, State, dcc, html
import dash_bootstrap_components as dbc

sidebar_icon = [
    "nc-icon nc-chart-pie-35",
    "fas fa-calendar-alt me-2",  
    "fas fa-envelope-open-text me-2",
    "fas fa-car-battery"
]

sidebar_header = html.Div(className="logo", style={'display': 'flex',  'align-items': "center", "justify-content": "flex-start", }, children=[
    html.Img(src="../assets/img/logo_small.png",
             style={"margin": "5px 15px", "padding-left": "13px"},),
    html.A(href="http://onesixx.com", style={},
           className="simple-text logo-normal", children="BECOM"),
])
# sidebar_user = dbc.Nav(className="user", vertical=True, pills=True, children=[
#     html.Div(className="photo", children=[
#         html.Img(src="assets/user-01.jpg")
#     ]),
#     html.Div(className="info", children=[
#         html.A(
#             html.Span([
#                 "Tania Andrew",
#                 html.B("", className="caret")
#             ]),
#             # href="#A",
#             className="collapsed",
#             **{"data-toggle": "collapse", "href": "#collapseExample"}
#         ),
#         html.Div(className="collapse", id="collapseExample", children=[
#             html.Ul(className="nav", children=[
#                 html.Li(
#                     html.A(href="#pablo", children=[
#                                 html.Span("MP", className="sidebar-mini"),
#                                 html.Span("My Profile",
#                                           className="sidebar-normal")
#                     ])
#                 ),
#                 html.Li(
#                     html.A(href="#pablo", children=[
#                                 html.Span("EP", className="sidebar-mini"),
#                                 html.Span("Edit Profile",
#                                           className="sidebar-normal")
#                     ])
#                 ),
#                 html.Li(
#                     html.A(href="#pablo", children=[
#                                 html.Span("S", className="sidebar-mini"),
#                                 html.Span(
#                                     "Settings", className="sidebar-normal")
#                     ]),
#                 )
#             ]),
#         ])
#     ])
# ])
# style="background-image: url(../assets/img/sidebar-5.jpg) "

sidebar = html.Div(className="sidebar", **{"data-color": "orange"}, children=[  #
    html.Div(className="sidebar-wrapper", children=[
        sidebar_header,
        # sidebar_user,
        # html.Span(print([page["relative_path"]
        #           for page in dash.page_registry.values()])),
        ###### NAV ######
        dbc.Collapse(id="collapse",  className="nav", children=[
            # html.Div(className="nav", children=[
            dbc.Nav(className="nav-item", vertical=True, pills=True, children=[
                # dbc.NavLink(href="/", active="exact", className="nav-link", children=[   #
                #     html.I(
                #         className="nc-icon nc-chart-pie-35"),
                #     html.Span(children="Dashboard"),
                # ]),
                # dbc.NavLink(href="/page-1", active="exact", className="nav-link", children=[
                #     html.I(
                #         className="fas fa-calendar-alt me-2"),
                #     html.Span("Calendar"),
                # ]),
                dbc.NavLink(href=page["relative_path"], active="exact", className="nav-link", children=[
                    html.I(
                        className="fas fa-envelope-open-text me-2"),
                    html.Span(page['name']),
                ])
            ]) for page in dash.page_registry.values()

            # dbc.Nav(className="nav-item", vertical=True, pills=True, children=[
            #     dbc.NavLink(href="/", active="exact", className="nav-link", children=[   #
            #         html.I(
            #             className="nc-icon nc-chart-pie-35"),
            #         html.Span(children="Dashboard"),
            #     ]),
            #     dbc.NavLink(href="/page-1", active="exact", className="nav-link", children=[
            #         html.I(
            #             className="fas fa-calendar-alt me-2"),
            #         html.Span("Calendar"),
            #     ]),
            #     dbc.NavLink(href="/page-2", active="exact", className="nav-link", children=[
            #         html.I(
            #             className="fas fa-envelope-open-text me-2"),
            #         html.Span("Messages"),
            #     ])
            # ]),


            ###### Form ######
            # dbc.Nav(className="nav", vertical=True, pills=True, children=[
            #         dbc.NavItem(className="nav-item", children=[
            #             dbc.NavLink(className="nav-link", href="#", children=[
            #                 html.I(className="nc-icon nc-notes"),
            #                 "Forms",
            #                 html.B(className="caret")
            #             ],
            #                 id="formsExamples",
            #                 # data_toggle="collapse"
            #             )
            #         ]),
            #         dbc.Collapse(id="formsExamples_collapse", children=[
            #             dbc.Nav(className="nav", vertical=True, pills=True, children=[
            #                 dbc.NavItem(className="nav-item", children=[
            #                     dbc.NavLink(className="nav-link", href="./forms/regular.html", children=[
            #                         html.Span(
            #                             "Rf", className="sidebar-mini"),
            #                         html.Span("Regular Forms",
            #                                   className="sidebar-normal")
            #                     ],
            #                     )
            #                 ]),
            #                 dbc.NavItem(className="nav-item", children=[
            #                     dbc.NavLink(className="nav-link", href="./forms/extended.html", children=[
            #                         html.Span(
            #                             "Ef", className="sidebar-mini"),
            #                         html.Span("Extended Forms",
            #                                   className="sidebar-normal")
            #                     ],
            #                     )
            #                 ]),
            #             ]),
            #         ]),
            #     ]),
            # ])
        ]),
        # html.Div(className="sidebar-background",
        #          style={"background-image": "url(./assets/img/sidebar-4.jpg)"})
    ])
])
