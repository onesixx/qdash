import dash
from dash import Dash, html, dcc
import dash_admin_components as dac
from templates import layout
# import alyxdash
# from alyxdash.templates import layout

# from frontend.mainboard.view import navbar, sidebar, body, controlbar, footer
# import pages
# =============================================================================
# Dash App and Flask Server
# =============================================================================
app_dash = dash.Dash(
    __name__,
    use_pages=True
)
app_dash.title = "Cathy Dashboard"

# =============================================================================
# App Layout
# =============================================================================
# app_dash.layout = dac.Page([navbar, sidebar, body, controlbar, footer])
server = app_dash.server

# =============================================================================
# Dash Admin Components
# =============================================================================
# Navbar
right_ui = dac.NavbarDropdown(
    badge_label="!",
    badge_color="danger",
    src="https://quantee.ai",
        header_text="2 Items",
    children=[
        dac.NavbarDropdownItem(
            children="message 1",
            date="today"
        ),
        dac.NavbarDropdownItem(
            children="message 2",
            date="yesterday"
        ),
    ]
)

navbar = dac.Navbar(color="white",
                    text="write text in the navbar!",
                    children=right_ui)

# Sidebar
subitems = [dac.SidebarMenuSubItem(id='tab_gallery_1',
                                   label='Gallery 1',
                                   icon='arrow-circle-right',
                                   badge_label='Soon',
                                   badge_color='success'),
            dac.SidebarMenuSubItem(id='tab_gallery_2',
                                   label='Gallery 2',
                                   icon='arrow-circle-right',
                                   badge_label='Soon',
                                   badge_color='success')
            ]

sidebar = dac.Sidebar(
    dac.SidebarMenu(
        [
            dac.SidebarHeader(children="Cards"),
            dac.SidebarMenuItem(
                id='tab_cards', label='Basic cards', icon='box'),
            dac.SidebarMenuItem(id='tab_social_cards',
                                label='Social cards', icon='id-card'),
            dac.SidebarMenuItem(id='tab_tab_cards',
                                label='Tab cards', icon='image'),
            dac.SidebarHeader(children="Boxes"),
            dac.SidebarMenuItem(id='tab_basic_boxes',
                                label='Basic boxes', icon='desktop'),
            dac.SidebarMenuItem(id='tab_value_boxes',
                                label='Value/Info boxes', icon='suitcase'),
            dac.SidebarHeader(children="Gallery"),
            dac.SidebarMenuItem(label='Galleries',
                                icon='cubes', children=subitems),
        ]
    ),
    title='Dash Admin',
    skin="light",
    color="primary",
    brand_color="primary",
    url="https://quantee.ai",
    src="https://adminlte.io/themes/AdminLTE/dist/img/user2-160x160.jpg",
    elevation=3,
    opacity=0.8
)

# Body
body = dac.Body(
    dac.TabItems([
        # cards_tab,
        # social_cards_tab,
        # tab_cards_tab,
        # basic_boxes_tab,
        # value_boxes_tab,
        dash.page_container,

        dac.TabItem(html.P('Gallery 1 (You can add Dash Bootstrap Components!)'),
                    id='content_gallery_1'),
        dac.TabItem(html.P('Gallery 2 (You can add Dash Bootstrap Components!)'),
                    id='content_gallery_2'),
    ])
)

# Controlbar
controlbar = dac.Controlbar(
    [
        html.Br(),
        html.P("Slide to change graph in Basic Boxes"),
        dcc.Slider(
            id='controlbar-slider',
            min=10,
            max=50,
            step=1,
            value=20
        )
    ],
    title="My right sidebar",
    skin="light"
)

# Footer
footer = dac.Footer(
    html.A("@DawidKopczyk, Quantee",
           href="https://twitter.com/quanteeai",
           target="_blank",
           ),
    right_text="2019"
)

app_dash.layout = dac.Page([navbar, sidebar, body, controlbar, footer])
# =============================================================================
# Callback
# =============================================================================
# alyxdash.callbacks.get_callbacks(app_dash)

# pages.tab_cards.callbacks.get_callbacks(app_dash)
# pages.basic_boxes.callbacks.get_callbacks(app_dash)
# pages.gallery_1.callbacks.get_callbacks(app_dash)
# pages.gallery_2.callbacks.get_callbacks(app_dash)

# =============================================================================
# Run app
# =============================================================================
if __name__ == '__main__':
    app_dash.run_server(debug=False, port=8880)
